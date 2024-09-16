import * as Effect from "effect/Effect";
import * as Console from "effect/Console";
import * as Cli from "@effect/cli";
import { HttpClient, FetchHttpClient } from "@effect/platform";
import { BunContext, BunRuntime } from "@effect/platform-bun";
import * as cheerio from "cheerio";
import type { HttpClientError } from "@effect/platform/HttpClientError";

const csvCmd = Cli.Command.make("csv", {}, ({}) => Console.log("see --help"));

const csvCreateCmd = Cli.Command.make("create", {}, ({}) => createCSV());

const command = csvCmd.pipe(Cli.Command.withSubcommands([csvCreateCmd]));

const cli = Cli.Command.run(command, {
  name: "csv",
  version: "v0.0.1",
});

cli(process.argv).pipe(
  Effect.provide(FetchHttpClient.layer),
  Effect.provide(BunContext.layer),
  BunRuntime.runMain,
);

const createCSV = (): Effect.Effect<
  void,
  HttpClientError,
  HttpClient.HttpClient.Service
> =>
  Effect.gen(function* () {
    const client = (yield* HttpClient.HttpClient).pipe(
      HttpClient.filterStatusOk,
    );
    const response = client
      .get("https://worldwitches.fandom.com/wiki/List_of_Witches")
      .pipe(
        Effect.flatMap((res) => res.text),
        Effect.scoped,
      );
    return yield* response.pipe(
      Effect.map(extract),
      Effect.andThen(Console.log),
    );
  });

type Witch = {
  name: string;
  img: string | null;
  nation: string | null;
  branch: string | null;
  unit: string | null;
  team: string | null;
  birthday: string | null;
};

const empty2null = (s: string): string | null => {
  return s === "" ? null : s;
};

const extract = (html: string): Array<Witch> => {
  const selector = cheerio.load(html);
  const ws: Array<Witch> = [];
  selector(".wikitable tr").each((i, element) => {
    if (i === 0) return;
    const tds = selector(element).find("td");
    ws.push({
      name: tds.eq(0).find("center > a").first().text(),
      img:
        tds.eq(0).find("img").first().attr("data-src") ??
        tds.eq(0).find("img").first().attr("src") ??
        null,
      nation: empty2null(tds.eq(1).text().trim()),
      branch: empty2null(tds.eq(2).text().trim()),
      unit: empty2null(tds.eq(3).text().trim()),
      team: empty2null(tds.eq(4).text().trim()),
      birthday: empty2null(tds.eq(5).text().trim()),
    });
  });
  return ws;
};

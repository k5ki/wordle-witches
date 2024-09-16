import * as Effect from "effect/Effect";
import * as Console from "effect/Console";
import * as Cli from "@effect/cli";
import { BunContext, BunRuntime } from "@effect/platform-bun";

const command = Cli.Command.make(
  "hello",
  {
    action: Cli.Args.text({ name: "action" }),
  },
  ({ action }) => Console.log("Hello via Effect!" + action),
);

const cli = Cli.Command.run(command, {
  name: "hello",
  version: "v0.0.1",
});

cli(process.argv).pipe(Effect.provide(BunContext.layer), BunRuntime.runMain);

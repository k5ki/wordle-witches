from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

html = urlopen("https://worldwitches.fandom.com/wiki/List_of_Witches")

soup = BeautifulSoup(html, "html.parser")

table = soup.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")

with open("./resources/witches.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n", quoting=csv.QUOTE_ALL)
    writer.writerow(["name", "nation", "branch", "unit", "team", "birthday", "image"])
    for row in rows[1:]:
        cells = row.find_all("td")

        img = cells[0].find("img").get("data-src")
        if img is None:
            img = cells[0].find("img").get("src")

        csvRow = [
            cells[0].text,
            cells[1].text,
            cells[2].text,
            cells[3].text,
            cells[4].text,
            cells[5].text,
            img,
        ]
        writer.writerow([r.strip().replace("\n", " ") for r in csvRow])

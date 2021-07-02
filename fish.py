import requests
from bs4 import BeautifulSoup


def get_fish():
    URL = "https://game8.co/games/Animal-Crossing-New-Horizons/archives/281313"
    page = requests.get(URL)

    # Get fish
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("td", class_="center")

    # Filter out a few outliers
    fish = []
    for elem in elements:
        text = elem.text.strip()
        if text == "Tips & Tricks":
            break
        elif "✭" in text:
            text = text[:-5]
            fish.append(text)
        else:
            fish.append(text)
    return fish[12:332]

def parse_data():
    fish = get_fish()
    fish_dict = {}
    for i in range(80):
        offset = i * 4
        fish_dict[fish[offset]] = fish[1 + offset:4 + offset]
    return fish_dict


def create_file():
    fish = parse_data()
    f = open("data/fish.txt", "a")
    for key in fish:
        query = "(" + key + ","
        for item in fish[key]:
            query += item + ","
        query += "0" + ")" + ","
        f.write(query)
    f.close()

create_file()

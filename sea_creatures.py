import requests
from bs4 import BeautifulSoup


def get_sea_creatures():
    URL = "https://game8.co/games/Animal-Crossing-New-Horizons/archives/291125"
    page = requests.get(URL)

    # Get sea creatures
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("td", class_="center")

    # Filter out a few outliers
    sea_creatures = []
    for elem in elements:
        text = elem.text.strip()
        if text == "Tips & Tricks":
            break
        elif "bubbles" in text:
            continue
        else:
            sea_creatures.append(text)
    return sea_creatures[22:-5]


def parse_data():
    sea_creatures = get_sea_creatures()
    sea_creatures_dict = {}
    for i in range(40):
        offset = i * 2
        sea_creatures_dict[sea_creatures[offset]] = sea_creatures[1 + offset]
    return sea_creatures_dict


def create_file():
    sea_creatures = parse_data()
    f = open("data/sea_creatures.txt", "a")
    for key in sea_creatures:
        query = "(" + key + "," + sea_creatures[key] + "," + "1" + ")" + ","
        f.write(query)
    f.close()

create_file()
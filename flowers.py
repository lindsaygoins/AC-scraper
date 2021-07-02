import requests
from bs4 import BeautifulSoup


def get_flowers():
    URL = "https://game8.co/games/Animal-Crossing-New-Horizons/archives/281316"
    page = requests.get(URL)

    # Get flowers
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("td", class_="center")

    # Filter out a few outliers
    flowers = []
    for elem in elements:
        text = elem.text.strip()
        if text in flowers:
            break
        if "White" in text or "Red" in text or "Yellow" in text:
            continue
        if " " in text:
            flowers.append(text)

    flowers.remove("Orange Windflower")
    flowers.remove("Lily of the Valley")

    flower_dict = {
        "Rose": flowers[:6],
        "Tulip": flowers[6:10],
        "Hyacinth": flowers[10:14],
        "Mum": flowers[14:17],
        "Pansy": flowers[17:20],
        "Lily": flowers[20:23],
        "Windflower": flowers[23:26],
        "Cosmos": flowers[26:]
    }

    return flower_dict

def create_file():
    flowers = get_flowers()
    f = open("data/flowers.txt", "a")
    for key in flowers:
        for item in flowers[key]:
            query = "(" + key + "," + item + "," + "0" + ")" + ","
            f.write(query)
    f.close()

create_file()
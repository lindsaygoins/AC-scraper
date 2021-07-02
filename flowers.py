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

    return flowers


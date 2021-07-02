import requests
from bs4 import BeautifulSoup


def get_wall_floor_rugs():
    URL = "https://game8.co/games/Animal-Crossing-New-Horizons/archives/286678"
    page = requests.get(URL)

    # Get DIYS
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("td", class_="center")

    # Filter out a few outliers
    wall_floor_rugs = []
    for elem in elements:
        text = elem.text.strip()
        if text == "List of DIY Recipes":
            break
        else:
            wall_floor_rugs.append(text)
    return wall_floor_rugs

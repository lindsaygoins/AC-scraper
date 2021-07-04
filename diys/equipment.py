import requests
from bs4 import BeautifulSoup


def get_equipment():
    URL = "https://game8.co/games/Animal-Crossing-New-Horizons/archives/286679"
    page = requests.get(URL)

    # Get DIYS
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("td", class_="center")

    # Filter out a few outliers
    equipment = []
    for elem in elements:
        text = elem.text.strip()
        if text == "List of DIY Recipes":
            break
        if text != "Currently no items to display.":
            equipment.append(text)
    return equipment
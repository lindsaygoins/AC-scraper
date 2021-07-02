import requests
from bs4 import BeautifulSoup


def get_misc():
    URL = "https://game8.co/games/Animal-Crossing-New-Horizons/archives/286676"
    page = requests.get(URL)

    # Get DIYS
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("td", class_="center")

    # Filter out a few outliers
    misc = []
    for elem in elements:
        text = elem.text.strip()
        if text == "List of DIY Recipes":
            break
        if len(text) > 1 and text != "Currently no items to display.":
            misc.append(text)
    return misc
import requests
from bs4 import BeautifulSoup


def get_housewares():
    URL = "https://game8.co/games/Animal-Crossing-New-Horizons/archives/286675"
    page = requests.get(URL)

    # Get DIYS
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("td", class_="center")

    # Filter out a few outliers
    housewares = []
    for elem in elements:
        text = elem.text.strip()
        if text == "List of DIY Recipes":
            break
        if len(text) > 1 and text != "Currently no items to display.":
            housewares.append(text)
    return housewares

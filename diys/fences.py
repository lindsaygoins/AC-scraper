import requests
from bs4 import BeautifulSoup


def get_fences():
    URL = "https://game8.co/games/Animal-Crossing-New-Horizons/archives/284860"
    page = requests.get(URL)

    # Get DIYS
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("td", class_="center")

    # Filter out a few outliers
    fences = []
    for elem in elements:
        text = elem.text.strip()
        if text == "List of DIY Recipes":
            break
        else:
            fences.append(text)
    return fences

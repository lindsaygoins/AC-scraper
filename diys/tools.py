import requests
from bs4 import BeautifulSoup


def get_tools():
    URL = "https://game8.co/games/Animal-Crossing-New-Horizons/archives/286711"
    page = requests.get(URL)

    # Get DIYS
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("td", class_="center")

    # Filter out a few outliers
    tools = []
    for elem in elements:
        text = elem.text.strip()
        if text == "List of DIY Recipes":
            break
        else:
            tools.append(text)
    return tools[10:52]
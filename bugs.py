import requests
from bs4 import BeautifulSoup


def get_bugs():
    URL = "https://game8.co/games/Animal-Crossing-New-Horizons/archives/281312"
    page = requests.get(URL)

    # Get bugs
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("td", class_="center")

    # Filter out a few outliers
    bugs = []
    for elem in elements:
        text = elem.text.strip()
        if text == "Tips & Tricks":
            break
        else:
            bugs.append(text)
    return bugs[12:]

print(get_bugs())
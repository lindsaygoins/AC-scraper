import requests
from bs4 import BeautifulSoup


def get_art():
    URL = "https://game8.co/games/Animal-Crossing-New-Horizons/archives/281329"
    page = requests.get(URL)

    # Get art
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("td", class_="center")

    # Filter out a few outliers
    art = {
        "Painting": [],
        "Statue": []
    }
    art_set = set()

    for elem in elements:
        text = elem.text.strip()
        if text not in art_set:
            art_set.add(text)
            if "Painting" in text:
                art["Painting"].append(text)
            if "Statue" in text:
                art["Statue"].append(text)
        else:
            break
    return art

def create_file():
    art = get_art()
    f = open("data/art.txt", "a")
    for key in art:
        for item in art[key]:
            query = "(" + item + "," + key + "," + "0" + "," + "0" + ")" + ","
            f.write(query)
    f.close()

create_file()
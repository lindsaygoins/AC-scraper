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
        elif "Season" in text:
            continue
        elif "★" in text:
            text = text[5:]
            bugs.append(text)
        else:
            bugs.append(text)
    return bugs[12:332]


def parse_data():
    bugs = get_bugs()
    bug_dict = {}
    for i in range(80):
        offset = i * 4
        bug_dict[bugs[offset]] = bugs[1 + offset:4 + offset]
    return bug_dict


def create_file():
    bugs = parse_data()
    f = open("data/bugs.txt", "a")
    for key in bugs:
        query = "(" + key + ","
        for item in bugs[key]:
            query += item + ","
        query += "0" + ")" + ","
        f.write(query)
    f.close()

create_file()

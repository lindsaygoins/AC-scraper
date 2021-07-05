import requests
from bs4 import BeautifulSoup


def get_saharah_items():
    URL = "https://www.eurogamer.net/articles/animal-crossing-saharah-departure-tickets-mysterious-wallpaper-flooring-new-horizons-7018"
    page = requests.get(URL)

    # Get Saharah items
    soup = BeautifulSoup(page.content, "html.parser")
    elements = soup.find_all("li")

    # Filter out a few outliers
    items = []
    for elem in elements:
        text = elem.text.strip()
        if text == "Animal Crossing (Switch) Review":
            break
        elif " (animated)" in text:
            text = text[:-11]
            items.append(text)
        else:
            items.append(text)

    items = items[14:]

    rugs_dict = {
        "Small": items[91:122],
        "Medium": items[122:165],
        "Large": items[165:]
    }

    items_dict = {
        "Wallpaper": items[:52],
        "Flooring": items[52:91],
        "Rugs": rugs_dict
    }

    return items_dict

def create_file():
    items = get_saharah_items()
    f = open("data/saharah_items.txt", "a")
    for key in items["Rugs"]:
        for value in items["Rugs"][key]:
            query = "(" + value + "," + "Rug" + "," + key + "," + "0" + "," + "0" + ")" + ","
            f.write(query)

    for key in items:
        if key == "Rugs":
            break
        for value in items[key]:
            query = "(" + value + "," + key + "," + "0" + "," + "0" + ")" + ","
            f.write(query)
    f.close()

create_file()
from bs4 import BeautifulSoup as bs
import requests


def get_weather(shaxar):
    url = f"https://sinoptik.ua/погода-{shaxar}"
    response = requests.get(url=url)

    if response.status_code != 200:
        return None

    soup = bs(response.content, "html5lib")
    table = soup.find('table', attrs={"class": "weatherDetails"})
    

    harorat = table.findAll('td', attrs={"class": "cur"})
    if not harorat or len(harorat) < 7:
        return None

    ob_havo = {
        "Vaqt": harorat[0].text.strip(),
        "Harorat": harorat[2].text.strip(),
        "Bosim": harorat[4].text.strip(),
        "Namlik": harorat[5].text.strip(),
        "Shamol": harorat[6].text.strip()
    }
    return ob_havo

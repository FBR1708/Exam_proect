from threading import Thread

import httpx,json
def bir():
    url1 = 'https://api.chucknorris.io/jokes/random'
    first = httpx.get(url1)
    l = first.json()
    with open('first.json', 'w') as f:
        json.dump(l, f, indent=4)


def ikki():
    url2 = 'https://api.chucknorris.io/jokes/categories'
    second = httpx.get(url2)
    l = second.json()
    with open('second.json', 'w') as f:
        json.dump(l, f, indent=4)


def uch():
    url3 = 'https://api.chucknorris.io/jokes/categories'
    third = httpx.get(url3)
    l = third.json()
    with open('third.json', 'w') as f:
        json.dump(l, f, indent=4)


def tort():
    url4 = 'https://api.chucknorris.io/jokes/search?query={query}'
    four = httpx.get(url4)
    l = four.json()
    with open('four.json', 'w') as f:
        json.dump(l, f, indent=4)


def besh():
    url5 = 'https://api.chucknorris.io/jokes/random?category={category}'
    birinchi = httpx.get(url5)
    l = birinchi.json()
    with open('five.json', 'w') as f:
        json.dump(l, f, indent=4)
oqim1 = Thread(target=bir(), daemon=True)
oqim2 = Thread(target=ikki(), daemon=True)
oqim3 = Thread(target=uch(), daemon=True)
oqim4 = Thread(target=tort(), daemon=True)
oqim5 = Thread(target=besh(), daemon=True)
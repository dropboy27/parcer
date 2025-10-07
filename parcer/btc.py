import requests
from bs4 import BeautifulSoup


def date_btc():
    req = requests.get(
        "https://www.blockchain.com/ru/explorer/blocks/btc/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f")
    src = req.text

    soup = BeautifulSoup(src, 'lxml')

    data = soup.find(
        "div", class_="sc-d60e75c0-7 iwMRhg").text.replace(".", "").replace(",", "").split()

    months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
              'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    for i in months:
        if data[1] in i:
            month = months[i]
            break
    month = str(month).zfill(2)
    date = str(data[2]).zfill(2)
    year = str(data[3]).zfill(4)

    date = year+month+date

    return date

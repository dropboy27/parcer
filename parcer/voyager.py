import requests
from bs4 import BeautifulSoup


def voyager_date():
    req = requests.get("https://science.nasa.gov/mission/voyager/voyager-1/")
    src = req.text

    soup = BeautifulSoup(src, 'lxml')

    data = soup.find_all(
        "div", class_=["p-lg font-weight-bold margin-0 padding-0 line-height-sm"])[1]\
        .text.replace(".", "").replace(",", "").split()

    months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
              'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    for i in months:
        if data[0] in i:
            month = months[i]
            break
    month = str(month).zfill(2)
    date = str(data[1]).zfill(2)
    year = str(data[2]).zfill(4)

    voyager_date = year+month+date

    return voyager_date

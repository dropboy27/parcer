import requests
from bs4 import BeautifulSoup


def rfc_date():
    req = requests.get("https://datatracker.ietf.org/doc/rfc1149/history/")
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    data = soup.find(
        "tr", id="history-264954").find("div").text.replace("-", "")
    return data

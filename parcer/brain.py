import requests
from bs4 import BeautifulSoup


def brain_codepoint():
    req = requests.get(
        "https://unicode.org/emoji/charts/full-emoji-list.html")
    src = req.text
    soup = BeautifulSoup(src, "lxml")

    codepoint = soup.find("td", class_="code").find("a").text
    return codepoint


print(brain_codepoint())

import requests
from bs4 import BeautifulSoup


def c_isbn():

    req = requests.get(
        "https://www.oreilly.com/library/view/c-programming-language/9780133086249/copyright.xhtml")
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    isbn = soup.find(
        "div", id="sbo-rt-content").find("code").text.split("ISBN")[-1].split()[0].replace("-", "")

    return isbn

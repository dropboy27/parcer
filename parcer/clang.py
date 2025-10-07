import requests
from bs4 import BeautifulSoup


def c_isbn():

    req = requests.get(
        "https://www.oreilly.com/library/view/c-programming-language/9780133086249/copyright.xhtml")
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    data = soup.find("div", class_="css-ge5d1n").find("span",
                                                      class_="MuiTypography-root MuiTypography-textBody css-1dv4x0j").text.split()
    isbn = data[1]

    return isbn

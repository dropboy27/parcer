import requests
from bs4 import BeautifulSoup, SoupStrainer


def brain_codepoint():
    req = requests.get(
        "https://www.unicode.org/Public/emoji/16.0/emoji-test.txt",)
    src = req.text
    for line in src.split("\n"):
        if "🧠" in line:
            codepoint = line.split()[0]
            break
    return codepoint

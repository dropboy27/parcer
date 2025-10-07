import hashlib
from src.brain import brain_codepoint
from src.btc import date_btc
from src.clang import c_isbn
from src.rfc import rfc_date
from src.voyager import voyager_date


def main():
    flag_string = f"FLAG{{{voyager_date()}-{rfc_date()}-{brain_codepoint()}-{date_btc()}-{c_isbn()}}}"
    sha256 = hashlib.sha256(flag_string.encode()).hexdigest()
    print(sha256)
    print(sha256 == "d311f26ea1a995af669a62758ad5e0ce2583331059fbfc5c04cc84b2d41f4aed")


if __name__ == "__main__":
    main()

# voyager_date - https://science.nasa.gov/mission/voyager/voyager-1/
# rfc1149_date - https://www.oreilly.com/library/view/c-programming-language/9780133086249/copyright.xhtml
# brain_codepoint - https://www.unicode.org/Public/emoji/16.0/emoji-test.txt
# btc_genesis_date - https://www.blockchain.com/ru/explorer/blocks/btc/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
# kr2_isbn10 - https://datatracker.ietf.org/doc/rfc1149/history/

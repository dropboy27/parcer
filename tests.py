import re
from src.voyager import voyager_date
from src.rfc import rfc_date
from src.brain import brain_codepoint
from src.btc import date_btc
from src.clang import c_isbn


def test_voyager():
    """Дата Voyager: 8 цифр"""
    result = voyager_date()
    assert re.match(
        r'^\d{8}$', result), f"Ожидалось 8 цифр, получено: {result}"
    print(f"Voyager date: {result}")


def test_rfc():
    """Дата RFC: 8 цифр"""
    result = rfc_date()
    assert re.match(
        r'^\d{8}$', result), f"Ожидалось 8 цифр, получено: {result}"
    print(f"RFC date: {result}")


def test_brain():
    """Кодпоинт: hex без U+"""
    result = brain_codepoint()
    assert re.match(
        r'^[0-9A-F]+$', result), f"Ожидались hex-цифры без U+, получено: {result}"
    print(f"Brain codepoint: {result}")


def test_btc():
    """Дата Bitcoin: 8 цифр"""
    result = date_btc()
    assert re.match(
        r'^\d{8}$', result), f"Ожидалось 8 цифр, получено: {result}"
    print(f"BTC date: {result}")


def test_isbn():
    """ISBN: 10 цифр без дефисов"""
    result = c_isbn()
    assert re.match(
        r'^\d{10}$', result), f"Ожидалось 10 цифр без дефисов, получено: {result}"
    print(f"ISBN: {result}")


if __name__ == '__main__':

    try:
        test_voyager()
        test_rfc()
        test_brain()
        test_btc()
        test_isbn()
        print("\nВсе тесты пройдены")
    except AssertionError as e:
        print(f"\nОшибка: {e}")

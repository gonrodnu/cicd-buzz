import unittest

from lxml import etree

from app import generate_buzz

def test_generate_buzz():
    parser = etree.HTMLParser()
    root = etree.fromstring(generate_buzz(), parser)
    errors = len(parser.error_log)
    if errors != 0:
        print(parser.error_log[0].message)
    assert errors == 0



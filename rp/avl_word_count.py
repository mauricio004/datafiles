# -*- coding: utf-8 -*-
import csv
import re
import unicodedata
from bs4 import BeautifulSoup


def cleanData(filename):
    """Returns an string

    filename: Delimited file with text and html.  Convert html to readable format.  Convert unicode to string
    """
    id_dict = {}
    with open(filename, "rb") as f:
        raw = BeautifulSoup(f).get_text()
    raw_text = unicodedata.normalize('NFKD', raw).encode('ascii', 'ignore')
    return raw_text


def readData(rawtxt):
        """
        xxx
        """

        # email_text = re.findall(r'CustomerID:(\d+),\s*(.*?)\s*(?=CustomerID:|$)', rawtxt, re.DOTALL)
        # email_text = re.findall(r'CustomerID:(\d+),(.*?)(?=CustomerID:)', rawtxt, re.DOTALL)
        email_text = re.findall(r'CustomerID:(\d+).*?(Comments:.*?)(?=CustomerID:)', rawtxt, re.DOTALL)
        return email_text

if __name__ == '__main__':
    filename = "C:/Users/mflores1/datafiles/rp/sample.csv"
    try:
        t = cleanData(filename)
    except IOError:
        print 'Cannot open file'

    output = readData(t)
    # print output
    for o in output:
        print o


    # tWrite = open("C:/Users/mflores1/datafiles/rp/t.txt", 'w')
    # tWrite.write(t)

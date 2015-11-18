import csv
import re
from bs4 import BeautifulSoup


def extractData(filename):
    """Returns a dictionary with 'CustomerID' and comments for each guest card

    filename: .csv file with customer id and email text from prospects
    """
    idDict = {}
    #with open(filename, "r") as f:
    #    for line in f:
    #        print line
    f = open(filename, 'r')
    raw = BeautifulSoup(f).get_text()
    print raw

if __name__ == '__main__':
    filename = "C:/Users/mflores1/datafiles/rp/sample.csv"
    try:
        extractData(filename)
    except IOError:
        print 'Cannot find file or directory'



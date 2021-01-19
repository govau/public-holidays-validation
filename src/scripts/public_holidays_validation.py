import csv
import datetime
import urllib.request

import pandas as pd

from blank_validation import checkBlankData
from date_validation import checkDateData
from jurisdiction_validation import checkJurisdictionData
from url_validation import checkURLData

filePath = "../../test/test.csv"
data = pd.read_csv(filePath)

numErrors = 0

validYear = False
while (validYear == False):
    try:
        print("Please enter a valid year in YYYY format.")
        currYear = input()
        datetime.datetime.strptime(currYear, "%Y")
        break
    except ValueError:
        print("Inputted date", currYear, "is invalid.")

for index, row in pd.DataFrame(data).iterrows():
    # Check blank data in row
    if (checkBlankData(index, row)):
        numErrors += 1
    # Check date data in row
    elif (checkDateData(index, str(int(row['Date'])), currYear)):
        numErrors += 1
    # Check url data in row
    elif (checkURLData(index, row['More Information'])):
        numErrors += 1
    # Check jurisdiction data in row
    elif (checkJurisdictionData(index, row['Jurisdiction'])):
        numErrors += 1


if (numErrors == 0):
    print("----------\nNo date errors reported.")
else:
    print("----------")
    raise Exception("TOTAL NUMBER OF ERRORS: " +
                    str(numErrors) + "\n----------\n")
print("----------")

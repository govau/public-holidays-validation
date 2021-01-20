import csv
import datetime
import os
import sys
import urllib.request

import pandas as pd

from blank_validation import checkBlankData
from date_validation import checkDateData
from jurisdiction_validation import checkJurisdictionData
from url_validation import checkURLData

# Check file exists and is valid
filePath = "../files/"+sys.argv[1]+".csv"
data = ""
if (os.path.exists(filePath)):
    data = pd.read_csv(filePath)
else:
    raise Exception("Inputted file", filePath, "is invalid.")

# Extract desired years from name
filenameSplit = sys.argv[1].split("_")
startYear = ""
endYear = ""
if (len(filenameSplit) == 4):
    startYear = filenameSplit[3]
elif (len(filenameSplit) == 5):
    startYear = filenameSplit[3]
    endYear = filenameSplit[4]

try:
    datetime.datetime.strptime(startYear, "%Y")
    if (endYear != ""):
        datetime.datetime.strptime(endYear, "%Y")
except ValueError:
    print("Please add the start (and end years, if appropriate) to the filename. e.g. australian_public_holidays_<startyear>_<endyear>")
    sys.exit()


numErrors = 0

for index, row in pd.DataFrame(data).iterrows():
    # Check blank data in row
    if (checkBlankData(index, row)):
        numErrors += 1
    # Check date data in row
    elif (checkDateData(index, str(int(row['Date'])), startYear, endYear)):
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

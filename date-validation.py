import csv
import datetime
import math

import pandas as pd

filePath = "./test-invalid-dates.csv"
validYear = False
while (validYear == False):
    try:
        print("Please enter a valid year in YYYY format.")
        currYear = input()
        datetime.datetime.strptime(currYear, "%Y")
        break
    except ValueError:
        print("Inputted date", currYear, "is invalid.")

date_format = '%Y%m%d'
data = pd.read_csv(filePath)
errors = False
for index, row in pd.DataFrame(data).iterrows():
    try:
        if (math.isnan(row['Date'])):
            date = "<empty>"
        else:
            date = str(int(row['Date']))
        date_obj = datetime.datetime.strptime(date, date_format)
        if (str(date_obj.year) != currYear):
            errors = True
            print("----------\nWrong year. Current year is", currYear,
                  "but written year is", str(date_obj.year) + ". \n" +
                  "Holiday:", row['Holiday Name'], "from", row['Jurisdiction'])

    except ValueError:
        errors = True
        print("----------\nInvalid date. Date listed is", date,
              "but date needs to exist and be in YYYYMMDD format.\n" +
              "Holiday:", row['Holiday Name'], "from", row['Jurisdiction'])
if (errors == False):
    print("----------\nNo date errors reported.")
print("----------")

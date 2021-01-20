import csv
import datetime

import pandas as pd


def checkDateData(index, date, startYear, endYear):
    date_format = '%Y%m%d'
    errors = False
    try:
        date_obj = datetime.datetime.strptime(date, date_format)
        if (str(date_obj.year) != startYear and endYear == ""):
            errors = True
            print("----------\nWrong year. Current year is", startYear,
                  "but written year is", str(date_obj.year), "in row", index+2)
        elif (date_obj.year < int(startYear) or (endYear != "" and date_obj.year > int(endYear))):
            errors = True
            print("----------\nWrong year. Written year is", str(date_obj.year),
                  "but this file only lists years", startYear, "to", endYear, "in row", index+2)
    except ValueError:
        errors = True
        print("----------\nInvalid date. Date listed is", date,
              "but date needs to exist and be in YYYYMMDD format in row", index+2)

    return errors

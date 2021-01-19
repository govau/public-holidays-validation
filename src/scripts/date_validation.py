import csv
import datetime

import pandas as pd


def checkDateData(index, date, currYear):
    date_format = '%Y%m%d'
    errors = False
    try:
        date_obj = datetime.datetime.strptime(date, date_format)
        if (str(date_obj.year) != currYear):
            errors = True
            print("----------\nWrong year. Current year is", currYear,
                  "but written year is", str(date_obj.year), "in row", index+2)

    except ValueError:
        errors = True
        print("----------\nInvalid date. Date listed is", date,
              "but date needs to exist and be in YYYYMMDD format in row", index+2)

    return errors

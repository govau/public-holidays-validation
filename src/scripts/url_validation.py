import csv
import re

import pandas as pd


def checkURLData(index, url):
    errors = False
    if ".gov.au" not in url:
        errors = True
        print("----------\nFaulty URL:", url,
              "\nURL needs to be from an Australian Government domain (.gov.au) in row", index+2)
    else:
        # READ PYTHON URL AND CHECK REGEX
        regex = re.compile(
            "https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
        if (str(regex.match(url)) == "None"):
            errors = True
            print("----------\nFaulty URL:", url,
                  "\nURL requires an \"https://\" signature in row", index+2)
    return errors

import csv
import urllib.request

import pandas as pd


def checkURLData(index, url):
    errors = False
    if ".gov.au" not in url:
        errors = True
        print("----------\nFaulty URL:", url,
              "\nURL needs to be from an Australian Government domain (.gov.au) in row", index+2)
    else:
        try:
            statusCode = urllib.request.urlopen(url).getcode()
        except ValueError:
            errors = True
            print("----------\nFaulty URL:", url,
                  "\nURL requires an \"https://www\" signature in row", index+2)
        except urllib.error.HTTPError as e:
            errors = True
            print("----------\nFaulty URL:", url, "\nURL returns an HTTP", e.code,
                  "code in row", index+2)
    return errors

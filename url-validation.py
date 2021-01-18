import csv
import math
import urllib.request

import pandas as pd

filePath = "./test-invalid-url.csv"
data = pd.read_csv(filePath)

for index, row in pd.DataFrame(data).iterrows():
    if (str(row['More Information']) == "nan"):
        print("----------\nURL slot is empty.\nHoliday:",
              row['Holiday Name'], "from", row['Jurisdiction'].upper())
    else:
        url = row['More Information']
        if ".gov.au" not in url:
            print("----------\nFaulty URL:", url, "\nURL needs to be from an Australian Government domain (.gov.au).\nHoliday:",
                  row['Holiday Name'], "from", row['Jurisdiction'].upper())
        else:
            try:
                statusCode = urllib.request.urlopen(url).getcode()
            except ValueError:
                print("----------\nFaulty URL:", url, "\nURL requires an \"https://www\" signature.\nHoliday:",
                      row['Holiday Name'], "from", row['Jurisdiction'].upper())
            except urllib.error.HTTPError as e:
                print("----------\nFaulty URL:", url, "\nURL returns an HTTP", e.code,
                      "code.\nHoliday:", row['Holiday Name'], "from", row['Jurisdiction'].upper())

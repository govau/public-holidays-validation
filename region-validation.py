import csv

import pandas as pd

filePath = "./test-invalid-region.csv"
data = pd.read_csv(filePath)

for index, row in pd.DataFrame(data).iterrows():
    region = str(row['Jurisdiction'])
    if (region == "nan"):
        print("----------\nJurisdiction is left blank for holiday:",
              row['Holiday Name'])
    elif (region != "act" and region != "nsw" and region != "nt" and region != "qld" and region != "sa" and region != "tas" and region != "vic" and region != "wa"):
        print("----------\nInvalid state or territory:", region, "\nFor holiday:",
              row["Holiday Name"], "\nThe data is case-sensitive, ensure there are no punctuations or uppercase letters.")

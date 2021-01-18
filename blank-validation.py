import csv

import pandas as pd

filePath = "./test.csv"
data = pd.read_csv(filePath)

for index, row in pd.DataFrame(data).iterrows():
    if (str(row['Date']) == "nan"):
        print("----------\nDate is left blank.")
    elif(str(row['Holiday Name']) == "nan"):
        print("----------\nHoliday Name is left blank.")
    elif(str(row['Information']) == "nan"):
        print("----------\nInformation is left blank.")
    elif(str(row['More Information']) == "nan"):
        print("----------\nMore Information is left blank.")
    elif(str(row['Jurisdiction']) == "nan"):
        print("----------\nJurisdiction is left blank.")

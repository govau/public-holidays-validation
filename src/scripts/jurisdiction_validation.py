import csv

import pandas as pd


def checkJurisdictionData(index, jurisdiction):
    if (jurisdiction != "act"
            and jurisdiction != "nsw"
            and jurisdiction != "nt"
            and jurisdiction != "qld"
            and jurisdiction != "sa"
            and jurisdiction != "tas"
            and jurisdiction != "vic"
            and jurisdiction != "wa"):
        print("----------\nInvalid state or territory:",
              jurisdiction, "in row", index + 2)
        return True
    else:
        return False

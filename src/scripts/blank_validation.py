def checkBlankData(index, row):
    errors = False
    if (str(row['Date']) == "nan"):
        errors = True
        print("----------\nDate is left blank in row", index+2)
    elif(str(row['Holiday Name']) == "nan"):
        errors = True
        print("----------\nHoliday Name is left blank in row", index+2)
    elif(str(row['Information']) == "nan"):
        errors = True
        print("----------\nInformation is left blank in row", index+2)
    elif(str(row['More Information']) == "nan"):
        errors = True
        print("----------\nMore Information is left blank in row", index+2)
    elif(str(row['Jurisdiction']) == "nan"):
        errors = True
        print("----------\nJurisdiction is left blank in row", index+2)
    return errors

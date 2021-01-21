# Validation Scripts

The validate.py script automatically runs all the helper scripts for a composite data health check.
**Primary validation script:** 
validate.py

**Helper scripts:**
- blank_validation.py
- date_validation.py
- url_validation.py
- jurisdiction_validation.py

## Validation parameters:

### File name
Checks that the file name is valid. A valid name is one that includes:
- Either singular parameter: australian_public_holidays_<year>.csv
- Or, start and end year: australian_public_holidays_<startyear>_<endyear>.csv
This file name structure will be used to extract the dates / date duration, to ensure all dates in the csv are in that range.

### Blank data
Checks for blank entries in the data, such as an empty row or an empty cell within a row, and will throw an exception.

### Date data
Checks all data in the "Date" column. A valid date is:
- In the format (YYYYMMDD)
- In the correct year (based on the file name above)
- Or, within the correct year duration for a composite-year dataset (based on the file name above)
Failures in any of the above will throw an exception.

### URL data
Checks for valid URLs in the "More Information" column. 
- URL contains ".gov.au" address
- URL matches a specific regex URL format (from https://urlregex.com/)

** Please note that this URL-validation is purely a regex text comparison, and does not send requests to determine the validity of the link itself.**

### Jurisdiction data
Checks that only the jurisdictions of Australia (act, nsw, nt, qld, sa, tas, vic, wa) are accepted as entries. Additionally, only lowercase entry names are accepted.

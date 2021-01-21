# Public Holidays Dataset Validation

This repository provides scripts to validate the public holidays dataset, located at: https://data.gov.au/data/dataset/australian-holidays-machine-readable-dataset

_Note: the year validations are automatically generated from the filename._

- Filename `australian_public_holidays_2021` will check that all dates in the csv are from 2021.
- Filename `australian_public_holidays_2021_2022` will validate for all dates between 2021-2022 inclusive.

A full list of used validation parameters can be found in src/scripts/README.md.

## Setup

Make sure you have Python 3 and Pandas installed.
Make sure all files you wish to validate are in the **src/files** folder, and are of type **.CSV**

## Run (locally)

1. Navigate to the repository's root directory.
2. Run `./validateAllFiles.sh`

*If a Permission Denied error occurs, modify the permissions first by running `chmod a+x ./validateAllFiles.sh` and then rerunning the above command.*

3. All files in the src/files folder will be validated. 
If all data from a CSV is valid, the following output will be produced:

``` 
----------
<name of csv checked>
----------
No date errors reported.
----------
```

If any of the data in any of the files are invalid, an exception will be thrown. Information about the error as well as the total number of errors in the file will be listed in the error message. An example of an error message is below:

```
----------
<name of csv checked>
----------
Wrong year. Current year is 2021 but written year is 2020 in row 8
----------
Traceback (most recent call last):
  <error location>
Exception: TOTAL NUMBER OF ERRORS: 1
----------
```

## Run (GitHub through CircleCI)

CircleCI runs the above validateAllFiles.sh script, so when a pull request is submitted, invalid data in the above scripts will fail the CircleCI build-and-test. You can launch CircleCI to see the exceptions raised and fix them accordingly.

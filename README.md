# Public Holidays Dataset Validation

This repository provides scripts to validate the public holidays dataset, located at: https://data.gov.au/data/dataset/australian-holidays-machine-readable-dataset

_Note: the year validations are automatically generated from the filename._

- Filename `australian_public_holidays_2021` will check that all dates in the csv are from 2021.
- Filename `australian_public_holidays_2021_2022` will validate for all dates between 2021-2022 inclusive.

## Setup

Make sure you have Python 3 and Pandas installed

## Run

`cd src/scripts`

`python3 validate.py <name of CSV to compare without extension>`

For example, to validate the 2020 csv:

`python3 validate.py australian_public_holidays_2020`

To validate the composite (future years, i.e. 2021-2022) csv:

`python3 validate.py australian_public_holidays_2021_2022`

#!/bin/bash

for file in ./src/files/*.csv; do
    filename=`basename ./src/files/$file .csv`
    echo $filename
    python3 ./src/scripts/validate.py $filename
done
#!/bin/bash
pip3 install virtualenv
virtualenv smart_mirror
. smart_mirror/bin/activate

pip3 install -r requirements.txt

echo What is your zip code?
read ZIP_CODE

sed -i '' "s/zip_code =.*/zip_code = ${ZIP_CODE}/g" src/weather.py

echo "Do you need to create or edit a .env file? (Y/n)"
read CREATE_FILE

if [ $CREATE_FILE = "Y" ]; then
    echo What is your Weather API Key?
    read WEATHER_API_KEY
    echo What is your NYT Devloper API Key?
    read NYT_API_KEY

    echo "WEATHER_API_KEY=${WEATHER_API_KEY}" > .env
    echo "NYT_API_KEY=${NYT_API_KEY}" >> .env
fi

echo Starting Smart Mirror...
python3 ./src/mainframe.py
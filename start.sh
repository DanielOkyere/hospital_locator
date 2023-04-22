#!/bin/bash

# Setup Environment and run app
echo "Activating environment" &&
source env/bin/activate &&

#install all requirements from requirements.txt
echo "Installing python requirements &&"
pip install -r ./requirement.txt &&

#Start app.py
uvicorn app:app --reload 

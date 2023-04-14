#!/bin/bash


#Start app.py
uvicorn app:app --reload &

#Wait for app to start and run 
cd ./frontend && npm run dev
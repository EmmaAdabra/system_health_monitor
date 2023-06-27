#!/usr/bin/env python3

from datetime import datetime
import os


def create_date_file(date, file_name):
    with open(file_name, mode='w') as date_file:
        date_file.write(date)


def get_date(date_file):
    with open(date_file, mode='r') as date_file:
        return(date_file.read())

def update_date(date, date_file):
    with open(date_file, mode='w') as date_file:
        date_file.write(date)

def current_date():
    date_file_name = ".today_date"
    date = datetime.today()
    today_date = date.today().strftime("%B %d, %Y")
    current_time = date.strftime("%H:%M:%S")
    dict_date = {"date":today_date, "time":current_time}

    if  not os.path.exists(date_file_name):
        create_date_file(today_date, date_file_name)
        return dict_date
    else:
        if get_date(date_file_name) == today_date:
            dict_date["date"] = None
            return dict_date
        else:
            update_date(today_date, date_file_name)
            dict_date["date"] = today_date
            return dict_date

# date = current_date()
# print(date)
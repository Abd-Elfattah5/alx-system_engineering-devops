#!/usr/bin/python3
""" a module that uses the request library
to fetch data using the JSONPlaceholder API
and put all the data inside a csv file
"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    link = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    task_req = requests.get(link + "/todos")
    usr_req = requests.get(link)

    tasks_info = task_req.json()
    usr = usr_req.json()["name"]

    headers = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    file_name = "{}.csv".format(employee_id)

    with open(file_name, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for task in tasks_info:
            writer.writerow([employee_id, usr, task["completed"], task["title"]])

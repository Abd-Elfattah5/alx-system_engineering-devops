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
    usr_info = usr_req.json()

    headers = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

    data = [{"USER_ID": usr_info["id"], "USERNAME": usr_info["name"],
            "TASK_COMPLETED_STATUS": task["completed"], "TASK_TITLE": task["title"]}
            for task in tasks_info]

    file_name = "{}.csv".format(employee_id)

    with open(file_name, mode='w', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)

        writer.writerows(data)

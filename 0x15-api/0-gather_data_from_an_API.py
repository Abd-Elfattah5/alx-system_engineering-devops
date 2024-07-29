""" a module that uses the request library
to fetch data using the JSONPlaceholder API"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    link = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    task_req = requests.get(link + "/todos")
    usr_req = requests.get(link)

    tasks_info = task_req.json()
    usr_info = usr_req.json()
    completed = 0
    total = len(tasks_info)
    for task in tasks_info:
        if task["completed"] is True:
            completed += 1

    text = "Employee {} is done with tasks({}/{}):".format(
            usr_info["name"], completed, total)
    print(text)
    for task in tasks_info:
        if task["completed"] is True:
            print("\t ", end='')
            print(task["title"])

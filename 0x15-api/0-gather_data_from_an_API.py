#!/usr/bin/python3
'''
    This module contains a Python script that gathers data from an API.

    Given an employee ID, the script returns information about their
    To-Do list progress.
'''


import requests
from sys import argv

if __name__ == '__main__':
    employee_id = argv[1]
    url_api = "https://jsonplaceholder.typicode.com"

    url_employee = "{}/users/{}".format(url_api, employee_id)
    employee = requests.get(url_employee).json()
    employee_name = employee['name']

    url_employee_todos = "{}/todos?userId={}".format(url_api, employee_id)
    employee_todos = requests.get(url_employee_todos).json()

    tasks_titles = []
    task_count = 0
    for tasks in employee_todos:
        if tasks['completed'] is True:
            tasks_titles.append(tasks['title'])
            task_count += 1

    print("Employee {} is done with tasks({}/{})".format(employee_name,
                                                         task_count,
                                                         len(employee_todos)))
    for task in tasks_titles:
        print("\t {}".format(task))

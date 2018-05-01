#!/usr/bin/python3
'''
    This module contains a Python script that gathers data from an API.

    Given an employee ID, the script returns information about their
    To-Do list progress.
'''

import csv
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

    csv_file = "{}.csv".format(employee_id)
    with open(csv_file, 'w') as f:
        for todo in employee_todos:
            csv.writer(f, quoting=csv.QUOTE_ALL).writerow(
                [employee_id, employee_name,
                 str(todo['completed']), todo['title']])

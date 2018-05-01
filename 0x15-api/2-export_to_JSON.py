#!/usr/bin/python3
'''
    This module contains a Python script that gathers data from an API.

    Given an employee ID, the script returns information about their
    To-Do list progress.
'''

import csv
import json
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

    todo_list = []
    for todo in employee_todos:
        new_dict = {}
        new_dict['task'] = todo['title']
        new_dict['completed'] = todo['completed']
        new_dict['username'] = employee_name
        todo_list.append(new_dict)
    new_dict = {}
    new_dict[employee_id] = todo_list
    with open("{}.json".format(employee_id), 'w') as f:
        f.write(json.dumps(new_dict))

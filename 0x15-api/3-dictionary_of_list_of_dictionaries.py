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
    url_api = "https://jsonplaceholder.typicode.com"

    url_employees = "{}/users".format(url_api)
    employees = requests.get(url_employees).json()
    url_employee_todos = "{}/todos".format(url_api)
    employee_todos = requests.get(url_employee_todos).json()

    employee_dict = {}
    for employee in employees:
        todo_list = []
        for todo in employee_todos:
            new_dict = {}
            new_dict['task'] = todo['title']
            new_dict['completed'] = todo['completed']
            new_dict['username'] = employee['name']
            todo_list.append(new_dict)
        employee_dict[todo['id']] = todo_list

    with open("todo_all_employees.json", 'w') as f:
        f.write(json.dumps(employee_dict))

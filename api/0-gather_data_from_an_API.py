#!/usr/bin/python3
"""Using this REST API, for a given employee ID, returns information about his/her list progress."""
import json
import requests
from sys import argv
if __name__ == "__main__":

    if len(argv) != 2:
        exit()

    
    employee_id = argv[1]
    request_user = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        )
    request_user_json = json.loads(request_user.text)

    total_user_request = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        )
    total_user_request_json = json.loads(total_user_request.text)

    completed_tasks = []
    total_tasks = len(total_user_request_json)

    for task in total_user_request_json:
        if task["completed"]:
            completed_tasks.append(task["title"])

    num_completed_tasks = len(completed_tasks)

    print(f"Employee {request_user_json['name']} is done with tasks"
          f"({num_completed_tasks}/{total_tasks}):")
    for task_title in completed_tasks:
        print(f"\t {task_title}")

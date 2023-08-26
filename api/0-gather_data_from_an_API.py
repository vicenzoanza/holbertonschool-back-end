#!/usr/bin/python3
import requests
import json
from sys import argv
if __name__ == "__main__":

    if len(argv) == 1:
    
        employee_id = argv[1]
        
        request_user = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        )
        
        request_user_json = json.loads(request_user.text)
        
        total_user_request = requests.get(
            f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        )
        total_user_request_json = json.loads(total_user_request.text)
        finished = 0
        total = 0
        
        for tasks in total_user_request_json:
            if task["completed"]:
                ready += 1
            else:
                not_ready += 1
                
        print (f"Employee {'name'} is done with tasks({ready}/{not_ready + ready})")
        for task in total_user_request_json:
            if task["completed"]:
                print(f'\t {task["title"]}')
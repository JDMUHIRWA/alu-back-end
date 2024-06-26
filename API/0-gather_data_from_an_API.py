#!/usr/bin/python3
"""
A Python script that, using a REST API, api
returns information about an employee's TODO list progress.
"""
if __name__ == "__main__":
    import json
    import sys
    import urllib.request

    # Format the employee ID with the URL
    employee_id = sys.argv[1]
    url1 = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    url2 = f"https://jsonplaceholder.typicode.com/users/{employee_id}/"
    
    # Request TODO list data
    req_object1 = urllib.request.Request(url1, method="GET")
    with urllib.request.urlopen(req_object1) as response_object1:
        response1 = json.load(response_object1)
    
    # Request employee data
    req_object2 = urllib.request.Request(url2, method="GET")
    with urllib.request.urlopen(req_object2) as response_object2:
        response2 = json.load(response_object2)
    
    # Process completed tasks
    completed_tasks = [task for task in response1 if task['completed']]
    no_of_comptasks = len(completed_tasks)
    totalno_of_task = len(response1)
    
    # Get employee name
    employee_name = response2["name"]
    
    # Print the TODO list progress
    print(f"Employee {employee_name} is done with tasks({no_of_comptasks}/{totalno_of_task}):")
    for comp_task in completed_tasks:
        print(f"\t {comp_task['title']}")



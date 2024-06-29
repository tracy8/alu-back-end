#!/usr/bin/python3

'''CSV export'''

import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/" \
        .format(user_id)

    user_info = requests.request('GET', user_url).json()
    todos_info = requests.request('GET', todos_url).json()

    employee_name = user_info["name"]
    task_completed = list(filter(lambda obj:
                                 (obj["completed"] is True), todos_info))
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    with open('{}.csv'.format(user_id), 'w') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [csvwriter.writerow([user_id, user_info["username"],
                             task["completed"], task["title"]])
         for task in todos_info]

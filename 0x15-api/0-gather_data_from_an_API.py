#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com/todo for
a given employee to return info about his/her TODO
list progress
"""


import json
import sys
import urllib.request


if __name__ == "__main__":
    completed_tasks = 0
    uncompleted_tasks = 0
    url = "https://jsonplaceholder.typicode.com/todos"
    req = urllib.request.Request(url)
    user_id = sys.argv[1]
    jobs_done = []
    req_2 = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(user_id)

    with urllib.request.urlopen(req_2) as response:
        character_set = response.headers.get_content_charset()
        body = json.loads(response.read().decode(character_set))
        user_name = body["name"]

    with urllib.request.urlopen(req) as response:
        character_set_2 = response.headers.get_content_charset()
        body_2 = json.loads(response.read().decode(character_set_2))
        for i in body_2:
            if i["userId"] == int(user_id):
                if i["completed"] is True:
                    completed_tasks = completed_tasks + 1
                    jobs_done.append(i["title"])
                else:
                    uncompleted_tasks = uncompleted_tasks + 1

    total_tasks = completed_tasks + uncompleted_tasks
    print("Employee {} is done with tasks({}/{}):". \
        format(user_name, completed_tasks, total_tasks))
    for w in jobs_done:
        print("\t {}".format(w))


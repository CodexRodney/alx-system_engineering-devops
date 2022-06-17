#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com/todo for
all employees to return info about his/her TODO
list progress and Exports the data to a json file
in json format
"""


import json
import urllib.request


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    req = urllib.request.Request(url)
    file_name = "todo_all_employees.json"
    user_dict = {}  # contains usernames with user_id as key
    new_dict_2 = {}  # holds employees info
    new_list = []  # contains dictionaries to load to file_name
    req_2 = "https://jsonplaceholder.typicode.com/users"

    with urllib.request.urlopen(req_2) as response:
        character_set = response.headers.get_content_charset()
        body = json.loads(response.read().decode(character_set))
        for y in range(10):
            user_dict[str(y + 1)] = body[y]["username"]

    with urllib.request.urlopen(req) as response:
        character_set_2 = response.headers.get_content_charset()
        body_2 = json.loads(response.read().decode(character_set_2))
        for z in range(1, 11):
            for i in body_2:
                new_dict = {}
                if i["userId"] == z:
                    new_dict["username"] = user_dict[str(z)]
                    new_dict["completed"] = i["completed"]
                    new_dict["task"] = i["title"]
                    new_list.append(new_dict)
            new_dict_2[str(z)] = new_list
            new_list = []

    with open(file_name, 'w') as jsonfile:
        json.dump(new_dict_2, jsonfile)

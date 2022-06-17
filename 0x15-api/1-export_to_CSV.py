#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com/todo for
a given employee to return info about his/her TODO
list progress and Exports the data to an csv file
in csv format
"""


import csv
import json
import sys
import urllib.request


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos"
    req = urllib.request.Request(url)
    user_id = sys.argv[1]
    file_name = "{}.csv".format(user_id)
    new_list = []  # contains dictionaries to convert to csv
    req_2 = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(user_id)

    with urllib.request.urlopen(req_2) as response:
        character_set = response.headers.get_content_charset()
        body = json.loads(response.read().decode(character_set))
        user_name = body["username"]

    with urllib.request.urlopen(req) as response:
        character_set_2 = response.headers.get_content_charset()
        body_2 = json.loads(response.read().decode(character_set_2))
        for i in body_2:
            new_dict = {}
            if i["userId"] == int(user_id):
                new_dict["userId"] = i["userId"]
                new_dict["username"] = user_name
                new_dict["completed"] = i["completed"]
                new_dict["title"] = i["title"]
                new_list.append(new_dict)

    new_dict_keys = ["userId", "username", "completed", "title"]
    with open(file_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=new_dict_keys,
                                quoting=csv.QUOTE_ALL)
        writer.writerows(new_list)

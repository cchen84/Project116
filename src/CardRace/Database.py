import csv
import json


def allUsers(filename):
    users = []
    with open( filename, newline="") as f:
        for row in csv.reader(f):
            users.append(row[0])
    return users


def add_Users(filename, name):
    x = allUsers(filename)
    new_user = name
    if (new_user not in x):
        with open(filename, "a") as f:
            csv.writer(f).writerow([new_user])
            x.append(new_user)
        return x
    else:
        return x




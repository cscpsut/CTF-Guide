from email import header
import requests
import time
import csv

users_file = "creds_test.csv"
api_token = "e5f0f9b2aa270a9e56d80e067bb6d96a1c4e41d61a5bfaf2b190b6edbb7c8ce5"
request_headers = {
    "Host": "localhost:1234",
    "Authorization": f"Token {api_token}",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Origin": "http://localhost:1234",
    "Referer": "http://localhost:1234/admin/users/new",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
}
url = "http://localhost:1234/"

with open(users_file) as csv_file:
    users = csv.reader(csv_file, delimiter=",")

    proxy = {"http": "127.0.0.1:8080"}
    for entry in users:
        name = entry[0]
        email = entry[1]
        passwd = entry[2]

        request_data = {
            "name": name,
            "email": email,
            "password": passwd,
            "type": "user",
            "verified": False,
            "hidden": False,
            "banned": False,
            "fields": [],
        }
        r = requests.post(
            f"{url}api/v1/users?notify=false",
            headers=request_headers,
            json=request_data,
        )
        if r.status_code != 200:
            print(r.content)
            print(request_data)
        time.sleep(1)
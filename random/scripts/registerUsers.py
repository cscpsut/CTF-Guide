import requests
import time

users_file = "creds_test.csv"

entry = "test,test@test.com,12334"
api_token = "6477ff7506776bccf9a37fc1d5ecf078562ba3ba1f0f5c741db978532f0e8a93"

request_headers = {
    "Authorization": f"Token {api_token}",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
}
proxy = {"http": "127.0.0.1:8080"}


name = entry.split(",")[0]
email = entry.split(",")[1]
passwd = entry.split(",")[2]

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
requests.get("https://cda9-176-29-43-49.eu.ngrok.io",proxies=proxy,verify=False)
time.sleep(0.5)

import string
import os
import csv
from passlib.hash import bcrypt_sha256

input_file = "CSCCTF v4.csv"
email_csv = open("email.csv", "w")
sql_csv = open("sql.csv", "w")


characterset = (
    string.ascii_letters + string.digits + string.punctuation.replace(",", "").replace('"',"")
)

line_count = 0
with open(input_file) as csv_file:
    input = csv.reader(csv_file, delimiter=",")
    for entry in input:
        if line_count == 0:
            line_count += 1
            continue
        password = ""
        random = os.urandom(20)
        for char in random:
            password = password + characterset[char % len(characterset)]
        hash = bcrypt_sha256.hash(str(password))
        sql_csv.write(
            f'"{1000+line_count}",\\N,"{entry[1]}","{hash}","{entry[5]}","user",\\N,\\N,\\N,\\N,\\N,"0","0","0",\\N,"2022-08-27 10:13:18"\n'
        )

        email_csv.write(f"{entry[1]},{entry[5]},{password}\n")

        line_count += 1
print(f"Processed {line_count - 1} lines.")

This is script is used to generate a password for each team. The output of the Generate_csv.py script are 2 csv files, email.csv which contains the name, password and email for the team leader for each team. sql.csv is used to add users directly into the ctfd mysql database using the following commands.


`SET SESSION SQL_MODE='ALLOW_INVALID_DATES'`<br>
`LOAD DATA LOCAL INFILE 'sql.csv' INTO TABLE users FIELDS TERMINATED BY ','  ENCLOSED BY '"' LINES TERMINATED BY '\n'`


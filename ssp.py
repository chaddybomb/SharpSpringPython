#https://github.com/chaddybomb/SharpSpringPython

###############################################
############# Begin Configuration #############
###############################################

# The accountID and secretKey can be found in your SharpSpring API settings.

accountID = ""
secretKey = ""

# Comma-separated list of e-mail addresses to grab lead data for.

email_addresses = ""

###############################################
############# End Configuration ###############
###############################################

import requests, json, string, random, pandas as pd

def rand_id_gen(size=36, chars=string.ascii_uppercase + string.digits):
	#uses string and random modules to create a random 36 char generated ID for the request
	return ''.join(random.choice(chars) for _ in range(size))

email_list = email_addresses.split(",") #create list object

for email in email_list: #run through each e-mail in the list

	#using the getLeads method via the SharpSpring Open API:
	#https://help.sharpspring.com/hc/en-us/sections/115000320047-API

	url = f"https://api.sharpspring.com/pubapi/v1/?accountID={accountID}&secretKey={secretKey}"
	payload = '''{
	"method": "getLeads",
	"params": {
			"where": {
				"emailAddress": "''' + email.strip() + '''"
			}
		},
	"id": "''' + rand_id_gen() + '''"
	}'''

	headers = {'Content-Type': 'text/plain'} #nothing special
	response = requests.request("POST", url, headers=headers, data=payload) #post the payload
	info = json.loads(response.text) #load the response with the json module
	df = pd.json_normalize(info['result']['lead']) #convert json data into a flat table with pandas

	#if this is the first email in the loop, create the file and add the header
	#otherwise, just add a new line
	if email == email_list[0]:
		df.to_csv("data.csv", index=False)
	else:
		df.to_csv("data.csv", mode='a', header=False, index=False)
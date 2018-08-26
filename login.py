import json
import requests

apic = '10.203.254.24'
user = 'admin'
passw = 'lumos123'

#print(apic, user, passw)



def login_apic(apic, user, passw):

	body = {
	  "aaaUser":{
	    "attributes":{
	      "name":"admin",
	      "pwd":"lumos123"
	    }
	  }
	}

	login = requests.post('https://{0}/api/aaaLogin.json' .format(apic),
		data = json.dumps(body), verify=False)

	status = login.status_code

	print(status)

login_apic(apic, user, passw)
# from stackoverflow
import sys
import os

def check_ping():
	for ip in range(1,256):
		hostname = "192.168.1."+ str(ip)
	#hostname = "192.168.1.1"
    
        response = os.system("ping -c 1 " + hostname)
    # and then check the response...
        if response == 0:
        	pingstatus = "Network Active"
    	else:
        	pingstatus = "Network Error"

	#print(response, pingstatus)

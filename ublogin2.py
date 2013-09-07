#!/usr/bin/env python
import getopt,sys
try:
	import requests
except ImportError:
	print "python-requests needs to be instaled"
	sys.exit()
else:
	pass
cookiesairos=''


def airosauth(ipdata,usernamedata,passdata):
	#Query for session and executes the auth request to the web server
	r=requests.get('http://'+ipdata+'/login.cgi')
	#We try to obtain a session to be authenticated
	try:
		global cookiesairos
		cookiesairos=dict(AIROS_SESSIONID=''+str(r.cookies['AIROS_SESSIONID'])+'')
	except not cookiesairos:
		print "Could not obtaing any AIROS session. Is the webserver ip in the device?"
	#Construct the data ot be sended
	authdata={'uri': '/', 'username': ''+usernamedata+'','password':''+passdata+''}
	authformfile={'file': ('form.txt', open('form.txt', 'rb'))}
	#Make the request, sending the cookies, data for auth, and form to do it well
	a=requests.post('http://'+ipdata+'/login.cgi', cookies=cookiesairos, data=authdata, files=authformfile)
	#Return status code of the web request
	return

def datareq(ipdata):
	b=requests.get('http://'+ipdata+'/iflist.cgi',cookies=cookiesairos)
	print b.text

def main(argv):
	ip=''
	username=''
	password=''
	sec=''
	try:
		opts, args = getopt.getopt(argv,"hi:u:p:s:d:")
	except getopt.GetoptError:
		print "Options are not recognized: -i ip/hostname -u user -p password -s ssl -d [channel|freq|ccq]"
	for opt, arg in opts:
		if opt == '-h':
			print "Options are not recognized: -i ip/hostname -u user -p password -s [ssl|off] -d [channel|freq|ccq]"
			sys.exit()
		elif opt in ("-i"):
			ip = arg
		elif opt in ("-u"):
			username = arg
		elif opt in ("-p"):
			password = arg
		elif opt in ("-s"):
			sec = arg
	airosauth(ip,username,password)
	datareq(ip)

if __name__ == "__main__":
	   main(sys.argv[1:])

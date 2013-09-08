#!/usr/bin/env python
import getopt,sys,re
import StringIO

try:
	import requests
except ImportError:
	print "python-requests needs to be instaled"
	sys.exit()
else:
	pass

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
	if debug=="on":
		print "===="
		print "Output of \"a\" object"
		print "--"
		print a
		print "--"
		print a.text
		print "===="
	return

def datareq(ipdata):
	#Do the request of the cgi scripts that retrieves the data
	global b
	b=requests.get('http://'+ipdata+'/iflist.cgi',cookies=cookiesairos)
        if debug=="on":
                print "===="
                print "Output of \"b\" object"
                print "--"
                print b
                print "--"
                print b.text
                print "===="
        return

def filterdata(req):
	#Filter the neccesary data and clean it
	buf = StringIO.StringIO(b.text)
	arr=[]
	for line in buf:
		if re.match(r'^\s*$', line):
			pass
		else:
			arr.append(line.rstrip('\n'))
	for i in arr:
		if str("\""+req+"\"") in i:
			output=i.rstrip('\,').strip().strip(':')
			of=re.sub("\""+req+"\": ",'',output)
			if "MHz" in of:
				of=re.sub(" MHz\"",'',of).strip("\"")
			print str(of)

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"hi:u:p:s:d:v")
	except getopt.GetoptError:
		print "Options are not recognized: -i ip/hostname -u user -p password -s ssl -d [channel|freq|ccq]"
	for opt, arg in opts:
		if opt == '-h':
			print "Options are not recognized: -i ip/hostname -u user -p password -s [ssl|off] -d [channel|frequency|ccq]"
			sys.exit()
		elif opt in ("-i"):
			ip = arg
		elif opt in ("-u"):
			username = arg
		elif opt in ("-p"):
			password = arg
		elif opt in ("-s"):
			sec = arg
		elif opt in ("-d"):
			info = arg
	#Control de verbose mode
	if "-v" in str(opts):
		global debug
		debug="on"
		print "Debugdata:"+debug+""
		print opts
	else:
		debug="off"
	#Execute the 3 functions of the script...
	airosauth(ip,username,password)
	datareq(ip)
	filterdata(info)

if __name__ == "__main__":
	main(sys.argv[1:])

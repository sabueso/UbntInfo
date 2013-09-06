#!/usr/bin/env python

import requests
import pprint as pp
import sys


r= requests.get('http://'+str(sys.argv[1])+'/login.cgi')

print "Status de peticion inicial:"+str(r.status_code)+""
print "===================================================================="
cookiesairos=dict(AIROS_SESSIONID=''+str(r.cookies['AIROS_SESSIONID'])+'')
print cookiesairos

print "===================================================================="
datos = {'uri': '/', 'username': ''+sys.argv[2]+'','password':''+sys.argv[3]+''}
#Encontrado en https://github.com/shazow/urllib3/issues/111
ficheros = {'file': ('form.txt', open('form.txt', 'rb'))}
a = requests.post('http://192.168.1.20/login.cgi', cookies=cookiesairos, data=datos, files=ficheros)
print "Status de autentificacion:"+str(a.status_code)+""
print "===================================================================="
b= requests.get('http://192.168.1.20/iflist.cgi',cookies=cookiesairos)
print "Salida final"
print b.text

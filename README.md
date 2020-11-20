# byp4xx.sh
Simple bash script to bypass "403 Forbidden" messages with well-known methods discussed in #bugbountytips

Usage:
./byp4xx.sh http(s)://url /path

Use http or https. Start your path with /

Example:
./byp4xx.sh https://www.google.es /test

Features:
- Multiple HTTP verbs/methods
- Multiple ways mentioned in #bugbountytips
- Multiple headers: Referer, X-Custom-IP-Authorization...

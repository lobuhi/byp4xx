
```
    __                __ __           
   / /_  __  ______  / // / _  ___  __
  / __ \/ / / / __ \/ // /_| |/_/ |/_/
 / /_/ / /_/ / /_/ /__  __/>  <_>  <  
/_.___/\__, / .___/  /_/ /_/|_/_/|_|  
      /____/_/                        
```
40X bypasser in Go. Methods from #bugbountytips, headers, verb tampering, user agents and more.

**Usage:** 
```
byp4xx <cURL or byp4xx options> <URL or file>

Some cURL options you may use as example:
  -L follow redirections (30X responses)
  -x <ip>:<port> to set a proxy
  -m <seconds> to set a timeout
  -H for new headers. Escape double quotes.
  -d for data in the POST requests body
  -...
  
 Built-in options:
  --all Verbose mode (by default only 2xx and 3xx codes will be prompted)
  -t or --thread Set the maximum threads. Rate limit disabled when threads are enabled. Use carefully.
  --rate Set the maximum reqs/sec. Only one thread enforced, for low rate limits. (5 reqs/sec by default)
  -xV Exclude verb tampering
  -xH Exclude headers
  -xUA Exclude User-Agents
  -xX Exclude extensions
  -xD Exclude default creds
  -xS Exclude CaSe SeNsiTiVe
  -xM Exclude middle paths
  -xE Exclude end paths
  -xB Exclude #bugbountytips
```
**Examples:**

Regular usage:
```
byp4xx http://localhost/test
```

Avoid default creds if the response is not 401:
```
byp4xx -xD http://localhost/test
```

Avoid end paths and extensions if the url ends with /:
```
byp4xx -xE -xX http://localhost/test
```

Set 2 seconds timeout, follow redirections and use proxy
```
byp4xx -m 2 -L -x 127.0.0.1:8080 http://localhost/test
```

Custom headers, you should escape double quotes:
```
byp4xx -H \"Authorization: Bearer <JWT>\" http://localhost/test
```

**Features:**
- Multiple HTTP verbs/methods
- Multiple methods mentioned in #bugbountytips
- Multiple headers: Referer, X-Custom-IP-Authorization...
- Accepts any cURL option
- Based on Seclist
    -  UserAgents
    -  Extensions
    -  Default credentials

**[Buy me a coffee... or a pizza! Stay cool! ^_^](https://buymeacoffee.com/lobuhi)**

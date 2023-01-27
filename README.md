
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
  -t or --thread Set the maximum threads. Rate limit disabled when threads are enabled.
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
**Example:**
```
byp4xx http://localhost/test
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

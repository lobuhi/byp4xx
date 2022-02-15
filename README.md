***byp4xx.py***
```
    __                __ __           
   / /_  __  ______  / // / _  ___  __
  / __ \/ / / / __ \/ // /_| |/_/ |/_/
 / /_/ / /_/ / /_/ /__  __/>  <_>  <  
/_.___/\__, / .___/  /_/ /_/|_/_/|_|  
      /____/_/                        
```
Python script for 40X responses bypassing. Methods from #bugbountytips, headers, verb tampering and user agents.

**Installation:**
```
pip install git+https://github.com/lobuhi/byp4xx.git
```

**Usage:** Start URL with http or https.
```
python3 byp4xx.py <cURL options> <target>

Some cURL options you may use as example:
  -L follow redirections (30X responses)
  -x <ip>:<port> to set a proxy
  -m <seconds> to set a timeout
  -H for new headers
  -d for data in the POST requests body
  -...
```
**Example:**
```
python3 byp4xx.py https://www.google.es/test
```
**Features:**
- Multiple HTTP verbs/methods
- Multiple methods mentioned in #bugbountytips
- Multiple headers: Referer, X-Custom-IP-Authorization...
- Accepts any cURL option
- New module, test for 2454 UserAgents from SecList

**Tips:**
- You can add proxychains to use with BurpSuite
- Interlace is a good option for multithreading multiples URLs
- BONUS: **[Buy me a coffee... or a pizza! Stay cool! ^_^](https://buymeacoffee.com/lobuhi)**

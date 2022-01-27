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
git clone https://github.com/lobuhi/byp4xx.git
cd byp4xx
chmod u+x byp4xx.py
./byp4xx.py
or
python3 byp4xx.py
```

**Usage:** Start URL with http or https.
```
usage: byp4xx.py [-h] --target TARGET [--curl-options CURL_OPTIONS] [--bypass-ip BYPASS_IP]
                 [--fuzz-user-agents | --skip-fuzz-user-agents]

optional arguments:
  -h, --help            show this help message and exit
  --curl-options CURL_OPTIONS
                        Any additional options to pass to curl
  --bypass-ip BYPASS_IP
                        Try bypass tests with a specific IP address (or hostname). i.e.:
                        "X-Forwarded-For: 192.168.0.1" instead of "X-Forwarded-For: 127.0.0.1"
  --fuzz-user-agents    Skip question and fuzz user agents with UserAgents.fuzz.txt from SecList or
                        not.
  --skip-fuzz-user-agents
                        Skip question and not fuzz User-Agent header.

required named arguments:
  --target TARGET       The url target of the tests
```

```
Some cURL options you may use as example:
  -L follow redirections (30X responses)
  -x <ip>:<port> to set a proxy
  -m <seconds> to set a timeout
  -H for new headers (-H "Cookie: test=value;")
  -d for data in the POST requests body
  -...
```
**Example:**
```
python3 byp4xx.py --target https://www.google.es/test
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

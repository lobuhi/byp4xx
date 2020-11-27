***byp4xx.sh***
```
    __                __ __           
   / /_  __  ______  / // / _  ___  __
  / __ \/ / / / __ \/ // /_| |/_/ |/_/
 / /_/ / /_/ / /_/ /__  __/>  <_>  <  
/_.___/\__, / .___/  /_/ /_/|_/_/|_|  
      /____/_/                        
```
A bash script to bypass "403 Forbidden" responses with well-known methods discussed in #bugbountytips

**Installation:**
```
git clone https://github.com/lobuhi/byp4xx.git
cd byp4xx
chmod u+x byp4xx.sh
```

**Usage:** Start URL with http or https.
```
./byp4xx.sh [OPTIONS] http(s)://url/path

OPTIONS:
  -c Return the entire curl command if response is 200
  -r Redirects if the response is 3XX
```
**Example:**
```
./byp4xx.sh https://www.google.es/test
```
**Features:**
- Multiple HTTP verbs/methods
- Multiple methods mentioned in #bugbountytips
- Multiple headers: Referer, X-Custom-IP-Authorization...
- Allow redirects
- Return the entire curl command if response is 200

**Tips:**
- You can add proxychains to use with BurpSuite
- Interlace is a good option for multithreading multiples URLs
- BONUS: **[Buy me a coffee... or a pizza! Stay cool! ^_^](https://buymeacoffee.com/lobuhi)**

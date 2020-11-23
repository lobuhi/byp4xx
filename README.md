# byp4xx.sh
Simple bash script to bypass "403 Forbidden" messages with well-known methods discussed in #bugbountytips

**Installation:**

git clone https://github.com/lobuhi/byp4xx.git

cd byp4xx

chmod u+x byp4xx.sh

**Usage:** Start URL with http or https.

./byp4xx.sh http(s)://url/path

**Example:**

./byp4xx.sh https://www.google.es/test

**Features:**

- Multiple HTTP verbs/methods
- Multiple methods mentioned in #bugbountytips
- Multiple headers: Referer, X-Custom-IP-Authorization...

**Tips:**

- You can add proxychains to use with BurpSuite
- Interlace is a good option for multithreading multiples URLs


![alt text](screenshot.png)

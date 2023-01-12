#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

# Replace the URL with the target server's URL
login_url = 'http://example.com/owa/auth.owa'
send_url = 'http://example.com/owa/compose.owa'

# Replace with your own credentials
username = 'your_username'
password = 'your_password'

# The details of the email you want to send
to_email = 'recipient@example.com'
subject = 'Testing OWA login and send email'
body = 'This is a test email sent through OWA'

session = requests.Session()

# Login to OWA
login_data = {'destination': 'https://example.com/owa/',
              'flags': '4',
              'forcedownlevel': '0',
              'username': username,
              'password': password,
              'isUtf8': '1'}

login_response = session.post(login_url, data=login_data)

# Check if login was successful
soup = BeautifulSoup(login_response.text, 'html.parser')
if soup.find('title').text != 'Outlook':
    print('Login failed')
    exit()

# Prepare the data for sending email
send_data = {'__EVENTTARGET': '',
             '__EVENTARGUMENT': '',
             '__VIEWSTATE': soup.find('input', {'name': '__VIEWSTATE'})['value'],
             '__VIEWSTATEGENERATOR': soup.find('input', {'name': '__VIEWSTATEGENERATOR'})['value'],
             '__EVENTVALIDATION': soup.find('input', {'name': '__EVENTVALIDATION'})['value'],
             'txtTo': to_email,
             'txtSubject': subject,
             'txtBody': body,
             'btnSend': 'Send'}

# Send the email
send_response = session.post(send_url, data=send_data)

# Check if the email was sent successfully
soup = BeautifulSoup(send_response.text, 'html.parser')
if soup.find('span', {'class': 'Error'}):
    print('Failed to send email')
else:
    print('Email sent successfully')

#!/usr/bin/python

from exchangelib import Credentials, Account, Configuration, DELEGATE
from exchangelib.errors import UnauthorizedError

def send_mail:

    # Set credentials for logging into Exchange Server
    creds = Credentials(
        username='username',
        password='password'
    )

    # Set account configuration
    config = Configuration(server='autodiscover', credentials=creds)

    # Connect to account
    try:
        account = Account(primary_smtp_address='email@domain.com', config=config, autodiscover=True, access_type=DELEGATE)
    except UnauthorizedError:
        print("Invalid credentials")
        exit()

    # Set recipients and attachment
    recipients = ['recipient1@example.com', 'recipient2@example.com', 'recipient3@example.com']
    attachment = 'file.txt'

    # Loop through recipients
    for recipient in recipients:
        # Create message
        message = account.new_message(
            subject='Test Email',
            body='This is a test email',
            to_recipients=[recipient]
        )

        # Add attachment
        message.attach(attachment)

        # Send email
        message.send()

    print("Emails sent successfully")

import smtplib  # It's an in-built module.
from email.message import EmailMessage

# The Simple Mail Transfer Protocol (SMTP) is an internet standard communication protocol for electronic mail
# transmission. Mail servers and other message transfer agents use SMTP to send and receive mail messages. User-level
# email clients typically use SMTP only for sending messages to a mail server for relaying, and typically submit
# outgoing email to the mail server on port 587 or 465 per RFC 8314. For retrieving messages, IMAP (which replaced
# the older POP3) is standard, but proprietary servers also often implement proprietary protocols, e.g.,
# Exchange ActiveSync.

# Since SMTP's introduction in 1981, it has been updated, modified and extended multiple times. The protocol version
# in common use today has extensible structure with various extensions for authentication, encryption, binary data
# transfer, and internationalized email addresses. SMTP servers commonly use the Transmission Control Protocol on
# port number 25 (for plaintext) and 587 (for encrypted communications).

email = EmailMessage()
email['from'] = 'Wasif Nadeem'
email['to'] = 'wasifnadeem1573@gmail.com'
email['subject'] = 'You are going to be killed tonight...'

email.set_content('I am a Python Master, BEWARE OF ME 👿')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # To initialize the server
    smtp.starttls()  # tls is an encryption mechanism, to connect securely to sever.
    smtp.login('wasif1607@gmail.com', '9871598177ray')  # email and password of sender
    smtp.send_message(email)
    print('all good boss!')

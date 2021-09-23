import smtplib  # It's an in-built module.
from email.message import EmailMessage
from string import Template  # with Template we can substitute dollar signed variable.
from pathlib import Path

html = Template(Path('index.html').read_text())  # To access html content.
email = EmailMessage()
email['from'] = 'Wasif Nadeem'
email['to'] = 'wasifnadeem1573@gmail.com'
email['subject'] = 'You just won 100,000,000 dollars!'

email.set_content(html.substitute({'name': 'Tintin', 'age': 100}), 'html')  # last html is necessary to make sure
# it read content of html file, if we miss it, python will simply send the whole html. We replaced name and age,
# as it had a $ sign
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()  # To initialize the server
    smtp.starttls()  # tls is an encryption mechanism, to connect securely to sever.
    smtp.login('wasif1607@gmail.com', '9871598177ray')  # email and password of sender
    smtp.send_message(email)
    print('all good boss!')

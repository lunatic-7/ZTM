from twilio.rest import Client

account_sid = 'AC1e0b463*******************'
auth_token = 'a97c0523ec0b**************'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+141******',
    body='Hello! This is an editable text message. You are free to change it and write whatever you like.',
    to='whatsapp:+9199********'
)

print(message.sid)

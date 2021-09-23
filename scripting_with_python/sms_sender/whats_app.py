from twilio.rest import Client

account_sid = 'AC1e0b46365218f59dbcfcf64bcb771d90'
auth_token = 'a97c0523ec0bc7497b30aff62eb8b052'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='whatsapp:+14155238886',
    body='Hello! This is an editable text message. You are free to change it and write whatever you like.',
    to='whatsapp:+919991800768'
)

print(message.sid)

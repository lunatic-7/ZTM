# I am using an API called Twilio for this:

from twilio.rest import Client

account_sid = 'AC1e0b46*************'
auth_token = 'a97c0523ec0bc************'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG10e87d****************8',
    body="Hi, Mohammd Nadeem. I am really dissapointed to tell you that,"
         " Your son Saqib Nadeem has been expelled from Learner's Paradise"
         " Public School, Due to indulgence in fighting cause along with his 4"
         " friends, For any further information, Kindly visit school on 19/sept.",
    to='+91*******'
)

print(message.sid)

# Copied the upper code from Twilio.

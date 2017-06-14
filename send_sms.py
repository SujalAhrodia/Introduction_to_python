from twilio.rest import Client

def send(account_sid,auth_token,iterations):

    client = Client(account_sid, auth_token)

    for i in range (0,length)
        message = client.messages.create(
            to="+XXXXXXXXXXXX", #verified number
            from_="+15XXXXXXXXX", #twilio number
            body="HI! I love Opensource")

        print(message.sid)

#twilio ID
account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# twilio auth token
auth_token  = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
send(account_sid,auth_token,10)

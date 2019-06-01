"""


ACCOUNT SID = AC3a926559aed1eb7ee925e900af71b5f6
AUTH TOKEN = 9165a7732b4921b84be31073796db365

Your first Twilio Phone Number
(786) 789-3458

Your new Phone Number is +17867893458

"""
from twilio.rest import Client #导包
# account_sid = 'ACc36bf50712a28f0ac74948531d1786d'
account_sid = 'AC3a926559aed1eb7ee925e900af71b5f6'
# auth_token = 'd97b85844f9d6a8762f916bdad4c903'
auth_token = '9165a7732b4921b84be31073796db365'
client = Client(account_sid, auth_token)
message = client.messages.create(
        from_='17867893458',
        body='测试发送短信',
        # to='+8618106534015'
        to='+8618252583182'
        )
print(message.sid)


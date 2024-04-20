from __future__ import print_function
import clicksend_client
from clicksend_client import SmsMessage
from clicksend_client.rest import ApiException


def send_sms(phone: str, msg: str):

    # Configure HTTP basic authorization: BasicAuth
    configuration = clicksend_client.Configuration()
    configuration.username = 'dablandonr'
    configuration.password = '78142A04-6798-1FAE-6AB8-E7D71099DC02'

    # Create an instance of the API class
    api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))

    # Configure your message
    sms_message = SmsMessage(
        source="JUAN MARIA CESPEDES",  # Replace this with your desired source name
        body=msg,
        to="+57" + phone # Enter the number you are sending to
    )

    sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])

    try:
        # Send an SMS message(s)
        api_response = api_instance.sms_send_post(sms_messages)
        return "Mensaje enviado correctamente"
    except ApiException as e:
        return "Exception when calling SMSApi->sms_send_post: %s\n" % e

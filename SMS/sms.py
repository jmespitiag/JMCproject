from sms_api.altiria_client import *


def send_sms(phone: str, msg: str):

    try:
        client = AltiriaClient('davidblandon.roman@gmail.com', 'pbdu3x7f')
        textMessage = AltiriaModelTextMessage(phone, msg)
        jsonText = client.sendSms(textMessage)
        return '¡Mensaje enviado!'
    except AltiriaGwException as ae:
        return 'Mensaje no aceptado:'+ae.message+ae.status
    except JsonException as je:
        return 'Error en la petición:'+je.message
    except ConnectionException as ce:
        if "RESPONSE_TIMEOUT" in ce.message: 
            return 'Tiempo de respuesta agotado:'+ce.message
        else:
            return 'Tiempo de conexión agotado:'+ce.message
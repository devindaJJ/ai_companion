from flask import request, abort
from twilio.twiml.messaging_response import MessagingResponse
from controllers.message_controller import MessageController

controller = MessageController()

def handle_whatsapp():
    if request.method != "POST":
        abort(403)
    incoming_msg = request.form.get("Body")
    if not incoming_msg:
        abort(403)

    reply = controller.handle_message(incoming_msg)

    resp = MessagingResponse()
    resp.message(reply)
    return str(resp)

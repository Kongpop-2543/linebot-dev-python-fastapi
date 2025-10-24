from linebot.v3.messaging import TextMessage

def response_message(event):
    #print(event)
    event_message = event.message.text
    if event_message.lower() == "hello":
        reply_message = "Hello from Dev Environment from response_message.py"
        print(reply_message + "print in function")
        return TextMessage(type = "text", text = reply_message)
    else:
        return None
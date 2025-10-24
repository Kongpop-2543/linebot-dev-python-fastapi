from linebot.v3.messaging import TextMessage

def response_message(event):
    print(event)
    reply_message = "Hello from Dev Environment from response_message.py"
    print(reply_message + "print in function")
    return TextMessage(text = reply_message)
import fbchat
from fbchat.models import *
from fbchat import Client
from secrets import user_id, password, thread

def sendPlaylist(user_id, password, thread, text):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    client= Client(user_id,password,user_agent=user_agent)
    message_id = client.send(Message(text= text),  thread_id= thread, thread_type=ThreadType.GROUP)
    return message_id

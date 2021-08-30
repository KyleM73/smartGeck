# Write your code here :-)
import sys
import os
import fbchat
from fbchat.models import *

def send_msg(msg_txt='Hello World!'):
    sender_username = 'smartGeck@gmail.com'
    sender_password = '7373seal'
    client = fbchat.Client(sender_username, sender_password)
    threadID = '100002722233322'
    threadTYPE = ThreadType.USER
    if not isinstance(msg_txt,str):
        try:
            msg_txt = str(msg_txt)
        except:
            msg_txt = 'String Formatting Error, Check Logs'
    msg = Message(text=msg_txt)
    sent = client.send(msg,thread_id=threadID,thread_type=threadTYPE)
    client.logout()
    
def send_img(img_path):
    if not isinstance(img_path,str) or not os.path.exists(img_path):
        send_msg('img_path Error, Check Logs')
    elif os.path.exists(img_path):
        sender_username = 'smartGeck@gmail.com'
        sender_password = '7373seal'
        client = fbchat.Client(sender_username, sender_password)
        threadID = '100002722233322'
        threadTYPE = ThreadType.USER
        client.sendLocalImage(img_path,message=Message(text='Daily Logs'),thread_id=threadID,thread_type=threadTYPE)
        client.logout()
        
    
    
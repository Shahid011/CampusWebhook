from campus.app import Wrapper
import os
from dotenv import load_dotenv
import time
import threading
import requests

"""
Load Campus's Login Details From .env

"""
load_dotenv()
username = os.environ.get('username_campus')
password = os.environ.get('password_campus')
webhook_url = os.environ.get('webhook_url')


campus = Wrapper()
coks=campus.login(username,password)

"""
    Simple Function to read/write ID in .ID file

"""
def read_write_id(mode,data=None):
    if ".ID" not in os.listdir():
        with open(".ID","w") as f:
            f.write("0")
    if mode == "r":
        with open(".ID","r") as f:
            data = f.read()
        return data
    with open(".ID","w") as f:
        f.write(data)
    return data



"""
    Function to send webHook to Discord

"""
def sendWebHook(notice):
    message_author = notice["postedBy"]
    message_to_send = {
    "content": None,
    "embeds": [
        {
        "title": notice["noticeTitle"],
        "description": notice["noticeContent"],
        "color": 5814783,
        "author": {
            "name": f"{message_author['firstname']} {message_author['lastname']}"
        },
        "footer": {
            "text": f"Notice Created at : {notice['createdAt']}\nWebhook Source Code :  https://github.com/dineshtiwari69/"
        }
        }
    ]
    }
    try:
        requests.post(webhook_url,json=message_to_send)
    except Exception as e:
        pass



def event_handler(function):
    while True:
        init_ID = read_write_id("r")
        time.sleep(1)
        try:
            notices=(campus.notices()["notices"])[0]
        except Exception:
            campus.login(username,password)
            notices=(campus.notices()["notices"])[0]
        new_ID = notices["_id"]
        if new_ID != init_ID:
            read_write_id("w",new_ID)
            init_ID = new_ID
            function(notices)
    

def on_new_notification(function):

    threading.Thread(target=event_handler,args=(function,),daemon=True).start()



on_new_notification(sendWebHook)

while 1:
    pass

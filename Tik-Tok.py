import os
os.system('pip install pywebio')
os.system('pip install TikTok-dl')
from pywebio.output import *
from pywebio.input import *
from pywebio import start_server,config
from pywebio.pin import *
from pywebio.session import *
from TikTok import TikTok_dl as TK
@config(theme="dark")
def App():
 popup("Contact",put_link('InstaGram','https://instagram.com/a3bs9',new_window=True))
 put_html("<h3>TikTok Downloader</h3>")
 url=input('Video URL')
 nurl=(TK(url).nowatermark)
# wurl=(TK(url).watermark)
# aurl=(TK(url).audio)
 put_button("Download", onclick=lambda: put_link('Click here | اضغط هنا ',nurl,new_window= True))
start_server(App, port=8193, debug=True)

from random import *
from uuid import uuid4
uid = uuid4()
from threading import Thread
from user_agent import generate_user_agent
import flask
from flask import jsonify
import requests
from uuid import uuid4
import random
from flask import *
app=Flask(__name__)
@app.route("/Kaero7/API/")
def Home():
        username = request.args.get('email')
        url='https://i.instagram.com/api/v1/accounts/login/'
        headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
        data = {'uuid':uid,  'password':'@gdo00bot',
              'username':username,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
        
        req= requests.post(url, headers=headers, data=data).json()
        if req['message'] == 'The password you entered is incorrect. Please try again.' or req['message'] == 'The password you entered is incorrect. Please try again or log in with Facebook.':
            return jsonify(Login="True",email=username,Dev="@Kaero7") 
        else:
            return jsonify(Login="False",email=username,Dev="@Kaero7")


app.run(port=2022)

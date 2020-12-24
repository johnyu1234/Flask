from flask import Flask, render_template, request, redirect, url_for,session,make_response
import os
from cv2 import cv2
from PIL import Image
import uuid
import numpy as np
import base64


app = Flask(__name__)
app.secret_key = b'sdsdssdsdc]/'

app.config["IMAGE_UPLOADS"] = r"C:\Users\johny\OneDrive\Desktop\Work\Flask\Flask"
#@app.route('/wrong',methods=['POST','GET'])
#def wrong():
#    if request.method == "POST":
#            return render_template('interface.html')
#    else:
#        return render_template("wrong.html")
@app.route('/')
def login_portal():
        user_id = request.cookies.get('userID')
        if user_id:
            print(user_id)

            return render_template("interface.html")
        else:
            return render_template("login.html")
        
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        resp = make_response(render_template('interface.html'))
        resp.set_cookie('userID', user)
        return resp
@app.route('/upload', methods=['POST','GET'])
def upload_file():
    if request.method == "POST":
        if request.files:
            image = []
            
            image.append(request.files["image0"])
            image.append(request.files["image1"])
            image.append(request.files["image2"])
            location = request.form["location"]
            field = request.form["field"]
            pond  = request.form["pond"]
            #file_1=open("location.txt","a")
            #file_1.write(image_0.filename+" "+image_1.filename+" "+image_2.filename+" "+location+" "+field+" "+" "+pond)
            #file_1.write("\n")
            #file_1.close()
            img_cv2 = []
            for img in image:
                npimg = np.fromfile(img,np.uint8)
                img_cv2.append(cv2.imdecode(npimg,cv2.IMREAD_COLOR))
            print(image)
            return redirect(request.url)
    else:
        return render_template("interface.html")


app.run(host='0.0.0.0',port=5000)
#http://127.0.0.1:5000/
from flask import Flask, render_template, request, redirect, url_for,session,make_response
import os
from PIL import Image
import uuid

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
            image = request.files["image_file"]
            location = request.form["location"]
            field = request.form["field"]
            pond  = request.form["pond"]
            file_1=open("location.txt","a")
            file_1.write(image.filename+" "+location+" "+field+" "+" "+pond)
            file_1.write("\n")
            file_1.close()
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))                                          
            if image.filename.find("png")==-1:
                print("converting to png file ")
                convert = Image.open(image.filename)
                convert.save(image.filename[:-3]+'png')
                os.remove(app.config["IMAGE_UPLOADS"] +"\\"+ image.filename)
                return redirect(request.url)
    else:
        return render_template("interface.html")


app.run(host='0.0.0.0',port=5000)
#http://127.0.0.1:5000/
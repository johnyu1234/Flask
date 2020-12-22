# Flask

This is a python program that uses flask as the backend.


To test run the code 
```
python app.py
#insert #http://127.0.0.1:5000/ for local testing
#insert ##http://(IPV4):5000/ for mobile testing 
```
You have to set where does the images go 
```
# do change this to the proper directory
app.config["IMAGE_UPLOADS"] = r"C:\Users\johny\OneDrive\Desktop\Work\Flask\Flask"
```
# interface
*  has a 3 dropdown box and 3 image file selector 
*  images that aren't in png will be converted 
*  files are converted into maximum of (1000,1000) pixels while maintaining aspect ratio


![alt text](https://github.com/johnyu1234/Flask/blob/main/location.jpg?raw=true)


# login
uses cookie to allow old  user to quickly jump to interface without login in 

![alt_text](https://github.com/johnyu1234/Flask/blob/main/login.jpg?raw=true)

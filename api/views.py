from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
from PIL import Image
import time
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.
def index(request):
    returnpage = render(request,"api/index.html")
    returnpage["Access-Control-Allow-Origin"] = "*"
    return returnpage

def post(request):
    username = request.POST["username"]
    fileobj = request.FILES["fileinput"]
    data = fileobj.read()
    if "image" not in fileobj.content_type :
        return HttpResponse('{"status":500,"error":"Image type not recogonsied"}',content_type="application/json",status=500)
    if (not os.path.isdir(ROOT_DIR+"/images/"+username)):
        os.mkdir(ROOT_DIR+"/images/"+username+"/")

    imgdata = fileobj.read()
    if "jpeg" in fileobj.content_type :
        ext = ".jpg"
    elif "png" in fileobj.content_type :
        ext = ".png"
    filename = timestamp()
    image = open(ROOT_DIR+"/images/"+username+"/"+filename+ext,"w")
    err = image.write(data)
    image.close()
    if ext == ".png":
        im = Image.open(ROOT_DIR+"/images/"+username+"/"+filename+ext)
        ext = ".jpg"
        im.save(ROOT_DIR+"/images/"+username+"/"+filename+ext,"JPEG")
        os.remove(ROOT_DIR+"/images/"+username+"/"+filename+".png")

    jsonreturnurl = username+"/"+filename+ext
    return HttpResponse('{"status" : 200 , "url" : "'+jsonreturnurl+'"}',content_type="application/json",status=200)

def userimages(request,username):
    if (not os.path.isdir(ROOT_DIR+"/images/"+username)):
        jsonresp = '{"status":404,"error":"User not found"}'
        return HttpResponse(jsonresp,content_type="application/json",status=404)
    images = os.listdir(ROOT_DIR+"/images/"+username)
    jsonreturn = ""
    for image in images:
        jsonreturn += "{ \"url\" : \""+username+"/"+image+"\"},"
    jsonreturn = "[" + jsonreturn[:len(jsonreturn)-1] + "]"
    newResponse = HttpResponse(jsonreturn)
    newResponse["Content-Type"] = "application/json"
    return newResponse

def serveimage(request,username,imgname):
    if (not os.path.isdir(ROOT_DIR+"/images/"+username)):
        jsonresp = '{"status":404,"error":"User not found"}'
        return HttpResponse(jsonresp,content_type="application/json",status=404)
    if (not os.path.exists(ROOT_DIR+"/images/"+username+"/"+imgname)):
        jsonresp = '{"status":404,"error":"Image not found"}'
        return HttpResponse(jsonresp,content_type="application/json",status=404)
    img = open(ROOT_DIR+"/images/"+username+"/"+imgname,"r")
    data = img.read()
    return HttpResponse(data,content_type="image/jpeg")

def timestamp():
    return time.strftime("%d-%m-%Y.%H-%M-%S")

import os
import zlib
import time
import serial
from SimpleCV import Camera
from threading import Thread
cam=Camera(camera_index=0,prop_set={'width':200,'height':200})

left_top=(255,255,255)
left_bottom=(255,255,255)
right_top=(255,255,255)
right_bottom=(255,255,255)

Volt1='Volt1:'
Volt2='Volt2:'
Dist='Dist:'

def recvdata():
    global left_top,left_bottom,right_top,right_bottom,Volt1,Volt2,Dist
    a=serial.Serial('/dev/ttyUSB0',9600)
    while True:
        while a.inWaiting():
            tmpstr=a.read(a.inWaiting())
            print tmpstr
            Volt1='Volt1:'+tmpstr[1+tmpstr.find('A'):tmpstr.find('B')]
            Volt2='Volt2:'+tmpstr[1+tmpstr.find('B'):tmpstr.find('C')]
            Dist='Dist:'+tmpstr[1+tmpstr.find('C'):tmpstr.find('D')]
            boolstr=tmpstr[1+tmpstr.find('D'):tmpstr.find(';')]
            if boolstr[0]=='1':
                left_top=(0,255,0)
            elif boolstr[0]=='0':
                left_top=(255,255,255)
            else:
                left_top=(255,0,0)
            if boolstr[1]=='1':
                right_top=(0,255,0)
            elif boolstr[1]=='0':
                right_top=(255,255,255)
            else:
                right_top=(255,0,0)
            if boolstr[2]=='1':
                left_bottom=(0,255,0)
            elif boolstr[2]=='0':
                left_bottom=(255,255,255)
            else:
                left_bottom=(255,0,0)
            if boolstr[3]=='1':
                right_bottom=(0,255,0)
            elif boolstr[3]=='0':
                right_bottom=(255,255,255)
            else:
                right_bottom=(255,0,0)


t=Thread(target=recvdata)
t.setDaemon(1)
t.start()


i=0
while True:


    img=cam.getImage()



    img.dl().line((img.width*0.15,img.height*0.8),(img.width*0.25,img.height*0.8),color=(255,255,255),width=2)
    img.dl().line((img.width*0.15,img.height*0.9),(img.width*0.25,img.height*0.9),color=(255,255,255),width=2)

    img.dl().line((img.width*0.19,img.height*0.8),(img.width*0.19,img.height*0.9),color=(255,255,255),width=2)
 
    img.dl().rectangle((img.width*0.13,img.height*0.79),(img.width*0.04,img.height*0.04),color=left_top,filled=True)#left top
    img.dl().rectangle((img.width*0.13,img.height*0.89),(img.width*0.04,img.height*0.04),color=left_bottom,filled=True)#left bottom
    img.dl().rectangle((img.width*0.23,img.height*0.79),(img.width*0.04,img.height*0.04),color=right_top,filled=True)#right top
    img.dl().rectangle((img.width*0.23,img.height*0.89),(img.width*0.04,img.height*0.04),color=right_bottom,filled=True)#right bottom

    img.drawText(text=Volt1,color=(255,255,255),x=img.width*0.6,y=img.height*0.75,fontsize=14)
    img.drawText(text=Volt2,color=(255,255,255),x=img.width*0.6,y=img.height*0.80,fontsize=14)
    img.drawText(text=Dist,color=(255,255,255),x=img.width*0.6,y=img.height*0.85,fontsize=14)


    img.save('/tmp/bbb.jpg')
    os.system('mv /tmp/bbb.jpg /tmp/aaa.jpg')
    # time.sleep(0.05)
    i+=1
    print i




#!/usr/bin/env python
# a=20
# def test():
# 	global a
# 	print 'Now a is %s' %a
# 	a*=2
# 	print 'a*2 is %s' %a

# test()

# try:
# 	print a
# except KeyboardInterrupt:
# 	pass
# 	print 'bbbbb'
# finally:
# 	print 'aaaaa'

#print 'In main thread, a is %s' %a


# import sys, time

# def fwrite(buf):
# 	sys.stdout.write(buf)
# 	sys.stdout.flush()

# spinners='|/-\\'
# spinpos=0
# while 1:
# 	fwrite(spinners[spinpos]+'\b')
# 	spinpos+=1
# 	if spinpos>=len(spinners):
# 		spinpos=0
# 	time.sleep(0.15)


# fwrite('a'+'\b')
# time.sleep(2)
# fwrite('b'+'\b')
# time.sleep(2)
# fwrite('c'+'\b')
# fwrite('d'+'\b')
# fwrite('e'+'\b')







# import threading, time

# childthread=[]
# con=threading.Condition()
# sec=0

# def threadcode():
# 	while 1:
# 		con.acquire()
# 		con.wait()
# 		print 'Thread %s is running.' %threading.currentThread().getName()
# 		con.release()
# 		time.sleep(1.3)


# for i in range(1,5):
# 	t=threading.Thread(target=threadcode,name='Thread-%d' %i)
# 	t.setDaemon(1)
# 	t.start()
# 	childthread.append(t)
# # t=threading.Thread(target=threadcode,name='Thread-1')
# # t.setDaemon(1)
# # t.start()
# # childthread.append(t)

# time.sleep(2)

# while 1:
# 	con.acquire()
# 	con.notifyAll()
# 	sec+=5
# 	print 'time is %d' %sec
# 	con.release()
# 	print childthread
# 	time.sleep(3)





# def cal():
# 	for i in xrange(100000):
# 		a[i]=i+i

# a=range(100000)

# for i in xrange(100):
# 	cal()





# var=['22','adff','213']
# string=','.join(var)
# print string








# f=open('/tmp/result.txt','r')
# currentPlaneList=[]

# tmplist=f.readlines()
# # TODO
# while True:
# 	tmpstr=tmplist.pop()
# 	if tmpstr.find('-----') != -1:
# 		break
# 	plane=tmpstr.split()
# 	if(len(plane)==12 and plane.count('S')==1):
# 		currentPlaneList.append(plane)

# f.close()








# import os
# import time
# from threading import Thread
# from datetime import datetime



# import time
# f=open('/tmp/tmp.txt','r')


# currentPlaneList=[]

# while True:
#     tmplist=f.readlines()
#     # Get planes' information
#     while True:
#         try:
#             tmpstr=tmplist.pop()
#         except:
#             time.sleep(1)
#             tmplist=f.readlines()
#             continue
#         if tmpstr.find('-----')!=-1:
#             break
#         plane=tmpstr.split()
#         if len(plane)<3:
#             continue
#         planedict=dict(Hex='',Mode='',Squawk='',Flight='',Altitude='',Speed='',Heading='',Latitude='',Longtitute='')
#         # if(len(plane)==12 and plane.count('S')==1):        # TODO:optimize
#         #   currentPlaneList.append(plane)

#         if(plane.count('S')):
#             planedict['Mode']='S'
#             planedict['Hex']=plane[0] if plane[1]=='S' else ''

#         for i in xrange(len(plane)):
#             if plane[i][0].isalpha() and plane[i][-1].isdigit():
#                 planedict['Flight']=plane[i] 
#             if plane[i].find('.') and len(plane[i])==6:
#                 planedict['Latitude']=plane[i] 
#             if plane[i].find('.') and len(plane[i])==7:
#                 planedict['Longtitute']=plane[i] 

#         if planedict['Mode']!='' and planedict['Flight']!='':
#             if plane.index(planedict['Mode'])-plane.index(planedict['Flight'])==-2:
#                 planedict['Squawk']=plane[plane.index(planedict['Mode'])+1]

#         if planedict['Latitude']!='':
#             if plane[plane.index(planedict['Latitude'])-1].isdigit() and int(plane[plane.index(planedict['Latitude'])-1])<=360:
#                 planedict['Heading']=plane[plane.index(planedict['Latitude'])-1]

#         if planedict['Heading']!='':
#             if plane[plane.index(planedict['Heading'])-1].isdigit() and int(plane[plane.index(planedict['Heading'])-1])<1000:
#                 planedict['Speed']=plane[plane.index(planedict['Heading'])-1]

#         if planedict['Speed']!='':
#             if plane[plane.index(planedict['Speed'])-1].isdigit():
#                 planedict['Altitude']=plane[plane.index(planedict['Speed'])-1]

#         if planedict['Latitude']!='' and planedict['Longtitute']!='':
#             currentPlaneList.append(planedict)

#     if len(currentPlaneList)==0:
#         continue

#     # Get current time
#     now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#     # Save planes' information to currentData.xml
#     currentData=open('/tmp/tmp.xml','w')
#     currentData.write('<?xml version="1.0" encoding="ISO-8859-1"?>\n')
#     currentData.write('<DataFrame>\n')
#     for i in xrange(len(currentPlaneList)):
#         currentData.write('\t<Plane>\n')
#         currentData.write('\t\t<Time>%s</Time>\n' % (now))
#         currentData.write('\t\t<Hex>%s</Hex>\n' % (currentPlaneList[i]['Hex']))
#         currentData.write('\t\t<Mode>%s</Mode>\n' % (currentPlaneList[i]['Mode']))  
#         currentData.write('\t\t<Squawk>%s</Squawk>\n' % (currentPlaneList[i]['Squawk']))
#         currentData.write('\t\t<Flight>%s</Flight>\n' % (currentPlaneList[i]['Flight']))
#         currentData.write('\t\t<Altitude>%s</Altitude>\n' % (currentPlaneList[i]['Altitude']))
#         currentData.write('\t\t<Speed>%s</Speed>\n' % (currentPlaneList[i]['Speed']))
#         currentData.write('\t\t<Heading>%s</Heading>\n' % (currentPlaneList[i]['Heading']))
#         currentData.write('\t\t<Latitude>%s</Latitude>\n' % (currentPlaneList[i]['Latitude']))
#         currentData.write('\t\t<Longtitute>%s</Speed>\n' % (currentPlaneList[i]['Speed']))
#         currentData.write('\t</Plane>\n')
#     currentData.write('</DataFrame>\n')
#     currentData.close()

#     # Initialise
#     currentPlaneList=[]
#     time.sleep(1)










# NxQ1NDMYcDcw53gVHzI7
# NxQ1ND8UfDM862QaEDk4




# import hashlib


# s='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# def yanzhen(strb):
#     for i1 in xrange(62):
#         for i2 in xrange(62):
#             for i3 in xrange(62):
#                 for i4 in xrange(62):
#                     for i5 in xrange(62):
#                         tmp=strb+s[i1]+s[i2]+s[i3]+s[i4]+s[i5]
#                         ha = hashlib.sha1()
#                         ha.update(tmp)
#                         if ord(ha.digest()[-1])==0 and ord(ha.digest()[-2])==0:
#                             print 'tmp is',tmp
#                             print '1'
#                             return tmp
# print yanzhen('hUzjE9OTYeWrcDwz')



# def fibs(num):
#     result=[0,1]
#     for i in range(num-2):
#         result.append(result[-2]+result[-1])
#     return result

# print fibs(1690)










# import time
# from SimpleCV import *
# img=Image('/tmp/bbb.jpg')
# imgStr=img.toString()
# print len(imgStr)

# import zlib
# tmp=zlib.compress(imgStr)
# print 'after zlib',len(tmp)
# print len(zlib.decompress(tmp))

# import pygame
# pygame.init()
# screen=pygame.display.set_mode((914, 1289))
# pygame.display.set_caption('Image Show')

# camshot=pygame.image.frombuffer(imgStr,(914, 1289),'RGB')
# screen.blit(camshot,(0,0))
# pygame.display.update()
# time.sleep(5)

# camshot=pygame.image.load('/tmp/bbb.jpg')
# screen.blit(camshot,(0,0))
# pygame.display.update()
# time.sleep(5)



import os
import zlib
import time
from SimpleCV import Camera
cam=Camera(camera_index=0,prop_set={'width':200,'height':200})

# import pygame
# pygame.init()
# screen=pygame.display.set_mode((320,240))
# pygame.display.set_caption('Image Show')
# clock=pygame.time.Clock()

i=0
while True:
    # img=cam.getImage()
    # imgStr=img.toString()
    # camshot=pygame.image.frombuffer(imgStr,(320,240),'RGB')
    # screen.blit(camshot,(0,0))
    # pygame.display.update()
    # print clock.get_fps()
    # clock.tick()
    # # print len(zlib.compress(imgStr))
    # print len(imgStr)
    # # time.sleep(0.1)

    img=cam.getImage()


    img.dl().rectangle((img.width*0.13,img.height*0.79),(img.width*0.04,img.height*0.04),color=(255,255,255),filled=True)#left top
    img.dl().rectangle((img.width*0.13,img.height*0.89),(img.width*0.04,img.height*0.04),color=(255,255,255),filled=True)#left bottom
    img.dl().rectangle((img.width*0.23,img.height*0.79),(img.width*0.04,img.height*0.04),color=(255,255,255),filled=True)#right top
    img.dl().rectangle((img.width*0.23,img.height*0.89),(img.width*0.04,img.height*0.04),color=(255,255,255),filled=True)#right bottom

    img.dl().line((img.width*0.15,img.height*0.8),(img.width*0.25,img.height*0.8),color=(255,255,255),width=2)
    img.dl().line((img.width*0.15,img.height*0.9),(img.width*0.25,img.height*0.9),color=(255,255,255),width=2)

    img.dl().line((img.width*0.19,img.height*0.8),(img.width*0.19,img.height*0.9),color=(255,255,255),width=2)

    img.drawText(text='Volt1:12.11v',color=(255,255,255),x=img.width*0.6,y=img.height*0.75,fontsize=14)
    img.drawText(text='Volt1:12.11v',color=(255,255,255),x=img.width*0.6,y=img.height*0.80,fontsize=14)
    img.drawText(text='Volt1:12.11v',color=(255,255,255),x=img.width*0.6,y=img.height*0.85,fontsize=14)


    img.save('/tmp/bbb.jpg')
    os.system('mv /tmp/bbb.jpg /tmp/aaa.jpg')
    # time.sleep(0.05)
    i+=1
    print i



# img=cam.getImage()
# img.drawText(text='Hello World',x=240,y=220,color=(255,255,255))
# img.show()

# img=Image('lenna')
# img.drawLine((img.width*0.5,img.height*0.20),(img.width*0.5,img.width*0.60),color=(255,255,255))
# img.drawLine((img.width*0.15,img.height*0.4),(img.width*0.85,img.height*0.4),color=(255,255,255))
# img.show()


# img=Image('lenna')
# img.drawRectangle(img.width*0.1,img.height*0.6,img.width*0.3,img.height*0.3,color=(255,255,255),width=1,alpha=255)
# img.show()
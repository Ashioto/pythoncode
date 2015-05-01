# import rsa

# (pubkey, privkey) = rsa.newkeys(1024)
 
# pub = pubkey.save_pkcs1()
# pubfile = open('public.pem','w+')
# pubfile.write(pub)
# pubfile.close()
 
# pri = privkey.save_pkcs1()
# prifile = open('private.pem','w+')
# prifile.write(pri)
# prifile.close()




# c5475050ed61fd11bd10cb7f1ad7a729









# import hashlib
# import string
# import socket,sys
# import time

# s='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)



# def yanzhen(strb):
# 	for i1 in xrange(62):
# 		for i2 in xrange(62):
# 			for i3 in xrange(62):
# 				for i4 in xrange(62):
# 					for i5 in xrange(62):
# 						tmp=strb+s[i1]+s[i2]+s[i3]+s[i4]+s[i5]
# 						ha = hashlib.sha1()
# 						ha.update(tmp)
# 						if ord(ha.digest()[-1])==0 and ord(ha.digest()[-2])==0:
# 							return tmp



# for x1 in xrange(62):
# 	for x2 in xrange(62):
# 		for x3 in xrange(62):
# 			for x4 in xrange(62):
# 				tmpstr=s[x1]+s[x2]+s[x3]+s[x4]
# 				sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 				sock.connect(('146.148.79.13',8888))
# 				stra=sock.recv(1024)
# 				print 'send back',stra
# 				tmp=yanzhen(stra[-17:-1])
# 				sendstr=tmp+tmpstr+'\n'
# 				sock.send(sendstr)
# 				print 'sendstr is',sendstr
# 				time.sleep(1)
# 				# sock.send(tmpstr)
# 				result=sock.recv(1024)
# 				print 'result is',result[-21:-1]
# 				sock.close()
# 				if result[-21:-1]=='NxQ1NDMYcDcw53gVHzI7':
# 					print 'Done!!!!!!!!!!!!!!!!!!'
# 					sys.exit(0)


# NxQ1NDEWcjU+5XoaBDo7

# NxQ1NDIZcTY/5HkaBS8=
# NxQ1NDMYcDcw53gVHzI7


# import hashlib
# SALT='dsafasfasfdd'
# N=17
# import os, sys
# import binascii
# import SocketServer
# import base64 as b64
# import hashlib
# import string


# def updateDict(s, lzwDict):
#     if not s in lzwDict:
#         count = len(lzwDict.keys())
#         lzwDict[s] = count % 256

# def LZW(s, lzwDict): # LZW written by NEWBIE
#     for c in s: updateDict(c, lzwDict)
#     # print lzwDict # have to make sure it works
#     result = []
#     i = 0
#     while i < len(s):
#         if s[i:] in lzwDict:
#             result.append(lzwDict[s[i:]])
#             break
#         for testEnd in range(i+2, len(s)+1):
#             if not s[i:testEnd] in lzwDict:
#                 updateDict(s[i:testEnd], lzwDict)
#                 result.append(lzwDict[s[i:testEnd-1]])
#                 i = testEnd - 2
#                 break
#         i += 1
#     return result

# def salted(m):
#     cyclesalt = SALT * (len(m)/len(SALT) + 1)
#     return "".join([ m[i] + cyclesalt[i] for i in range(len(m)) ])

# def STRONGPseudoRandomGenerator(s):
#     return s[13 - 16 :], hashlib.md5(s).digest()

# def encrypt(m):
#     lzwDict = dict()
#     toEnc = LZW(SALT + m, lzwDict)
#     key = hashlib.md5(SALT*2).digest()
#     OTPBase = ""
#     OPT = ""
#     step = 16 - 13
#     for i in range(0, 3*N+step, step):
#         rand, key = STRONGPseudoRandomGenerator(key)
#         OTPBase += rand
#     enc = []
#     otpadded = []
#     for i in range(len(toEnc)):
#         index = i % N
#         iRound = i / N + 1
#         OTP = OTPBase[3*int(pow(ord(OTPBase[3*index]),ord(OTPBase[3*index+1])*iRound, N))+2]
#         otpadded.append(ord(OTP))
#         enc.append(chr(toEnc[i] ^ ord(OTP)))
#     return b64.b64encode(''.join(enc))



# print encrypt('dsafadf')






f=open('/home/laputa/Documents/python/sushubiao.txt','r')
s=f.read()
print s
ss=s.split()
print ss
while True:
	N=int(raw_input('Please enter a integer\n'))

	print ss[N-1]
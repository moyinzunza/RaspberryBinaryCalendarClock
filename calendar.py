#Orden de los pines
#GPIO4 = Led1
#GPIO5 = Led2
#GPIO6 = Led3
#GPIO12 = Led4
#GPIO13 = Led5


#GPIO16 = Led6
#GPIO17 = Led7
#GPIO18 = Led8
#GPIO19 = Led9
#GPIO20 = Led10
#GPIO21 = Led11
#GPIO22 = Led12

#GPIO23 = Led13
#GPIO24 = Led14

#GPIO25 = Button


import RPi.GPIO as GPIO
import time
import datetime
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_UP)

totalpinarray = [4,5,6,12,13,16,17,18,19,20,21,22,23,24]

pinMesHora = [0,4,5,6,12,13]
pinDiaMin = [0,16,17,18,19,20,21,22]

print(time.strftime("%m-%d"))


## Test Encendido de leds
#try:
#	while(1):
#		for x in range(0, len(pinarray)):
#			GPIO.output(pinarray[x], 1)
#			time.sleep(1)
#			GPIO.output(pinarray[x], 0)
#			time.sleep(1)

def MostrarMes():
	now = datetime.datetime.now()
	mes = now.month
	if mes >= 10:
		GPIO.output(pinMesHora[1], 1)
		if mes == 10:
			GPIO.output(pinMesHora[2], 0)
			GPIO.output(pinMesHora[3], 0)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 11:
			GPIO.output(pinMesHora[2], 1)
			GPIO.output(pinMesHora[3], 0)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 12:
			GPIO.output(pinMesHora[2], 0)
			GPIO.output(pinMesHora[3], 1)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 0)
	else:
		GPIO.output(pinMesHora[1], 0)

		if mes == 1:
			GPIO.output(pinMesHora[2], 1)
			GPIO.output(pinMesHora[3], 0)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 2:
			GPIO.output(pinMesHora[2], 0)
			GPIO.output(pinMesHora[3], 1)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 3:
			GPIO.output(pinMesHora[2], 1)
			GPIO.output(pinMesHora[3], 1)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 0)

		elif mes == 4:
			GPIO.output(pinMesHora[2], 0)
			GPIO.output(pinMesHora[3], 0)
			GPIO.output(pinMesHora[4], 1)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 5:
			GPIO.output(pinMesHora[2], 1)
			GPIO.output(pinMesHora[3], 0)
			GPIO.output(pinMesHora[4], 1)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 6:
			GPIO.output(pinMesHora[2], 0)
			GPIO.output(pinMesHora[3], 1)
			GPIO.output(pinMesHora[4], 1)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 7:
			GPIO.output(pinMesHora[2], 1)
			GPIO.output(pinMesHora[3], 1)
			GPIO.output(pinMesHora[4], 1)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 8:
			GPIO.output(pinMesHora[2], 0)
			GPIO.output(pinMesHora[3], 0)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 1)
		elif mes == 9:
			GPIO.output(pinMesHora[2], 1)
			GPIO.output(pinMesHora[3], 0)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 1)
	return

def MostrarDia():
	now = datetime.datetime.now()
	dia = now.day
	if dia >= 30:
		GPIO.output(pinDiaMin[1], 1)
		GPIO.output(pinDiaMin[2], 1)
		GPIO.output(pinDiaMin[3], 0)
		if dia == 30:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 31:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
	elif dia >= 20:
		GPIO.output(pinDiaMin[1], 0)
		GPIO.output(pinDiaMin[2], 1)
		GPIO.output(pinDiaMin[3], 0)
		if dia == 20:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 21:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 22:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 23:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 24:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 25:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 26:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 27:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 28:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
		elif dia == 29:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
	elif dia >= 10:
		GPIO.output(pinDiaMin[1], 1)
		GPIO.output(pinDiaMin[2], 0)
		GPIO.output(pinDiaMin[3], 0)
		if dia == 10:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 11:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 12:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 13:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 14:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 15:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 16:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 17:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 18:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
		elif dia == 19:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
	else:
		GPIO.output(pinDiaMin[1], 0)
		GPIO.output(pinDiaMin[2], 0)
		GPIO.output(pinDiaMin[3], 0)
		if dia == 1:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 2:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 3:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 4:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 5:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 6:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 7:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 8:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
		elif dia == 9:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
		else:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
	return


def MostrarHora():

	now = datetime.datetime.now()

	mes = now.hour
	if now.hour == 0:
		mes = 12
	elif now.hour == 13:
		mes = 1
	elif now.hour == 14:
		mes = 2
	elif now.hour == 15:
		mes = 3
	elif now.hour == 16:
		mes = 4
	elif now.hour == 17:
		mes = 5
	elif now.hour == 18:
		mes = 6
	elif now.hour == 19:
		mes = 7
	elif now.hour == 20:
		mes = 8
	elif now.hour == 21:
		mes = 9
	elif now.hour == 22:
		mes = 10
	elif now.hour == 23:
		mes = 11

	if mes >= 10:
		GPIO.output(pinMesHora[1], 1)
		if mes == 10:
			GPIO.output(pinMesHora[2], 0)
			GPIO.output(pinMesHora[3], 0)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 11:
			GPIO.output(pinMesHora[2], 1)
			GPIO.output(pinMesHora[3], 0)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 12:
			GPIO.output(pinMesHora[2], 0)
			GPIO.output(pinMesHora[3], 1)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 0)
	else:
		GPIO.output(pinMesHora[1], 0)

		if mes == 1:
			GPIO.output(pinMesHora[2], 1)
			GPIO.output(pinMesHora[3], 0)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 2:
			GPIO.output(pinMesHora[2], 0)
			GPIO.output(pinMesHora[3], 1)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 3:
			GPIO.output(pinMesHora[2], 1)
			GPIO.output(pinMesHora[3], 1)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 0)

		elif mes == 4:
			GPIO.output(pinMesHora[2], 0)
			GPIO.output(pinMesHora[3], 0)
			GPIO.output(pinMesHora[4], 1)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 5:
			GPIO.output(pinMesHora[2], 1)
			GPIO.output(pinMesHora[3], 0)
			GPIO.output(pinMesHora[4], 1)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 6:
			GPIO.output(pinMesHora[2], 0)
			GPIO.output(pinMesHora[3], 1)
			GPIO.output(pinMesHora[4], 1)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 7:
			GPIO.output(pinMesHora[2], 1)
			GPIO.output(pinMesHora[3], 1)
			GPIO.output(pinMesHora[4], 1)
			GPIO.output(pinMesHora[5], 0)
		elif mes == 8:
			GPIO.output(pinMesHora[2], 0)
			GPIO.output(pinMesHora[3], 0)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 1)
		elif mes == 9:
			GPIO.output(pinMesHora[2], 1)
			GPIO.output(pinMesHora[3], 0)
			GPIO.output(pinMesHora[4], 0)
			GPIO.output(pinMesHora[5], 1)
	return

def MostrarMinutos():
	now = datetime.datetime.now()
	dia = now.minute
	if dia >= 50:
		GPIO.output(pinDiaMin[1], 1)
		GPIO.output(pinDiaMin[2], 0)
		GPIO.output(pinDiaMin[3], 1)
		if dia == 50:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 51:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 52:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 53:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 54:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 55:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 56:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 57:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 58:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
		elif dia == 59:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)

	elif dia >= 40:
		GPIO.output(pinDiaMin[1], 0)
		GPIO.output(pinDiaMin[2], 0)
		GPIO.output(pinDiaMin[3], 1)
		if dia == 40:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 41:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 42:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 43:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 44:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 45:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 46:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 47:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 48:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
		elif dia == 49:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)

	elif dia >= 30:
		GPIO.output(pinDiaMin[1], 1)
		GPIO.output(pinDiaMin[2], 1)
		GPIO.output(pinDiaMin[3], 0)
		if dia == 30:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 31:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 32:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 33:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 34:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 35:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 36:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 37:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 38:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
		elif dia == 39:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
	elif dia >= 20:
		GPIO.output(pinDiaMin[1], 0)
		GPIO.output(pinDiaMin[2], 1)
		GPIO.output(pinDiaMin[3], 0)
		if dia == 20:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 21:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 22:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 23:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 24:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 25:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 26:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 27:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 28:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
		elif dia == 29:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
	elif dia >= 10:
		GPIO.output(pinDiaMin[1], 1)
		GPIO.output(pinDiaMin[2], 0)
		GPIO.output(pinDiaMin[3], 0)
		if dia == 10:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 11:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 12:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 13:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 14:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 15:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 16:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 17:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 18:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
		elif dia == 19:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
	else:
		GPIO.output(pinDiaMin[1], 0)
		GPIO.output(pinDiaMin[2], 0)
		GPIO.output(pinDiaMin[3], 0)
		if dia == 1:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 2:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 3:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 4:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 5:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 6:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 7:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 1)
			GPIO.output(pinDiaMin[6], 1)
			GPIO.output(pinDiaMin[7], 0)
		elif dia == 8:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
		elif dia == 9:
			GPIO.output(pinDiaMin[4], 1)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 1)
		else:
			GPIO.output(pinDiaMin[4], 0)
			GPIO.output(pinDiaMin[5], 0)
			GPIO.output(pinDiaMin[6], 0)
			GPIO.output(pinDiaMin[7], 0)
	return
isdate = 0
buttonPress = 1
try:
	while(1):
		os.system("clear")
		print("Moy Raspberry CalendarClock")
		print(time.strftime("%m-%d %I:%M:%S"))
		buttonPress = GPIO.input(25)
		if buttonPress == 0 and isdate == 0:
			isdate = 1
		elif buttonPress == 0 and isdate == 1:
			isdate = 0

		if isdate == 1:
			MostrarMes()
			MostrarDia()
			GPIO.output(23, 0)
			GPIO.output(24, 1)
		else:
			GPIO.output(23, 1)
			GPIO.output(24, 0)
			MostrarHora()
			MostrarMinutos()
		time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()

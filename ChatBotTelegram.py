# -*- coding: utf-8 -*-
import random

import telebot
import pyborg
import sys

TOKEN = ''

bot = telebot.TeleBot(TOKEN)
ia = pyborg.pyborg()

class elBot(object):

	def __init__(self, tg):
		self.tg = tg

	def set_m(self, m):
		self.m = m

	def output(self, mensaje, argumento):
		mensaje = mensaje.replace("#nick", argumento)
		self.tg.send_chat_action(self.m.chat.id, 'typing')
		self.tg.reply_to(self.m, mensaje)

# creamos un objeto que responde. Él pasa de pyborg a Telegram el mensaje.
elbot = elBot(bot)

def filtro(mensaje):
	mensaje = mensaje.replace('\\','')
	mensaje = mensaje.replace('@','')
	return mensaje

def es_invalido(mensaje):
	if mensaje.find('http')!=-1 \
	 or mensaje.find('gay')!=-1:
		return True

enable_reply = True # permitimos el responder.

def listener(mensajes):
	for m in mensajes:
		if m.content_type == 'text':
			mensaje = m.text
			usuario = m.from_user.first_name
			cid = m.chat.id

			# aleatoriamente guardamos
			if random.randint(0,4)==3:
				ia.save_all()

			if enable_reply:
				# respondemos.
				# filtramos mensaje
				mensaje = filtro(mensaje)
				elbot.set_m(m) # le enviamos la información para que pueda responder.
				if es_invalido(mensaje):
					print('Mensaje invalido: ' + mensaje)
					continue
				probabilidad_responder=98
				
				if len(mensaje.split(' '))==2:
					if random.randint(0,3)!=2:
						continue
				ia.process_msg(elbot, mensaje, probabilidad_responder, learn, usuario, owner = 0)
			
			else:
				# sólo aprendemos.
				ia.learn(mensaje)
				print('Sólo aprendemos')
		else:
			print('no es texto, quizás es un evento de que alguien entro, enviaron una foto, cambiaron el nombre del grupo, etc. Menos lo que queremos que es un texto')
				


bot.set_update_listener(listener)

bot.polling(none_stop=True, timeout=200)

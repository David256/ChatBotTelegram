# -*- coding: utf-8 -*-
import random

import telebot
import pyborg
import sys

TOKEN = ''

bot = telebot.TeleBot(TOKEN)
ia = pyborg.pyborg()

class elBot(object):
	"""
	Esta clase es la encargada de recojer el mensaje que libera la clase pyBorg. Además,
	se encarga de responder por medio de un objeto, instaciado de la clase TeleBot, al 
	usuario que efectuó la acción de enviarle un mensaje.
	"""

	def __init__(self, tg):
		self.tg = tg

	def set_m(self, m):
		"""
		Redefine el objeto Message que indica quién envió el mensaje, su id para responderle
		, y otros atributos. Acá solo se usará para poder responderle al usuario de forma
		cómoda.
		"""
		self.m = m

	def output(self, mensaje, argumento):
		"""
		Este método recibe el mensaje, como respuesta, desde un objeto de tipo pyBorg.

		:param mensaje:		es el mensaje en si, un texto.
		:param argumento:	es el sujeto.
		"""
		mensaje = mensaje.replace("#nick", argumento)
		# esto hace que Telegram muestre que el bot está escribiendo...
		self.tg.send_chat_action(self.m.chat.id, 'typing') # <---
		self.tg.reply_to(self.m, mensaje)

# creamos un objeto que responde. Él pasa de pyborg a Telegram el mensaje.
elbot = elBot(bot)

def filtro(mensaje):
	"""
	Intento de filtrar los comandos enviados a los demás bots para que éste no
	aprenda de ellos. Los comandos son de la forma:

	/comando@botQueLosRecibe
	"""
	mensaje = mensaje.replace('\\','')
	mensaje = mensaje.replace('@','')
	return mensaje

def es_invalido(mensaje):
	"""
	Intento de filtrar las URL y una que otras palabras que no queremos que el bot
	aprenda y luego le responda a otro usuario.
	"""
	if mensaje.find('http')!=-1 \
	 or mensaje.find('gay')!=-1:
		return True

enable_reply = True # permitimos el responder.


"""
Esta variable es 1 si queremos que el bot 'aprenda'. Ó es cero si queremos que sólo
rsponda a lo que se le envía.
"""
learn = 1

def listener(mensajes):
	"Este método recibe los mensaje enviados desde Telegram."
	for m in mensajes:
		if m.content_type == 'text':
			mensaje = m.text
			usuario = m.from_user.first_name

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
						continue # ignoramos palabras simples.
				ia.process_msg(elbot, mensaje, probabilidad_responder, learn, usuario, owner = 0)
			
			else:
				# sólo aprendemos.
				ia.learn(mensaje)
				print('Sólo aprendemos')
		else:
			print('no es texto, quizás es un evento de que alguien entro, enviaron una foto, cambiaron el nombre del grupo, etc. Menos lo que queremos que es un texto')
				


# le indicamos a la API de Telegram que método es el que debe recibir los mensajes.
bot.set_update_listener(listener)

bot.polling(none_stop=True, timeout=200)

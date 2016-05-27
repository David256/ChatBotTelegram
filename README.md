# ChatBotTelegram
Elemental código en Python que permite a un Bot de Telegram tener "inteligencia artificial". La verdad es que mola muchísimo.

Este código es un pequeño [bot](https://es.wikipedia.org/wiki/Bot "bot") de [Telegram](https://es.wikipedia.org/wiki/Telegram_Messenger "Telegram Messenger") que usa la librería de [pyBorg](https://github.com/bdrewery/PyBorg). Está listo para revisar y aprender, además podrás conocer el funcionamiento y crear tú propio _bot de inteligencia artificial_. Luego vas con tus amigos y les muestras lo que has aprendido _:v_


- [Cómo ponerlo en funcionamiento](#c%C3%B3mo-ponerlo-en-funcionamiento)
  - [Consideraciones a tener en cuenta en Windows](#consideraciones-a-tener-en-cuenta-en-windows)
- [Cosas a tener en cuenta](#cosas-a-tener-en-cuenta)
  - [Pero... No tengo Telegram, ¿qué hago?](#pero-no-tengo-telegram-qu%C3%A9-hago)
  - [Pero... El código no me funciona si lo ejecuto con python](#pero-el-c%C3%B3digo-no-me-funciona-si-lo-ejecuto-con-python)
  - [Dónde conseguir este TOKEN](#d%C3%B3nde-conseguir-este-token)
- [Se han creados unos archivos al ejecutar el script del bot...](#se-han-creados-unos-archivos-al-ejecutar-el-script-del-bot)
- [Cómo funciona el bot y como que aprende](#c%C3%B3mo-funciona-el-bot-y-como-que-aprende)


## Cómo ponerlo en funcionamiento
Al ser programado en [Python](https://es.wikipedia.org/wiki/Python) se necesita del interprete en su versión __2.x__ ya que es la versión en que trabaja la librería [pyBorg](https://github.com/bdrewery/PyBorg). Se puede ejecutar simplemente con:

```
python ChatBotTelegram.py
```

### Consideraciones a tener en cuenta en Windows
En el sistema operativo _Windows_ se requiere de la librería de [request](https://pypi.python.org/pypi/requests/ "Librería necesaria por la API de Telegram") que es necesitada por la librería de [la API de Telegram para Bot](https://github.com/eternnoir/pyTelegramBotAPI#getting-started)

## Cosas a tener en cuenta

### Pero... No tengo Telegram, ¿qué hago?
Descargalo [ahora mismo sin ningún problema](https://telegram.org/apps)

### Pero... El código no me funciona si lo ejecuto con python
El código necesita de un __TOKEN__ para que tu _bot_ se pueda comunicar con _Telegram_. En el código está definida la variable `TOKEN` pero está vacía.
```python
# -*- coding: utf-8 -*-
import random

import telebot
import pyborg
import sys

TOKEN = ''

bot = telebot.TeleBot(TOKEN)
```

### Dónde conseguir este TOKEN
Dentro de telegram te tienes que poner en contacto con _El gran Bot_ de [@BotFather](http://telegram.me/BotFather). Entonces le hablas y le dice que quieres un bot, pero como BotFather no entiende el castellano (ni el inglés, el esperanto, el árabe, o cualquier otro idioma) le tienes que hablar por medios de comandos.

Al comienso te saldrá un botón que dice __START__ (al menos que diga otra cosa porque lo has configurado con otro idioma o cualquier motivo absurdo) que debes presionar, entonces BotFather te responderá con una serie de comandos para crear tu bot.
Con el comando `/newbot` de expresas tus deseos por crear un <s>homúnculo</s> bot nuevo. Luego de esto BotFather te pedirá el nombre y el __@username__ del nuevo bot.

Como por arte de magía BotFather te enviará un mensaje y dentro de éste estará el preciado __TOKEN__. Ahora corres a tu código python y lo pegas donde debería ir:

```python
TOKEN = 'CaRa-Teres:RarossNoSerPelotu2niCopiarEsto'
```

Ahora estará todo listo.

Puedes seguir charlando con BotFather y decirle todo lo que quieres para tu nuevo bot, como la imagen del perfil, la descripción, etc.

## Se han creados unos archivos al ejecutar el script del bot...
Si amigo, entre ellos está `archive.zip` si no estoy mal. Estos archivos permiten nada más y nada menos que el bot __APRENDAAA!!!__. Así no más.

## Cómo funciona el bot y como que aprende
El bot lee los mensajes que recibe y los despedaza en trocitos (como lo hace [Jack el destripador](https://es.wikipedia.org/wiki/Jack_el_Destripador)) y después lo guarda en `archive.zip`. Al momento de recibir el mensaje, y habiendo almacenado ya un gran número de __oraciones__ el bot es capaz de responder en función de todo lo que ha aprendido, en las palabras que conoce, en la forma como se usaron, y en el número de veces que fueron usadas, y en otros factores.

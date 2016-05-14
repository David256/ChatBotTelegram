# ChatBotTelegram
Elemental código en Python que permite a un Bot de Telegram tener "inteligencia artificial". La verdad es que mola muchísimo.

Este código es un pequeño [bot](https://es.wikipedia.org/wiki/Bot "bot") de [Telegram](https://es.wikipedia.org/wiki/Telegram_Messenger "Telegram Messenger") que usa la librería de [pyBorg](https://github.com/bdrewery/PyBorg). Está listo para revisar y aprender, además podrás conocer el funcionamiento y crear tú propio _bot de inteligencia artificial_. Luego vas con tus amigos y les muestras lo que has aprendido _:v_

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



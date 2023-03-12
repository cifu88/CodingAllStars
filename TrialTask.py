#Librerias:

from bs4 import BeautifulSoup
import requests
from deep_translator import GoogleTranslator

#Traer la página on bs4:

url = 'https://www.classcentral.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
response = requests.get(url, headers=headers, stream=True)
html = response.content
soup = BeautifulSoup(response.text, 'html.parser')

traductor = GoogleTranslator(source='en', target='hi')
trans = {}
trans_dir = {}

#Obtener texto traducido
for child in soup.stripped_strings:
  if child == 'Copy link':
    continue
  else:
    traduccion = (traductor.translate(child))
    trans[str(child)]=str(traduccion)
    
texto = list(soup.stripped_strings)
texto2 = []
for i in texto:
    if i in texto2:
        continue
    else:
        texto2.append(i)

for i in range (len(texto2)):
    for texto in soup.find_all(string=True):
      if texto.parent.name != 'style' and texto.parent.name != 'script':
        if texto2[i] in trans.keys():
            nuevo_texto = texto.replace(texto2[i], trans[texto2[i]])
            texto.replace_with(nuevo_texto)

#descargar archivo traducido:
with open('casi.html', 'w', encoding='utf-8') as f:
    mensaje = str(soup)
    f.write(mensaje)
    f.close()
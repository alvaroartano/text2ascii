import sys
import requests #librería para hacer las peticiones a la api
import time #libreria para esperar tiempo (aun no usada)
import os   #libreria para saber desde que sistema se usa.
from colorama import Fore, Back, Style  #libreria para importar los colores.


os.system('cls')  # Limpiar la terminal en Windows
os.system('clear')  # Limpiar la terminal en Linux OS

print(Style.RESET_ALL)  #se elimina cualquier estilo que pueda estar funcionando en la terminal

print(Fore.GREEN + """ 
 ___________________________________________________
|                                                   |
|    ---------𝙢𝙖𝙙𝙚 𝙗𝙮 @𝙖𝙡𝙫𝙖𝙧𝙤𝙖𝙧𝙩𝙖𝙣𝙤--------       |
|       ---------░▒▓█ 𝓥１.０ █▓▒░---------          |
|                                                   |
|___________________________________________________|
""")    #aparece el cuadro de la version y mi nombre en //verde//

print(Style.RESET_ALL)  #se elimina el estilo verde de mi nombre y version


texto = input(Fore.YELLOW + "Introduce something to convert it to ASCII art:  " + Style.RESET_ALL)  #Pregunta al usuario que quiere convertir a ASCII en //amarillo// y elimina todos los estilos




r = requests.get('http://artii.herokuapp.com/make?text=' + texto)   #Se hace la petición al servidor api para devolver el texto en ascii



os.system('cls')  # Limpiar la terminal para windows
os.system('clear')  # Limpiar la terminal en Linux

print(Fore.CYAN + "Here's the result!! ¯\_(ツ)_/¯" + Style.RESET_ALL)   #Avisa de que el resultado está preparado en //cyan// y se elimina cualquier estilo

print(Style.RESET_ALL + r.text)   #Se imprime el texto en ASCII en //blanco//

print("")   #Linea en blanco

result=input(Fore.MAGENTA + "\nDo you want to convert another word? [y/n] > ")
if result=='y':
     os.system('python "text2ascii.py"')
else:
     print(Fore.RED + "\nOk! No problem! See you soon! ")
     print(Fore.YELLOW + "github: https://github.com/alvaroartano")

print(Style.RESET_ALL)
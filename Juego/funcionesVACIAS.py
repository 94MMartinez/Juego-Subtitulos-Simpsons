from principal import *
from configuracion import *
import random
import math



def lectura(archivo, subtitulo,n): #se queda solo con los subtitulo de cierta longitud y filtra
    lineas= archivo.readlines()
    numeroLinea = 1
    guardar = True

    for linea in lineas: #limpia lineas de tiempo
        cont1=0

        if ":" in linea:
            for caracter in linea:
                if caracter == ":":
                    cont1 = cont1+1
                    if cont1 == 4:
                        guardar = False

        if guardar:
            numeroLineaStr = str(numeroLinea)
            if  numeroLineaStr in linea:
                numeroLinea = numeroLinea + 1
                guardar = False

        if guardar and linea != "" and linea != "\n" and "www.argenteam.net" not in linea and "Subtitulos por aRGENTeaM" not in linea:
            #if "<i>" in linea or "</i>" in linea:
            subtitulo.append(linea.replace("<i>","").replace("</i>","").replace("\n",""))

        guardar = True

    return subtitulo


def seleccion(subtitulo):
    #elige uno al azar, lo devuelve, el siguiente y otro
    longitud = len(subtitulo)

    numeroRandom = random.randint(0, longitud-1)
    mostrada = subtitulo[numeroRandom]
    siguiente = subtitulo[numeroRandom +1]
    otra = random.choice(subtitulo)
    while otra.lower() == mostrada.lower() or otra.lower() == siguiente.lower():
        otra = random.choice(subtitulo)

    lista = [mostrada, siguiente,otra]

    return lista

def puntos(n):
    #devuelve el puntaje, segun seguidilla
    return 2**n

def procesar(palabraUsuario, mostrada,siguiente, otra, correctas):
    #chequea que sea correcta, que pertenece solo a la frase siguiente. Devuelve puntaje segun seguidilla
    if palabraUsuario.lower() in siguiente.lower() and palabraUsuario != "":
        return puntos(correctas)
    else:
        return 0
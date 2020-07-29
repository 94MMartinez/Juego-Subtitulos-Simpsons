#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesVACIAS import *



pygame.init()
pygame.mixer.init()

nelson = pygame.mixer.Sound('Nelson.wav')
homero = pygame.mixer.Sound('homero.wav')
select = pygame.mixer.Sound('Select.wav')
street = pygame.mixer.Sound('street.wav')
pygame.mixer.music.load('battletoads.wav')
pygame.mixer.music.play(-1)



#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("T.P(IP)Simpsons")
        screen = pygame.display.set_mode((ANCHO, ALTO))
        ganadores = pygame.image.load('winners-dont-use-drugs.png')
        simps = pygame.image.load('Simps.png')
        screen.blit(ganadores,(0,0))
        pygame.display.flip()

        #Menu de seleccion
        menu=True
        selected="start"

        while menu:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        select.play()
                        selected="start"
                    elif event.key==pygame.K_DOWN:
                        select.play()
                        selected="quit"
                    if event.key==pygame.K_RETURN:
                        if selected=="start":
                            street.play()
                            menu = False
                            pygame.mixer.music.load('8bit.wav')
                            pygame.mixer.music.play(-1)
                        if selected=="quit":
                            pygame.quit()
                            quit()

            # Main Menu UI
            screen.blit(ganadores,(0,0))
            title=text_format("S I M P S O N S U B S", font, 90, yellow)
            if selected=="start":
                text_start=text_format("EMPEZAR", font, 75, white)
            else:
                text_start = text_format("EMPEZAR", font, 75, black)
            if selected=="quit":
                text_quit=text_format("SALIR", font, 75, white)
            else:
                text_quit = text_format("SALIR", font, 75, black)

            title_rect=title.get_rect()
            start_rect=text_start.get_rect()
            quit_rect=text_quit.get_rect()

            # Ajustes texto Menu
            screen.blit(title, (ANCHO/2 - (title_rect[2]/2), 20))
            screen.blit(text_start, (ANCHO/2 - (start_rect[2]/2), 370))
            screen.blit(text_quit, (ANCHO/2 - (quit_rect[2]/2), 420))
            pygame.display.update()




        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial


        puntos = 0
        palabraUsuario = ""

        subtitulo=[]
        correctas=0

        archivo= open("TheSimpsons.srt","r")


        #lectura del archivo y filtrado de caracteres especiales
        lectura(archivo, subtitulo, N)

        #elige unsubtitulo al azar, su siguiente y otro
        lista= seleccion(subtitulo)

        print(lista)

        azar=random.randrange(2)
        dibujar(screen, palabraUsuario, lista, azar, puntos, segundos)

        while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()


            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        #chequea si es correcta y suma o resta puntos
                        sumar=procesar(palabraUsuario, lista[0], lista[1], lista[2],correctas)
                        puntos+=sumar
                        if sumar>0:
                            correctas=correctas+1
                            homero.play()
                        else:
                            correctas=0
                            nelson.play()
                        #elige un subtitulo al azar, su siguiente y otro
                        lista=seleccion(subtitulo)
                        palabraUsuario = ""
                        #cambia el orden al azar
                        azar=random.randrange(2)

            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.blit(simps,(0,0))

            #Dibujar de nuevo todo
            dibujar(screen, palabraUsuario, lista, azar, puntos, segundos)

            pygame.display.flip()

        while 1:
            #Esperar el QUIT del usuario
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

        archivo.close()

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()

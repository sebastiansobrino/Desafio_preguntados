import pygame
from biblioteca import *
from constantes import *
from datos import *

pygame.init() #Se inicializa pygame.
#Inicializamos los contadores que se usaran durante el programa.
contador = 0 
contador_error = 0 
valor_score = 0 
lista_pregunta = generar_lista(lista,"pregunta")
lista_respuesta_a = generar_lista(lista,"a")
lista_respuesta_b = generar_lista(lista,"b")
lista_respuesta_c = generar_lista(lista,"c")
lista_respuesta_correcta = generar_lista(lista,"correcta")
bandera_fin_de_juego = False
bandera_score_final = False
bandera_respuesta_correcta = None
bandera_inicio = None
respuesta_correcta = False

pantalla = pygame.display.set_mode([550, 550]) #Se crea una ventana.

running = True

imagen = pygame.image.load("imagen preguntados.png") #Se carga la imagen. 
imagen = pygame.transform.scale(imagen,(150,150)) #Se cambia la escala de la imagen.

#Generamos los textos que vamos a usar como menu basico para el desarrollo del juego.
reiniciar = generar_texto("Reiniciar", COLOR_NEGRO, (70,20))
pregunta = generar_texto("Pregunta",  COLOR_NEGRO, (70,20))
titulo_score = generar_texto("Score",  COLOR_NEGRO, (70,20))
score = generar_texto("0",  COLOR_NEGRO, (15,15))
desea_continuar = generar_texto("¿Desea volver a empezar?", COLOR_NEGRO,(250,80))
si = generar_texto("Si", COLOR_NEGRO,(50,25))
no =generar_texto("No", COLOR_NEGRO,(50,25))

#Iniciamos la musica que sonara constantemente y le damos un volumen determinado para que no sea molesto.
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
musica = pygame.mixer.Sound("musiquita.wav")
musica.set_volume(0.05)

while running:
# Se verifica si el usuario cerro la ventana.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #Se verifica que el usuario haya dato click en alguna parte de la pantalla. Si Bandera fin de juego es False, significa que el juego ya dio inicio, una vez que el usuario
        #termine, bandera pasa a False y se evalua si el usuario quiere continuar o no.
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            posicion_mouse = list(event.pos)
            
            if bandera_fin_de_juego == False:

                if (posicion_mouse[0] > 200 and posicion_mouse[0] < 330) and (posicion_mouse[1] > 430 and posicion_mouse[1] < 490): #Boton reinicio
                    contador_error = 0
                    contador = 0
                    valor_score = 0
                    bandera_respuesta_correcta = False
                    score = generar_texto(str(valor_score), COLOR_NEGRO, (30,30))
                
                elif (posicion_mouse[0] > 200 and posicion_mouse[0] < 330) and (posicion_mouse[1] > 30 and posicion_mouse[1] < 90): #Boton pregunta
                    if contador_error == 2: 
                        contador = contador + 1
                        contador_error = 0
                    elif bandera_inicio == None:
                        bandera_inicio = True
                        bandera_respuesta_correcta = False
                    else:
                        contador = contador + 1
                        bandera_respuesta_correcta = False  

                elif contador_error < 2 and bandera_respuesta_correcta == False:
                    
                    if (posicion_mouse[0] > 30 and posicion_mouse[0] < 160) and (posicion_mouse[1] > 320 and posicion_mouse[1] < 380):#Boton pregunta A
                        if "a" == lista_respuesta_correcta[contador]:
                            respuesta_correcta = True
                        else:
                            contador_error = contador_error + 1
                    
                    elif (posicion_mouse[0] > 210 and posicion_mouse[0] < 340) and (posicion_mouse[1] > 320 and posicion_mouse[1] < 380):#Boton pregunta B
                        if "b" == lista_respuesta_correcta[contador]:
                            respuesta_correcta = True
                        else:
                            contador_error = contador_error + 1
                    
                    elif (posicion_mouse[0] > 390 and posicion_mouse[0] < 520) and (posicion_mouse[1] > 320 and posicion_mouse[1] < 380):#Boton pregunta C
                        if "c" == lista_respuesta_correcta[contador]:
                            respuesta_correcta = True
                        else:
                            contador_error = contador_error + 1
            
            else:
                
                if (posicion_mouse[0] > 95 and posicion_mouse[0] < 152) and (posicion_mouse[1] > 290 and posicion_mouse[1] < 360): #Boton Si
                    contador = 0
                    bandera_fin_de_juego = False
                    valor_score = 0
                    score = generar_texto(str(valor_score), COLOR_NEGRO, (30,30))
                elif (posicion_mouse[0] > 386 and posicion_mouse[0] < 465) and (posicion_mouse[1] > 290 and posicion_mouse[1] < 360): #Boton No
                    bandera_score_final = True


    
    pantalla.fill((COLOR_BLANCO))# Se pinta el fondo de la ventana.

    pantalla.blit(imagen,(5,5))#Se superpone la imagen cargada por sobre la ventana.

    #Este if maneja si la respuesta es correcta para sumar el contador, aumentar el score y generar el texto con el valor aumentado.
    if respuesta_correcta == True:
        respuesta_correcta = False
        valor_score = valor_score + 10
        score = generar_texto(str(valor_score), COLOR_NEGRO, (30,30))
        bandera_respuesta_correcta = True
        contador_error = 0

    #Usamos el -1 para que la musica funcione en bucle.
    musica.play(-1)

    #En este if/elif/else evaluamos la situacion del juego.S i el contador es igual al len es porque se llego al fin del juego y el usuario debe decidir si continua o no,
    #Si bandera_score_final es True, significa que el usuario no desea jugar mas. En caso contrario a estas dos, el juego corre normalmente.


    if bandera_score_final:
        generar_dibujar_score_final(valor_score,COLOR_NEGRO,pantalla,(200,60),(150, 190))

    elif contador == len(lista_pregunta):
        dibujar_texto(desea_continuar,(150, 190),pantalla) 
        dibujar_texto(si,(100, 300),pantalla) 
        dibujar_texto(no,(400, 300),pantalla) 
        generar_dibujar_score_final(valor_score,COLOR_NEGRO,pantalla,(200,60),(170, 140))
        bandera_fin_de_juego = True
        

    else: 
    
        pygame.draw.rect(pantalla,(COLOR_AMARILLO),(200,30,130,60))
        pygame.draw.rect(pantalla,(COLOR_AMARILLO),(200,430,130,60))

        if contador_error < 2 and bandera_inicio != False and bandera_respuesta_correcta == False: 
            generar_y_dibujar_textos_respuestas_preguntas(lista_respuesta_a,lista_respuesta_b,lista_respuesta_c, lista_pregunta,score,titulo_score, pantalla,contador,COLOR_NEGRO)
        
        elif contador_error == 2 or bandera_respuesta_correcta == True:
            preguntas = generar_texto(lista_pregunta[contador], COLOR_NEGRO, (400,40))
            dibujar_texto(preguntas,(10, 230),pantalla)
            dibujar_texto(score,(200, 170),pantalla) #Se dibuja el texto.
            dibujar_texto(titulo_score,(200, 150),pantalla) #Se dibuja el texto.

        dibujar_texto(reiniciar,(230, 450),pantalla) 
        dibujar_texto(pregunta,(230, 50),pantalla) 
   
    pygame.display.flip()#Actualiza los cambios hechos a cada vuelta que hace.
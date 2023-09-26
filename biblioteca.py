import pygame
from datos import *

def mostrar_dato(dato):
    """ 
    Imprime en pantalla el dato que queremos mostrar.
    Recibe un dato, sea int, float, string, lista o diccioanario.
    No retorna nada.
    """
    print(dato)

def generar_lista(lista:list,clave:str):
    """
    Utiliza una lista de diccionarios accediendo a una clave para guardar los valores en una lista nueva.
    Recibe una lista de diccionarios y una clave.
    Retorna la lista creada.
    """
    if len(lista) != 0:
        lista_generada = []
        for elementos in lista:
            lista_generada.append(elementos[clave])
        return_auxiliar = lista_generada
    else:
        return_auxiliar = -1
    
    return return_auxiliar

def elegir_fuente(fuente:str,size:int):
    """
    Permite seleccionar la fuente que deseamos utilizar para generar nuestros textos.
    Recibe una fuente y el size.
    Retorna la fuente
    """
    fuente = pygame.font.SysFont(fuente, size)
    return fuente

def generar_texto(texto:str,color:tuple,escala:tuple):
    """
    Genera un texto a partir de un Str dandole una escala y renderizandolo.
    Recibe el texto, el color y la escala.
    Retorna el texto generado
    """
    if type(texto) == str and type(color) == tuple and type(escala) == tuple:
        fuente = elegir_fuente("Segoe_UI_Black",50)
        texto_generado = fuente.render(texto, True, (color))
        texto_generado = pygame.transform.scale(texto_generado,escala)
        return_auxiliar = texto_generado
    else:
        return_auxiliar = -1
    
    return return_auxiliar

def dibujar_texto(texto:pygame.surface.Surface,posicion:tuple,pantalla:pygame.surface.Surface):
    """
    Permite dibujar en pantalla el texto.
    Recibe el texto, la posicion de la pantalla y la pantalla en donde queremos que se dibuje
    No retorna nada
    """  
    if type(texto) == pygame.surface.Surface and type(posicion) == tuple and type(pantalla) == pygame.surface.Surface:
        pantalla.blit(texto,posicion)
    else:
        mostrar_dato(-1)

def generar_y_dibujar_textos_respuestas_preguntas(lista_respuesta_a:list,lista_respuesta_b:list,lista_respuesta_c:list, 
                                                  lista_pregunta:list,score:pygame.surface.Surface,titulo_score:pygame.surface.Surface, 
                                                  pantalla: pygame.surface.Surface,contador:int,color:tuple):
    """
    Genera el texto y dibuja en pantalla las preguntas y respuestas de nuestro juego.
    Recibe la lista de pregunta y respuestas, el score, el titulo del escore, la pantalla donde se dibujara, un contador para determinar que pregunta se muestra y el color.
    No retorna nada.
    """
    if len(lista_respuesta_a) != 0 and len(lista_respuesta_b) != 0 and len(lista_respuesta_c) != 0 and len(lista_pregunta) != 0 and type(contador == int):
        if type(pantalla) == pygame.surface.Surface and type(color) == tuple and type(titulo_score) == pygame.surface.Surface and type(score) == pygame.surface.Surface:
            respuesta_a = generar_texto(lista_respuesta_a[contador], color, (100,30))
            respuesta_b = generar_texto(lista_respuesta_b[contador], color, (100,30))
            respuesta_c = generar_texto(lista_respuesta_c[contador], color, (100,30))
            preguntas = generar_texto(lista_pregunta[contador], color, (400,40))
            dibujar_texto(preguntas,(10, 230),pantalla)        
            dibujar_texto(respuesta_a,(30, 320),pantalla)
            dibujar_texto(respuesta_b,(210, 320),pantalla)
            dibujar_texto(respuesta_c,(390, 320),pantalla)
            dibujar_texto(score,(200, 170),pantalla) #Se dibuja el texto.
            dibujar_texto(titulo_score,(200, 150),pantalla) #Se dibuja el texto. 
        else:
            mostrar_dato (-2)
    else:
        mostrar_dato(-1)

def generar_dibujar_score_final(valor_score:int,color:tuple,pantalla:pygame.surface.Surface,escala:tuple,posicion:tuple):
    """
    Genera el texto y dibuja el score final que veremos en pantalla una vez finalizado el juego.
    Recibe el valor del score, el color, la pantalla donde se dibujara, la escala y la posicion.
    No retorna nada. En caso de error, imprime en consola -1
    """
    if type(valor_score) == int and type(posicion) == tuple and type(pantalla) == pygame.surface.Surface and type(color) == tuple and type(escala) == tuple:
        score_final = generar_texto(f"Tu score final es: {str(valor_score)}", color, escala)
        dibujar_texto(score_final,posicion,pantalla) 
    else:
        mostrar_dato("Error")

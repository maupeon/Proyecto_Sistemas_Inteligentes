'''
    Mauricio Peón  A01024162
    Romeo Varela A01020736
    Germán Torres A01651423

'''

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
iteraciones = 5000

#Se asigna la puerta ganadora de forma aleatoria
def puerta_ganadora():
    puerta = random.randint(1, 3)
    return puerta

#Se elige una puerta de forma aleatoria
def eleccion_usuario():
    eleccion = random.randint(1, 3)
    return eleccion

#Se cambia de puerta dependiendo la primera elección y la puerta mostrada por el host
def segunda_eleccion_usuario(primera_eleccion, puerta_g):
    if primera_eleccion == 1:
        if puerta_g != 2:
            eleccion = 3
        else:
            eleccion = 2
    elif primera_eleccion == 2:
        if puerta_g != 1:
            eleccion = 3
        else:
            eleccion = 1
    elif primera_eleccion == 3:
        if puerta_g != 2:
            eleccion = 1
        else:
            eleccion = 2
    return eleccion

#Se itera sobre i juegos siempre cambiando de puerta y guardando el resutado del juego -> 1:Ganado 0:Perdido
def ganadas_dos_elecciones(i,res):
    ganar = 0
    for _ in range(0,i):
        eleccion_u = eleccion_usuario()
        puerta_g = puerta_ganadora()
        eleccion_u2 = segunda_eleccion_usuario(eleccion_u,puerta_g)
        if eleccion_u2 == puerta_g:
            ganar = 1
        else:
            ganar = 0
        res.append(ganar)
    return res

#Se itera sobre i juegos nunca cambiando de puerta y guardando el resutado del juego -> 1:Ganado 0:Perdido
def ganadas_una_eleccion(i,res):
    ganar = 0
    for _ in range(0,i):
        eleccion_u = eleccion_usuario()
        puerta_g = puerta_ganadora()
        if eleccion_u == puerta_g:
            ganar = 1
        else:
            ganar = 0
        res.append(ganar)
    return res

#Simulación del juego sin cambiar de puerta y guardando los promedios de ganados de cada iteración
def Simulacion_sin_cambio():
    promedio_res = []
    eje_y = []
    for i in range(1,iteraciones):
        resultados = []
        resultados = ganadas_una_eleccion(i,resultados)
        promedio_res.append(np.mean(resultados))
        eje_y.append(i)
    #plt.plot(eje_y,promedio_res,label='Sin cambio')
    return resultados

#Simulación del juego cambiando de puerta y guardando los promedios de ganados de cada iteración    
def Simulacion_con_cambio():
    promedio_res = []
    eje_y = []
    for i in range(1,iteraciones):
        resultados = []
        resultados = ganadas_dos_elecciones(i,resultados)
        promedio_res.append(np.mean(resultados))
        eje_y.append(i)
    #plt.plot(eje_y,promedio_res, label = "Con cambio")
    #plt.ylabel('Promedio')
    #plt.legend(bbox_to_anchor=(.85, 1.13), loc='upper left', borderaxespad=0.)
    #plt.xlabel('Veces de Simulación')
    #plt.title("Paradoja Monty Hall")
    #plt.savefig("Paradoja Monty Hall")
    return resultados

def Simulacion():
    print("A continuacion se mostrará una simulación escogiendo una puerta sin cambiar la decisión:\n")
    
    #Se suman todos las veces que se ganó sin cambiar de puerta y se muestra el porcentaje de éxito 
    veces_ganadas_1_eleccion= sum(Simulacion_sin_cambio())
    porcentaje_ganadas = (veces_ganadas_1_eleccion * 100) / iteraciones
    print("Las veces que ganaste sin cambiar la respuesta fue de: {0} veces, sobre: {1} iteraciones.\nGanaste un %{2} de las veces.".format(veces_ganadas_1_eleccion,iteraciones,porcentaje_ganadas))

    print("\nA continuacion se mostrará una simulación escogiendo una puerta cambiando la decisión:\n")

    #Se suman todos las veces que se ganó cambiando de puerta y se muestra el porcentaje de éxito  
    veces_ganadas_2_elecciones = sum(Simulacion_con_cambio())
    porcentaje_ganadas = (veces_ganadas_2_elecciones * 100) / iteraciones
    print("Las veces que ganaste cambiando la respuesta fue de: {0} veces, sobre: {1} iteraciones.\nGanaste un %{2} de las veces.".format(veces_ganadas_2_elecciones,iteraciones,porcentaje_ganadas))

  
if __name__ == "__main__":
    print('***********************************************************\n')
    print('Bienvenido a la simulación de la Paradoja de Monty Hall.\n')
    print('***********************************************************\n')

    Simulacion()

    print("\nEn el archivo 'Paradoja Monty Hall.png' se pueden ver dos gráficas comparativas.")

    print("\nViendo ambas opciones, la mejor decisión es cambiar la puerta una vez que se te muestre otra donde no está el premio.\n")

    

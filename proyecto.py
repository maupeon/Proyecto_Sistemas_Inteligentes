import random

iteraciones = 1000000

def puerta_ganadora():
    num = random.randint(0, 99)
    if num >= 0 and num < 33:
        puerta = 1
    elif num >= 33 and num < 66:
        puerta = 2
    elif num >= 66 and num < 100:
        puerta = 3
    return puerta

def eleccion_usuario():
    num = random.randint(0, 99)
    if num >= 0 and num < 33:
        eleccion = 1
    elif num >= 33 and num < 66:
        eleccion = 2
    elif num >= 66 and num < 100:
        eleccion = 3
    return eleccion

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

def ganadas_dos_elecciones():
    veces_ganadas = 0
    for _ in range(0,iteraciones):
        eleccion_u = eleccion_usuario()
        puerta_g = puerta_ganadora()
        eleccion_u2 = segunda_eleccion_usuario(eleccion_u,puerta_g)
        if eleccion_u2 == puerta_g:
            veces_ganadas+=1
    return veces_ganadas

def ganadas_una_eleccion():
    veces_ganadas = 0
    for _ in range(0,iteraciones):
        eleccion_u = eleccion_usuario()
        puerta_g = puerta_ganadora()
        if eleccion_u == puerta_g:
            veces_ganadas+=1
    return veces_ganadas

#print("Bienvenido a la catafixia.")
#print("En una de las 3 puertas hay un coche, en las otras 2 hay ovejas.")

veces_ganadas_2_elecciones = ganadas_dos_elecciones()
porcentaje_ganadas = (veces_ganadas_2_elecciones * 100) / iteraciones
print("Las veces que ganaste cambiando la respuesta fue de: {0} sobre: {1} iteraciones.\nGanaste un %{2} de las veces.".format(veces_ganadas_2_elecciones,iteraciones,porcentaje_ganadas))

veces_ganadas_1_eleccion= ganadas_una_eleccion()
porcentaje_ganadas = (veces_ganadas_1_eleccion * 100) / iteraciones
print("Las veces que ganaste sin cambiar la respuesta fue de: {0} sobre: {1} iteraciones.\nGanaste un %{2} de las veces.".format(veces_ganadas_1_eleccion,iteraciones,porcentaje_ganadas))

#try:
 #   choose=int(input('¿Cuál escoges?\n1,2,3\nElección: '))
#except ValueError:
 #   print("Not a number")


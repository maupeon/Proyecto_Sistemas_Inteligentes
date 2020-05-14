import random

iteraciones = 1000000

def puerta_ganadora():
    puerta = random.randint(1, 3)
    return puerta

def eleccion_usuario():
    eleccion = random.randint(1, 3)
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



def decision(message):
    while True:
        try:
            print("")
            dec = int(input(message))
        except ValueError:
            print("Escoge un numero.")
            continue
        else:
            return dec


if __name__ == "__main__":

    veces_ganadas_2_elecciones = ganadas_dos_elecciones()
    porcentaje_ganadas = (veces_ganadas_2_elecciones * 100) / iteraciones
    print("Las veces que ganaste cambiando la respuesta fue de: {0} sobre: {1} iteraciones.\nGanaste un %{2} de las veces.".format(veces_ganadas_2_elecciones,iteraciones,porcentaje_ganadas))

    veces_ganadas_1_eleccion= ganadas_una_eleccion()
    porcentaje_ganadas = (veces_ganadas_1_eleccion * 100) / iteraciones
    print("Las veces que ganaste sin cambiar la respuesta fue de: {0} sobre: {1} iteraciones.\nGanaste un %{2} de las veces.".format(veces_ganadas_1_eleccion,iteraciones,porcentaje_ganadas))



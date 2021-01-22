# Universidad Metropolitana
# Departamento de Ingeniería de Sistemas
# Modelación de Sistemas de Redes
# Prof. Rafael Matienzo

# Programa que implementa el Algoritmo de Dijkstra. 
# Aplicado al Proyecto 1 - Cámino Más Corto - Javier y Andreina de Modelación de Sistemas de Redes. 

# Grupo E.
# Integrantes: 
#   - Miguel Jaimes
#   - Valeria Madio
#   - Gilberto Pucciarelli 
#   - Vito Tatoli
#   - Luis Torres


from os import system, name 
import ssl
import sys
import time
import numpy as np
import datetime
import pandas as pd
import csv
import copy


def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')



from os import system, name 


calles = {
    0: 'Calle 55 Carrera 15', 1: 'Calle 55 Carrera 14', 2: 'Calle 55 Carrera 13', 3: 'Calle 55 Carrera 12', 4: 'Calle 55 Carrera 11', 5: 'Calle 55 Carrera 10', 
    6: 'Calle 54 Carrera 15', 7: 'Calle 54 Carrera 14', 8: 'Calle 54 Carrera 13', 9: 'Calle 54 Carrera 12', 10: 'Calle 54 Carrera 11', 11: 'Calle 54 Carrera 10', 
    12: 'Calle 53 Carrera 15', 13: 'Calle 53 Carrera 14', 14: 'Calle 53 Carrera 13', 15: 'Calle 53 Carrera 12', 16: 'Calle 53 Carrera 11', 17: 'Calle 53 Carrera 10', 
    18: 'Calle 52 Carrera 15', 19: 'Calle 52 Carrera 14', 20: 'Calle 52 Carrera 13', 21: 'Calle 52 Carrera 12', 22: 'Calle 52 Carrera 11', 23: 'Calle 52 Carrera 10', 
    24: 'Calle 51 Carrera 15', 25: 'Calle 51 Carrera 14', 26: 'Calle 51 Carrera 13', 27: 'Calle 51 Carrera 12', 28: 'Calle 51 Carrera 11', 29: 'Calle 51 Carrera 10', 
    30: 'Calle 50 Carrera 15', 31: 'Calle 50 Carrera 14', 32: 'Calle 50 Carrera 13', 33: 'Calle 50 Carrera 12', 34: 'Calle 50 Carrera 11', 35: 'Calle 50 Carrera 10' 
}


def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear')


def dijkstra(graph, persona):
    
    table = []
    for filas in range(len(graph)):
        row = []
        row.append(filas)
        row.append(999)
        row.append(" ")
        row.append(False)
        table.append(row)
    
   
        
    table[persona][1] = 0
    # print('Tabla antes de realizar el algoritmo de Dijkstra: ')
    # print(*table, sep="\n")
    # print('\n')
    
    
    # Mientras haya nodos sin visitar, itere:
    for filas in range(len(table)):
        while table[filas][3] == False:
            
            # Visite el nodo no visitado que tenga la menor distancia conocida al nodo de inicio
            minimo = 999
            node = 0
            for i in range(len(table)):
                if table[i][1] <= minimo and table[i][3] == False:
                    node = i
                    minimo = table[i][1]

            # Para el nodo que está visitando, examine sus nodos adyacentes no visitados
            for j in range(len(graph[node])):

                # Si la distancia calculada para un vecino es menor que la que figuraba en la tabla entonces
                if table[j][3] == False and graph[node][j] != 0:
                    dist = minimo + graph[node][j]
                    
                    if dist <= table[j][1]: 
                        # Actualice la distancia mínima en la tabla
                        table[j][1] = dist
                        
                        # Actualice el predecesor en la tabla
                        table[j][2] = node

            # Marque el nodo que está visitando como visitado (rojo, o sea cuarta columna inicializada a TRUE)
            table[node][3] = True

    

    # print('Tabla luego de realizar el algoritmo de Dijkstra: ')
    # print(*table, sep="\n")
    # print('\n')
    return table


def camino(table, start, end):

    cadena, esteNodo = calles[end],end
    ruta = [end]
    minutos = 0
    primeraI = True
     # guardando minutos que tarda en llegar hasta el destino
    minutos = table[esteNodo][1]
    while esteNodo != start:
        esteNodo = table[esteNodo][2]
        cadena = calles[esteNodo] + ' - ' + cadena
        ruta.append(esteNodo)
    
    ruta.reverse()
    print("Camino a seguir:")
    print(cadena)
    print(ruta)
    return ruta, minutos


def multiplesCaminos(matriz, end ,start,persona):
    multiples=True
    datos=[]
    ady=copy.deepcopy(matriz)
    while multiples==True:
        row=[]
        #busqueda de camino
        print("Resultados de la iteracion "+str(len(datos)+1)+ " de "+ persona)
        table = dijkstra(ady, start)
        way, minutos = camino(table, start, end)
        row.append(way)
        row.append(minutos)
        print("El tiempo del camino de esta iteracion es: "+str(row[1]))
        if len(datos)==0:
            #Guardar resultados de la primera corrida
            datos.append(row)
            #Quitar camino de la matriz de adyacencia
            print("Se elimina el camino de esta iteracion de la matriz de adyacencia")
            ady=quitarCamino(way,ady,start,end)
        else:
            #Comparar con el tiempo del ultimo camino hallado
            if datos[-1][1]==row[1]:
                #Si son iguales guarda y se continua buscando
                datos.append(row)
                #Quitar camino de la matriz de adyacencia
                print("Se elimina el camino de esta iteracion de la matriz de adyacencia")
                ady=quitarCamino(way,ady,start,end)
            else:
                print("Como es mayor al anterior se para de buscar ")
                #Si no lo son Se termina de buscar
                multiples=False
        print("Presione enter para continuar")
        input()
        print("\n")
    return datos


def quitarCamino(camino, matriz,start,end):
    way=camino.copy()
    way.remove(start)
    way.remove(end)
    #Quitar un camino del grafo
    for item in way:
            for i in range(0,len(matriz)):
                if i==item:
                    for j in range(0,len(matriz[i])):
                        matriz[i][j]=0
                matriz[i][item]=0
    return matriz


def armarMapa(matriz):
    aux=0
    puntos=[]
    #Mostrar los nodos que estan disponibles en base a una Matriz de adyacencia
    for i in range(0,6):
        row=[]
        for j in range(0,6):
            next=999
            for k in range(len(matriz)):
                if matriz[k]==aux:
                    next=aux
            row.append(next)
            aux=aux+1
        puntos.append(row)

    for i in range(0,6):
        row=" "
        for j in range(0,6):
            if puntos[i][j]==999:
                aux="-"
            else:
                if puntos[i][j]<10:
                    aux="  -"
                else:
                    aux=" -"
            row=row+str(puntos[i][j])+aux
        print(row)


def compararCaminos(camino1, camino2):
    resultado=False
    for i in range(0,len(camino1)-1):
        for j in range(0,len(camino2)-1):
            if camino2[j]== camino1[i]:
                resultado=True
                break
    return resultado


def main():  
    graph=[]
    cudricula=[]  
    count=0
    #Armar matriz que representa las intersecciones con un numero de identificacion
    for i in range(0,6) :
        row=[]
        for j in range(0,6):
            row.append(count)
            count=count+1
        cudricula.append(row)

    #Armar matriz de Adyacencia Vacia
    for i in range(0,36) :
        row=[]
        for j in range(0,36):
            row.append(0)
        graph.append(row)
    print("Nodos presentes")
    print(*cudricula, sep="\n")    
    
    #LLenado de matriz de adyacencia en base a los datos del enunciado
    for i in range(0,6) :
        for j in range(0,6):
            #con el numero del nodo se identifica la fila en la matriz
            fila=cudricula[i][j]
            #Se agregan los pesos con nodos adyacentes que estos indican
            # la columna en la matriz de adyacencia
            w=5
            if j==2 or j==3 or j==4:
                w=7 #Peso para las carreras 13,12 y 11
            #Se verifican los nodos adyacentes
            if i+1<6:
                col=cudricula[i+1][j]
                graph[fila][col]=w
            if i-1>=0:
                col=cudricula[i-1][j]
                graph[fila][col]=w
            w=5
            if i==4:
                w=10 #Peso para la calle 51
            if j+1<6:
                col=cudricula[i][j+1]
                graph[fila][col]=w
            if j-1>=0:
                col=cudricula[i][j-1]
                graph[fila][col]=w
            
    # print(*graph, sep="\n")

    destination = None
    while destination == None:
        try:
            destination = int(input(
            '''Indique (ingresando el número de la opción) el establecimiento donde se desean encontrar Javier y Andreína: 
                    1. Discoteca The Darkness : Carrera 14 con Calle 50.
                    2. Bar La Pasión: Calle 54 con Carrera 11.
                    3. Cervecería Mi Rolita: Calle 50 con Carrera 12.
            '''))
        except:
            print("No coloco una opción válida")
            destination = None
    
    if destination == 1:
        end=31
    elif destination == 2:
        end=10
    else:
        end=33

    
    #Buscar Multiples caminos minimos de cada uno 
    print("Se hallan los caminos minimos que puede tener Andreina")
    CaminosA=multiplesCaminos(graph,end,20,"Andreina")
    print("Caminos de igual tiempo minimo de Andreina")
    print(*CaminosA, sep="\n")
    print("Presione enter para continuar")
    input()


    print("Luego los caminos de Javier")
    print("\n")
    CaminosJ=multiplesCaminos(graph,end,7,"Javier")
    print("Caminos de igual tiempo minimo de Javier")
    print(*CaminosJ, sep="\n")
    print("Presione enter para continuar")
    input()
    print("\n\n\n")
    
    print("Se comparan los caminos que tiene cada uno disponibles:")
    javier=[]
    andreina=[]
    #Comparar los caminos resultantes
    # para verificar si coinciden en algun punto o no 
    for i in range(len(CaminosA)):
        for j in range(len(CaminosJ)):
            result=compararCaminos(CaminosA[i][0],CaminosJ[j][0])
            if result==False:
                andreina=CaminosA[i]
                javier=CaminosJ[j]
                break
            else:
                andreina=CaminosA[i]
                javier=CaminosJ[j]
    print("Seleccionados:")
    print(javier)
    print(andreina)           
    #Si los caminos resultantes de la comparacion coinciden 
    #se elige el que tenga menor 
    #tiempo y se elimina de la matriz de adyacencia 
    if result==True:
        print("\n\n")
        print("Como coinciden en sus ruta sin tener alternativas, se vuelve a calcular una ruta para el que tenga menor tiempo")
        ady=copy.deepcopy(graph)
        if andreina[1]<javier[1]:
            print("Andreina teniendo el menor tiempo, se calcula una ruta alterna")
            print("Se elimina la ruta actual de la matriz y se vuelve a buscar un camino")
            ady=quitarCamino(javier[0],ady,7,end)
            table = dijkstra(ady, 20)
            andreina[0], andreina[1] = camino(table, 20, end)
        elif javier[1]< andreina[1]:
            print("Javier teniendo el menor tiempo, se calcula una ruta alterna")
            print("Se elimina la ruta actual de la matriz y se vuelve a buscar un camino")
            ady=quitarCamino(andreina[0],ady,7,end)
            table = dijkstra(ady, 20)
            javier[0], javier[1] = camino(table, 20, end)
        print("Seleccionados:")
        print(javier)
        print(andreina)

    print("Presione enter para continuar")
    input()
    print("\n\n\n")
    

    #Mostrar todos los de cada uno en una matriz 6x6
    #que representan las intersecciones 
    first_list = javier[0].copy()
    second_list = andreina[0].copy()

    in_first = set(first_list)
    in_second = set(second_list)

    in_second_but_not_in_first = in_second - in_first
    result = first_list + list(in_second_but_not_in_first)
    print("Todas las Intersecciones ") 
    print(result)
    armarMapa(result)
    print("\n")

    # Mostrar el camino que debe de seguir cada uno para llegar al destino
    print('El camino que debe seguir Andreina es: ')
    for nodes in andreina[0]:
        for key, value in calles.items():
            if nodes == key:
                print(calles[key])
    print("\n")

    print('El camino que debe seguir Javier es: ')
    for nodes in javier[0]:
        for key, value in calles.items():
            if nodes == key:
                print(calles[key])
    print("\n")

    # Mostrar si uno tiene que salir antes que el otro para llegar al mismo tiempo al destino
    if javier[1] < andreina[1]:
        print('Andreina tarda en llegar al destino {} minutos'.format(andreina[1]))
        print('Javier tarda en llegar al destino {} minutos'.format(javier[1]))
        print('Andreina debe salir {} minuto/s antes que Javier, para que ambos lleguen al mismo tiempo al destino.'.format(andreina[1] - javier[1]))
    
    elif andreina[1] < javier[1]:
        print('Andreina tarda en llegar al destino {} minutos'.format(andreina[1]))
        print('Javier tarda en llegar al destino {} minutos'.format(javier[1]))
        print('Javier debe salir {} minuto/s antes que Andreina, para que ambos lleguen al mismo tiempo al destino.'.format(javier[1] - andreina[1]))
    
    else:
        print('Andreina tarda en llegar al destino {} minutos'.format(andreina[1]))
        print('Javier tarda en llegar al destino {} minutos'.format(javier[1]))
        print('Andreina y Javier llegan al destino al mismo tiempo')
    print("\n")


if __name__ == "__main__":
    main()
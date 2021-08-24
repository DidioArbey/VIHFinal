import random as ran
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


N=10
edad=[]
sigmaFinal=[]

# FUNCIONES
def infectadoinicial(G):  #crear infectado
    inf=ran.randint(0,N)  #inf-> infectado y saca un numero aleatorio entre 0 y N
    G.nodes[inf]['Estado']='I'
    return G, inf


def hallarpareja(inf):
    if ran.choice(['si', 'no']) == 'si':
        print('el infectado', inf, ' si se va a emparejar')
        vecinos=[]
        for i in range(N):
            if G.has_edge(i,inf):
                vecinos=vecinos+[i]
        print('las posibles parejas del nodo infectado', inf, '  son: ', vecinos)
        pareja=ran.choice(vecinos)
        print('la pareja del infectado', inf, '  va a ser el nodo: ', pareja)
        riesgo=np.random.rand()#edades para el riesgo y sus rangos de probabilidad
        #ries=rangoedades()
        print('el riesgo de infeccion es: ', riesgo)
        if riesgo > 0.5 :
            #if de random para si o no se infecta basado en la probabilidad
            G.nodes[pareja]['Estado']='I'
            print('el nodo ', pareja, 'se infecto')
        else:
            print('el nodo', pareja, 'no se infecto')
    else:
        print('el infectado', inf, '  no se va a emparejar')


def rangoedades():
    for i in range (N):
        edad.append(ran.randint(0, 75))#75 ya qyue es la esperanza de vida que hay en colombia
        print (f"la edad del nodo {i+1} es de {edad[i]} ")
        if edad[i] >= 0 and edad[i] <=14:
            sigma=ran.randint(10, 20)
            alpha=0.005
            beta=ran.uniform(0, 0.002)
            R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
            print(f"su s {sigma} a {alpha} b {beta} R0 {R0} ")
            return riesgo=np.random.rand(0,0.6)

        elif edad[i] > 14 and edad[i] <=24:
            sigma=ran.randint(8, 15)
            alpha=0.005
            beta=ran.uniform(0, 0.002)
            R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
            print(f"su s {sigma} a {alpha} b {beta} R0 {R0} ")
        elif edad[i] > 24 and edad[i] <=49:
            sigma=ran.randint(5, 10)
            alpha=0.005
            beta=ran.uniform(0, 0.002)
            R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
            print(f"su s {sigma} a {alpha} b {beta} R0 {R0} ")
        elif edad[i] > 50 and edad[i] <=100:
            sigma=ran.randint(0, 5)
            alpha=0.005
            beta=ran.uniform(0, 0.002)
            R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
            print(f"su s {sigma} a {alpha} b {beta} R0 {R0} ")

#VARIABLES
#G = nx.scale_free_graph(N) #Crear el grafo sin escala del tamaño N
G = nx.erdos_renyi_graph(N,0.2)
#EN EL GRAFO DARLES ESTADO SUSCEPTIBLE
for i in range(N):
    G.nodes[i]['Estado']='S'

#COLOR A LOS NODOS
color_map={'S': 'green', 'I': 'red'}

#FORMA DEL GRAFO
pos=nx.circular_layout(G)

#INICIALISAMOS LA FUNCION
G,inf=infectadoinicial(G)

#DIBUJAR EL GRAFO
nx.draw(G,pos,node_color=[color_map[G.nodes[node]['Estado']] for node in G], node_size = 100)
plt.show()

#ITERACIONES PARA HALLAR PAREJAS
n=20 #numero de iteraciones
for i in range(n):
    print('iteracion: ', i)
    for j in range(N):
        if G.nodes[j]['Estado']=='I':
            hallarpareja(j)
    nx.draw(G,pos,node_color=[color_map[G.nodes[node]['Estado']] for node in G], node_size = 100)
    plt.show()

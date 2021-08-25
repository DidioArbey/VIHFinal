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

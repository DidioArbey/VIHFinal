# librerías
import networkx as nx
import matplotlib.pyplot as plt
import random as ran
import numpy as np
#---------------------------------------------------------------------------

N=10
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
        print('el riesgo de infeccion es: ', riesgo)
        if riesgo > 0.5 :
            G.nodes[pareja]['Estado']='I'
            print('el nodo ', pareja, 'se infecto')
        else:
            print('el nodo', pareja, 'no se infecto')
    else:
        print('el infectado', inf, '  no se va a emparejar')


#---------------------------------------------------------------------------

G = nx.erdos_renyi_graph(N,0.2)
for i in range(N):
    G.nodes[i]['Estado']='S'

color_map={'S': 'green', 'I': 'red'}
#plt.figure(num=None, figsize=(8, 6), dpi=80)
pos=nx.circular_layout(G)
#nx.draw(G,pos,node_size = 100,)
#plt.show()

#---------------------------------------------------------------------------

G,inf=infectadoinicial(G)
nx.draw(G,pos,node_color=[color_map[G.nodes[node]['Estado']] for node in G], node_size = 100)
plt.show()


n=20 #numero de iteraciones
for i in range(n):
    print('iteracion: ', i)
    for j in range(N):
        if G.nodes[j]['Estado']=='I':
            hallarpareja(j)
    nx.draw(G,pos,node_color=[color_map[G.nodes[node]['Estado']] for node in G], node_size = 100)
    plt.show()

# Graph.neighbors():	Return an iterator over all neighbors of node n.
# Graph.number_of_edges([u, v]): Return the number of edges between two nodes.
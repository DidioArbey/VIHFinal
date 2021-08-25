# librerías
import networkx as nx
import matplotlib.pyplot as plt
import random as ran
import numpy as np
from random import uniform
#---------------------------------------------------------------------------

#I=infectado
#S=susceptible
#---------------------------------------------------------------------------

N=10 #numero de la poblacion
e1=np.linspace(0,1,500)                                             #efectividad de la terapia 1
e2=np.linspace(0,1,500)                                             #efectividad de la terapia 2
Neta=14                                                             #produccion viral
u=1                                                                 #proporcion de la terapia
mu=0.005                                                            #tasa de muerte natural de las celulas T no infectadas
#beta=0.000025                                                       #tasa de infeccion ###cambia por edad
#sigma=10                                                            #construccion constante de celulas T ### cambia por edad
c=0.24                                                              #tasa de eliminacion del virus ##posible edad
# alpha=0.005                                                         #muerte poblacional sitotoxica


#-----------------CALCULA EL Ro DE CADA NODO
def Ro(e1, e2,beta,Neta,sigma):
    R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
    return R0

#-----------------crear primer nodo infectado
def infectadoinicial(G):  #crear infectado
    inf=ran.randint(0,N)  #inf-> infectado y saca un numero aleatorio entre 0 y N
    G.nodes[inf]['Estado']='I'
    return G, inf

#--------------- sigma y beta de edades
def rangoedades():
    edad=[]
    # diccionarios=dict()
    for i in range (N):
        edad.append(ran.randint(0, 75))#75 ya qyue es la esperanza de vida que hay en colombia
        if edad[i] >= 0 and edad[i] <=14:
            beta=uniform(0,0.00005)
            sigma=ran.randint(0, 20)
            alpha=uniform(0,0.003)
            lista=(sigma,beta,alpha)
            return lista
        elif edad[i] > 14 and edad[i] <=24:
            beta=uniform(0,0.00005)
            sigma=ran.randint(0, 20)
            alpha=uniform(0,0.003)
            lista=(sigma,beta,alpha)
            return lista
        elif edad[i] > 24 and edad[i] <=49:
            beta=uniform(0,0.00005)
            sigma=ran.randint(0, 20)
            alpha=uniform(0,0.003)
            lista=(sigma,beta,alpha)
            return lista
        elif edad[i] > 50 and edad[i] <=100:
            beta=uniform(0,0.00005)
            sigma=10
            alpha=uniform(0,0.003)
            lista=(sigma,beta,alpha)
            return lista

#--------------------hallar parejas

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


#Encontrar los nodos infectados en la red

def FindInfected(G):
    NoInfectadosST = 0
    NoInfectadosCT = 0         ########         NTI=numero total de infectados
    NoSusceptibles = 0
    for i in range(N):
        if (G.nodes[i]["V"]) > 0.0:
            G.nodes[i]['Ro'] = Ro(e1[i],e2[i],beta[i],Neta[i],sigma[i])
            if G.nodes[i]["Estado"] == 'Ct':
                NoInfectadosCT +=1
                PAT=uniform(0,1) #probabilidad de abandonar tto
                if PAT<0.2:
                    G.nodes[i]["Estado"] = 'St'
                    e1[i]=0
                    e2[i]=0
                    NoInfectadosST +=1
                    NoInfectadosCT -=1
            else:
                NoInfectadosST +=1
                if G.nodes[i]["T"]<350: #probabilidad de inciar tto
                    G.nodes[i]["Estado"] = 'Ct'
                    e1[i]=uniform(0,1)
                    e2[i]=uniform(0,1)
                    NoInfectadosCT +=1
                    NoInfectadosST -=1
        NoSusceptibles = N-(NoInfectadosCT+NoInfectadosST)
    return NoInfectadosST, NoInfectadosCT, NoSusceptibles

#---------------------------------------------------------------------------
prue=rangoedades()


beta=prue[1]
sigma=prue[0]
alpha=prue[2]
R0=Ro(e1,e2,beta,Neta,sigma)


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
import networkx as nx
import matplotlib.pyplot as plt
import random as ran
import numpy as np
from random import uniform


N=100 #numero de la poblacion
e1=uniform(0,1)                                             #efectividad de la terapia 1
e2=uniform(0,1)                                             #efectividad de la terapia 2
Neta=14                                                             #produccion viral
u=1                                                                 #proporcion de la terapia
mu=0.005
c=0.24
edad=[]
edad.append(ran.randint(0, 75))



def riesgo(edad):
    for i in range (N):
        if edad[i] >= 0 and edad[i] <=14:
            ries=uniform(0,1)
            return ries
        elif edad[i] > 14 and edad[i] <=24:
            ries=uniform(0,1)
            return ries
        elif edad[i] > 24 and edad[i] <=49:
            ries=uniform(0,1)
            return ries
        elif edad[i] > 50 and edad[i] <=100:
            ries=uniform(0,1)
            return ries






# diccio={edad[i]:pruebas()}
def rangoedades(edad):
    # edad=[]
    # diccionarios=dict()
    for i in range (N):
        edad.append(ran.randint(0, 75))#75 ya qyue es la esperanza de vida que hay en colombia
        if edad[i] >= 0 and edad[i] <=14:
            beta=uniform(0,0.00005)
            sigma=ran.randint(0, 20)
            alpha=uniform(0,0.003)
            lista=(edad[i],sigma,beta,alpha)
            return lista
        elif edad[i] > 14 and edad[i] <=24:
            beta=uniform(0,0.00005)
            sigma=ran.randint(0, 20)
            alpha=uniform(0,0.003)
            lista=(edad[i],sigma,beta,alpha)
            return lista
        elif edad[i] > 24 and edad[i] <=49:
            beta=uniform(0,0.00005)
            sigma=ran.randint(0, 20)
            alpha=uniform(0,0.003)
            lista=(edad[i],sigma,beta,alpha)
            return lista
        elif edad[i] > 50 and edad[i] <=100:
            beta=uniform(0,0.00005)
            sigma=10
            alpha=uniform(0,0.003)
            lista=(edad[i],sigma,beta,alpha)
            return lista


def Ro(e1, e2,beta,Neta,sigma):
    R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
    return R0

#-----------------crear primer nodo infectado
def infectadoinicial(G):  #crear infectado
    inf=ran.randint(0,N)  #inf-> infectado y saca un numero aleatorio entre 0 y N
    G.nodes[inf]['Estado']='I'
    return G, inf



prue=rangoedades()

edad=prue[0]
sigma=prue[1]
beta=prue[2]
alpha=prue[3]
R0=Ro(e1,e2,beta,Neta,sigma)
# print(R0)
for i in range (N):
    prue=rangoedades()
    edad=prue[0]
    sigma=prue[1]
    beta=prue[2]
    alpha=prue[3]
    R0=Ro(e1,e2,beta,Neta,sigma)
    print(edad, sigma, beta, alpha,R0)




    # print(sigmas) #sigmas,betas,alphas
    # print()
    # print(betas) #sigmas,betas,alphas
    # print()
    # print(alphas) #sigmas,betas,alphas
# for i in range (N):
#     diccio={edad[i]:pruebas()}
#     print(f'datos del nodo: {diccio}')

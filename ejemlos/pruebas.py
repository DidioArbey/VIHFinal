import networkx as nx
import matplotlib.pyplot as plt
import random as ran
import numpy as np
from random import uniform
import pprint


N=10



# diccio={edad[i]:pruebas()}
def pruebas():
    edad=[]
    diccionarios=dict()
    # sigmas=[]
    # betas=[]
    # alphas=[]
    for i in range (N):
        edad.append(ran.randint(0, 75))#75 ya qyue es la esperanza de vida que hay en colombia
        # print (f"la edad del nodo {i+1} es de {edad[i]} ")
        if edad[i] >= 0 and edad[i] <=14:
            # betas.append(uniform(0,0.00005))
            # sigmas.append(uniform(0,20))
            # alphas.append(uniform(0,0.003))
            beta=uniform(0,0.00005)
            sigma=ran.randint(0, 20)
            alpha=uniform(0,0.003)
            dicionario={edad[i]:(sigma,beta,alpha)}
            # return dicionario

        elif edad[i] > 14 and edad[i] <=24:
            beta=uniform(0,0.00005)
            # sigma=ran.randint(0, 20)
            alpha=uniform(0,0.003)
            dicionario={edad[i]:(beta,alpha)}
            # return dicionario

        elif edad[i] > 24 and edad[i] <=49:
            beta=uniform(0,0.00005)
            sigma=ran.randint(0, 20)
            alpha=uniform(0,0.003)
            dicionario={edad[i]:(sigma,beta,alpha)}
            # return dicionario

        elif edad[i] > 50 and edad[i] <=100:
            beta=uniform(0,0.00005)
            sigma=10
            alpha=uniform(0,0.003)
            dicionario={edad[i]:(sigma,beta,alpha)}
            # return dicionario
        diccionarios.update(dicionario)
    return diccionarios

pprint.pprint(pruebas())




    # print(sigmas) #sigmas,betas,alphas
    # print()
    # print(betas) #sigmas,betas,alphas
    # print()
    # print(alphas) #sigmas,betas,alphas
# for i in range (N):
#     diccio={edad[i]:pruebas()}
#     print(f'datos del nodo: {diccio}')

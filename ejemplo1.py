#librerias
import random as ran

from numpy.lib.function_base import append


# variables
diccionario=dict
mu=0.005
edad=[]
sigmaFinal=[]
N=5
Neta=14
u=1
c=0.24
e1=ran.random()
e2=ran.random()

#funciones



for i in range (N):
    edad.append(ran.randint(0, 75))#75 ya qyue es la esperanza de vida que hay en colombia
    # print (f"la edad del nodo {i+1} es de {edad[i]} ")
    if edad[i] >= 0 and edad[i] <=14:
        sigma=ran.randint(10, 20)
        alpha=0.005
        beta=ran.uniform(0, 0.002)
        R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
        sigmaFinal.append(R0)
        # return sigma
        # print(f"su s {sigma} a {alpha} b {beta} R0 {R0} ")
    elif edad[i] > 14 and edad[i] <=24:
        sigma=ran.randint(8, 15)
        alpha=0.005
        beta=ran.uniform(0, 0.002)
        R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
        sigmaFinal.append(R0)
        # return sigma
        # print(f"su s {sigma} a {alpha} b {beta} R0 {R0} ")
    elif edad[i] > 24 and edad[i] <=49:
        sigma=ran.randint(5, 10)
        alpha=0.005
        beta=ran.uniform(0, 0.002)
        R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
        sigmaFinal.append(R0)
        # return sigma
        # print(f"su s {sigma} a {alpha} b {beta} R0 {R0} ")
    elif edad[i] > 50 and edad[i] <=100:
        sigma=ran.randint(0, 5)
        alpha=0.005
        beta=ran.uniform(0, 0.002)
        R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
        sigmaFinal.append(R0)
        # return sigma
    # print (edad[i])
print(f'la edad de cada nodo es {edad}')
print(f'el sigma para cada edad es de {sigmaFinal}')



def Ro(e1, e2,beta,Neta,sigma): #######################  CALCULA EL Ro DE CADA NODO
    R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
    #R0 = beta*Neta*sigma*(1-e1)*(1-e2)/(c*mu)
    return R0
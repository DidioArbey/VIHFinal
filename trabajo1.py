import random as ran
import numpy as np
# print(random.randint(0, 100))
# mu=0.005
# c=0.24
# delta=0.26
# alpha=0.005
# beta=0.000025
# sigma=10
# u=1
e1=ran.random()

e2=ran.random()



mu=0.005
# edad=[]
N=5
Neta=14
u=1
c=0.24

# sigma=9
# alpha=0.002
# beta=0.0005




def prueba():
    edad=[]
    for i in range (N):
        edad.append(ran.randint(0, 75))#75 ya qyue es la esperanza de vida que hay en colombia
        # print (f"la edad del nodo {i+1} es de {edad[i]} ")
        if edad[i] >= 0 and edad[i] <=14:
            sigma=ran.randint(10, 20)
            alpha=0.005
            beta=ran.uniform(0, 0.002)
            R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
            return sigma
            # print(f"su s {sigma} a {alpha} b {beta} R0 {R0} ")
        elif edad[i] > 14 and edad[i] <=24:
            sigma=ran.randint(8, 15)
            alpha=0.005
            beta=ran.uniform(0, 0.002)
            R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
            return sigma
            # print(f"su s {sigma} a {alpha} b {beta} R0 {R0} ")
        elif edad[i] > 24 and edad[i] <=49:
            sigma=ran.randint(5, 10)
            alpha=0.005
            beta=ran.uniform(0, 0.002)
            R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
            return sigma
            # print(f"su s {sigma} a {alpha} b {beta} R0 {R0} ")
        elif edad[i] > 50 and edad[i] <=100:
            sigma=ran.randint(0, 5)
            alpha=0.005
            beta=ran.uniform(0, 0.002)
            R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
            return sigma
    return edad
            # print(f"su s {sigma} a {alpha} b {beta} R0 {R0} ")

print(prueba())

        # print("---------------------------------")
    # print(f"la edad del nodo {i+1} es de {edad[i]} ")

# def Ro(e1, e2,beta,Neta): #######################  CALCULA EL Ro DE CADA NODO
#     R0= (beta*prueba()*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
#     #R0 = beta*Neta*sigma*(1-e1)*(1-e2)/(c*mu)
#     return(R0)
# def funcii():
#     beta=ran.uniform(0, 0.002)
#     return Ro(e1, e2,beta,Neta)

# print(funcii())
# ENCUENTRA NODOS INFECTADOS EN LA RED
# ACTUALIZA LOS ATRIBUTOS (EI) DE CADA NODO DE LA RED
# EULER MEJORADO
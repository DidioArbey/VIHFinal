import random
import numpy as np
# print(random.randint(0, 100))
# mu=0.005
# c=0.24
# delta=0.26
# alpha=0.005
# beta=0.000025
# sigma=10
# u=1
e1=random.random()
print(e1)
e2=random.random()
print(e2)
print("###############")

mu=0.005
edad=[]
N=5
Neta=14
u=1
c=0.24

sigma=9
alpha=0.002
beta=0.0005

def Ro(e1, e2,beta,Neta,sigma): #######################  CALCULA EL Ro DE CADA NODO
    R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
    #R0 = beta*Neta*sigma*(1-e1)*(1-e2)/(c*mu)
    return(R0)


print(Ro(e1, e2,beta,Neta,sigma))

for i in range (N):
    edad.append(random.randint(0, 75))#75 ya qyue es la esperanza de vida que hay en colombia
    print (f"la edad del nodo {i+1} es de {edad[i]} ")
    if edad[i] >= 0 and edad[i] <=14:
        sigma=random.randint(10, 20)
        alpha=0.005
        beta=random.uniform(0, 0.002)
        R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
        print(f"su s {sigma} a {alpha} b {beta} R0 {R0} ")
    elif edad[i] > 14 and edad[i] <=24:
        sigma=random.randint(8, 15)
        alpha=0.005
        beta=random.uniform(0, 0.002)
        R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
        print(f"su s {sigma} a {alpha} b {beta} R0 {R0} ")
    elif edad[i] > 24 and edad[i] <=49:
        sigma=random.randint(5, 10)
        alpha=0.005
        beta=random.uniform(0, 0.002)
        R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
        print(f"su s {sigma} a {alpha} b {beta} R0 {R0} ")
    elif edad[i] > 50 and edad[i] <=100:
        sigma=random.randint(0, 5)
        alpha=0.005
        beta=random.uniform(0, 0.002)
        R0= (beta*sigma*Neta*(1-e1*u)*(1-e2*u))/(mu*c)
        print(f"su s {sigma} a {alpha} b {beta} R0 {R0} ")

    print("---------------------------------")
    # print(f"la edad del nodo {i+1} es de {edad[i]} ")



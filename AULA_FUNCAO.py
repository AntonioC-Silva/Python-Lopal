import random

###############################
def saudacao():               #
    print("Olá, mundo!")      #
###############################

##################################
def calcular_media(nota1,nota2): #
    media = (nota1+nota2)/2      #       # se não colocar o return  l não vai fazer nada
    return media                 #
##################################

##########################
def minha_funcao():      #
    x=10 #varivel local  #
    print(x)             #
##########################

###########################################
def outra_funcao():                       #
    print(y) #pode acessar o valor global #
###########################################

####################
def mudar_valor(): #
    global z       #   #mudando local para global
    z = 100        #
####################

###############################################################
def tentar_mudar():                                           #
    a = 50 #isso é uma nova variavel local! Não muda a global #
    print(a) #imprime 50                                      #
###############################################################





saudacao()

minha_funcao()
#print(x) #ERRO

y = 20 #variavel global
outra_funcao()
print(y) # tbm pode usar aqui

z = 5
mudar_valor()
print(z)# Agora z vale 100

a = 7
tentar_mudar()
print(a) #ainda imprime 7

nota1= int(input("Escreva um numero: "))
nota2= int(input("Escreva um numero: "))
print(f"A media entre as notas {nota1} e {nota2} é {calcular_media(nota1,nota2)}")




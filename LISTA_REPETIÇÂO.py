#ATVD 1
'''
contador = 0
for num in range(10):
    nume = int(input("Escreva um numero: "))
    if nume%3 ==0:
        contador +=1
print(f"A quantidade de numeros multiplos de 3 é:  {contador}")
'''

'''
#ATVD 2
senha = 2617

while True:
    password = int(input("Digite a senha: "))
    if senha == password:
        break
'''


#ATVD 3
'''
opcao = 0
while True:
    print("Menu:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        resultado = num1+num2
        print("Resultado:",resultado)

    elif opcao == 2:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        resultado = num1 - num2
        print("Resultado:", resultado)

    elif opcao == 3:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        resultado = num1 * num2
        print("Resultado:", resultado)

    elif opcao == 4:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
        if num2 != 0:
            resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Erro: Divisão por zero.")
    elif opcao ==5:
        break
'''


#ATVD 4
'''
num1 = int(input("Escreva um numero: "))
num2  = int(input("Escreva outro numero"))

for num in range(num1 + 1, num2):                     #############TERMINAR##############
    if num <=1:
        continue
    primo = True
    for pri in range(2, num):
        if num % pri == 0:
            primo = False
            break
if primo:
    print(num)
'''

#ATVD5
'''
contador = 0
senha = 2617
while contador<4:
    password = int(input("Digite a Senha: "))
    if senha == password:
        print("Bem vindo!")
        break
    else:
        contador +=1
        if contador ==3:
            print("Acesso bloquado.")
            break
'''

#ATVD 6
'''
pares = []
impar = []
for num in range(10):
    numeros = int(input("Digite um numero: "))
    if numeros%2 ==0:
        pares.append(numeros)
    else:
        impar.append(numeros)

print(f"A lista de numeros pares é {pares}")
print(f"A lista de numeros impar é {impar}")
'''


#ATVD 7
'''
frase = input("Escreva uma frase: ")
cont_a = 0
cont_e = 0
cont_i = 0
cont_o = 0
cont_u = 0

for vogal in frase.lower():
    if vogal == "a":
        cont_a +=1
    elif vogal == "e":
        cont_e +=1
    elif vogal == "i":
        cont_i +=1
    elif vogal == "o":
        cont_o +=1
    elif vogal == "u":
        cont_u +=1

print(f"A quantidade de vogais 'a' : {cont_a} ")
print(f"A quantidade de vogais 'e' : {cont_e} ")
print(f"A quantidade de vogais 'i' : {cont_i} ")
print(f"A quantidade de vogais 'o' : {cont_o} ")
print(f"A quantidade de vogais 'u' : {cont_u} ")
'''











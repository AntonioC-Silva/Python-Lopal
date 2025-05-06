
'''def saudacao():
    print("Hello World")

saudacao()

def calcular(num1,num2,opcao):
    if opcao == 1:
        resultado = num1+num2
    elif opcao == 2:
        resultado = num1 - num2
    elif opcao == 3:
        resultado = num1 * num2
    elif opcao == 4:
        resultado = num1 / num2
    return resultado

opcao = int(input("Digite o numero da operação que vc deseja realizar: "))

if opcao <1 or opcao>4:
    print("ERRO")
else:
    num1= int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))

    calcular(num1,num2,opcao)
'''

'''
def area(l,c):
    resultado = l*c
    return resultado

l = float(input("Digite a largura: "))
c = float(input("Digite o comprimento: "))

print(area(l,c))
'''
'''
lista = []
useri = int(input("Escreva o numero onde a lista deve iniciar: "))
userf = int(input("Escreva o numero onde a lista deve finalizar: "))
cont = useri
for list in range(useri,userf):
    lista.append(list)
while cont<(userf**0.5):
    for re in lista:
        if re % cont ==0:
            lista.remove(re)
    cont += 1


print(lista)
'''

A = [[4, 1],
     [2, 5]]
print((A[0][0]*A[1][1])-(A[0][1]*A[1][0]))

def calcular_fatorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado

num = int(input("escreva o numero que deseja fatorar: "))
print(calcular_fatorial(num))
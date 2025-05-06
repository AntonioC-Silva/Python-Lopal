def maior(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2



num1 = int(input("Escreva um numero: "))
num2 = int(input("Escreva outro numero: "))
print(f"O numero maior é {maior(num1,num2)}")
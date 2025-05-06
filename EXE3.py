def media(numeros):
    soma = 0
    for numero in numeros:
        soma +=numero
        return soma/len(numeros)

numeros = [10,20,30]
print(media(numeros))
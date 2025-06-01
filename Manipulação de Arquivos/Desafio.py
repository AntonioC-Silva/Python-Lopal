def decodificador(texto):
    resultado = ''

    for letra in texto:
        if letra.isalpha():
            if letra.islower():
                codigo = ord(letra) - 3
                if codigo < ord('a'):
                    codigo += 26
                resultado += chr(codigo)
            elif letra.isupper():
                codigo = ord(letra) - 3
                if codigo < ord('A'):
                    codigo += 26
                resultado += chr(codigo)
        else:
            resultado += letra
    return resultado

caminho = input('Digite o caminho do arquivo: ')

try:
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print('Arquivo lido com sucesso!\n')
        pronto = decodificador(conteudo)
        print('Texto decifrado:')
        print(pronto)
        with open('decodificado.txt', 'w', encoding='utf-8') as saida:
            saida.write(pronto)

        print('\nTexto salvo como "decodificado.txt"')

except FileNotFoundError:
    print('Arquivo não encontrado. Verifique o caminho e tente novamente.')

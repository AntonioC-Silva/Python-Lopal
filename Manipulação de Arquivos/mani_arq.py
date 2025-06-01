import pandas as pd

historico_pedidos = [
    {'ID': 1, 'Nome': 'João', 'Endereço': 'Rua das Flores, 123', 'Produto': 'Camiseta', 'Quantidade': 2, 'Preço': 50, 'Data': '01/01/2023'},
    {'ID': 2, 'Nome': 'Mariana', 'Endereço': 'Avenida Central, 456', 'Produto': 'Tênis', 'Quantidade': 1, 'Preço': 120, 'Data': '02/01/2023'},
    {'ID': 3, 'Nome': 'Carlos', 'Endereço': 'Praça da Estação, 789', 'Produto': 'Mochila', 'Quantidade': 1, 'Preço': 80, 'Data': '03/01/2023'},
    {'ID': 4, 'Nome': 'Fernanda', 'Endereço': 'Alameda dos Anjos, 101', 'Produto': 'Relógio', 'Quantidade': 1, 'Preço': 150, 'Data': '04/01/2023'}
]

df = pd.DataFrame(historico_pedidos)
df.to_excel('Arquivo.xlsx', index=False)

#Atvd2
df = pd.read_excel('Arquivo.xlsx') #lendo
print(df)
df.to_csv('Arquivo.csv', index=False, encoding='utf-8')#convertendo

#Atvd3
df = pd.read_csv('Arquivo.csv')
print(df)
df.to_json('Arquivo.json', indent=4, force_ascii=False) #force igual a utf-8





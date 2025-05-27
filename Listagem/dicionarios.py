#dicionarios 

elemento = {
    'Z':3,
    'nome':'Litio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(elemento)
print(f'elemento: {elemento['nome']}')
print(f'Densidade: {elemento['densidade']}')
print(f'O dicionario possui: {len(elemento)} elementos')

#Atualizar uma entrada

elemento['grupo'] = 'Alcalinos'
print(elemento)

#adcionar uma entrada

elemento['periodo'] = 1
print(elemento)

#exclusão de intens em dicionarios

# del elemento['periodo']
# print(elemento)

# #apagar todos os elementos

# elemento.clear()
# print(elemento)

# #apagar o dicionario por completo

# del elemento
# print(elemento)

#visualizar os itens do dicionario
print(elemento.items())
for i in elemento.items():
    print(i)

# visualizar as chaves do dicionario
print(elemento.keys())
for i in elemento.keys():
    print(i)

# visualizar os valores do dicionario
print(elemento.values())
for i in elemento.values():
    print(i)

# separar as chaves e valores
for i, j in elemento.items():
    print(f'{i}:{j}')

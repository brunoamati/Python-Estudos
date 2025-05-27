import random

# valor = random.randint(1, 20)
# print(valor)

# print('gerar cinco numeros aleatorios entre 1 e 50: \n')
# for i in range(5):
#     n = random.randint(1,50)
#     print(f'Numero gerado: {n}')

# valor = random.random()
# print(f'numero gerado: {round(valor*10,2)}')

# valor = random.uniform(1,100)
# print(f'numero: {round(valor,4)}')

L = [2,4,6,9,10,11,15,13,17,14,27,66]
# n = random.choice(L)
# print(f'Numero escolido: {n}')

# n = random.sample(L,3)
# print(f'Numeros escolidos: {n}')

#Embaralhar
print(f'Exibir a lista original: {L}')
print(f'Embaralhar a lsita e exibi-la: ')
n = random.shuffle(L)
print(L)
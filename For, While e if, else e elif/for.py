lista = [2,6,9,4,0,12,3,7] # [] é pra fazer listas
palavra = 'palavra'

for item in lista:
    print(item)

for letra in palavra:
    print(letra)

for num in range(1,11):
    print(num)
#ou
for num in range(10):
    print(num)

nome = input('Digite seu nome: ')

for x in range(10):
    print(f'{x+1} {nome}')

# range(val_inc, val_final, incremento)
for x in range(2,20,2):
    print(x)

pedras = ('rubi','esmeralda','safira','quartzo','diamante','ametista')

for pedra in pedras:
    if pedra == 'quartzo':
        continue # ele apenas faz não imprimir a iteração atual, porem imprime as seguintes
    print(pedra)
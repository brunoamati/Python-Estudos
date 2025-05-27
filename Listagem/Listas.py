# lista = representa uma sequencia de valores
#sintaxe: nome_lista = [val]
# notas = [5,7,8,6,9]
# print(notas)

# n1 = [4,6,7,8,0,3]
# n2 = [1,6,3,0,12,4]

# valores = n1 + n2
# valores[0] = 9

# print(valores)
# print(valores[0]) # valores do começo
# print(valores[-1])
# print(valores[-2]) # valores do final
# print(valores[0:2]) # imprimir 2 valores ou qualquer um
# print(len(valores)) # imprime a quantia de elementos da lista
# print(sorted(valores)) #mostra os valores em ordem crescente
# print(sorted(valores, reverse=True)) # ordem inversa
# print(sum(valores)) # soma os valores da lista
# print(min(valores)) # valor minimo
# print(max(valores)) # valor maximo

# valores.append(13) # adciona um valor a ultima posição da lista
# print(valores)
# valores.pop() #retira o ultimo elemento da lista
# print(valores)
# valores.pop(3) # se digitar um numero remove o respectivo numero
# print(valores)
# valores.insert(3,21) # coloca um valor em uma posição determinada
# print(valores)
# print(12 in valores)
# print(17 in valores) # verifica se tem na lista

# planetas = ['Mercurio', 'Venus', 'Terra', 'Marte', 'Saturno', 'Urano']
# for planeta in planetas:
#     print(planeta)

# Criar uma lista de bebidas inseridas pelo usuario e retornar ela em ordem alfabetica usando o laço de repet for

# minha resolução
# b = (input('Digite uma bebida que você gosta: '))
# b2 = (input('Digite outra bebida que você gosta: '))
# b3 = (input('Digite outra bebida que você gosta: '))
# b4 = (input('Digite outra bebida que você gosta: '))
# b5 = (input('Digite outra bebida que você gosta: '))
# bebidas = [b,b2,b3,b4,b5]
# bebidas = sorted(bebidas)

# for bebida in bebidas:
#     print(bebida)

# resolução sugerida

# bebidas = []

# for i in range(5):
#     print('Digite uma bebida favorita: ')
#     bebida = input()
#     bebidas.append(bebida)

# bebidas.sort()
# print (f'\nBebidas escolidas: ')
# for bebida in bebidas:
#     print (bebida)

# print(f'Saúde!')
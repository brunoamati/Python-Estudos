# numeros = [1,4,7,9,10,12,21]
# quadrados = [num **2 for num in numeros]
# print(quadrados)

# Criar lista de num pares de 0 a 10
# pares = [num for num in range(11) if num % 2 == 0]
# print(pares)

# frase = 'uma frase muito legal sem ser lorem ipsum é legal'
# vogais = ['a','e','i','o','u','é']
# lista_vogais = [v for v in frase if v in vogais]
# print(f'A frase possui {len(lista_vogais)} vogais')
# print(lista_vogais)

# Distributiva entre valores de duas listas
distributiva = [k * m for k in [2, 3, 5] for m in [10, 20, 30]]
print(distributiva)

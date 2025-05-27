# Funções
# modularização, reuso do codigo, legibilidade

# def define a função
# def <nome_função> ([argumentos]):
#   <instruções>

# def mensagem():
#     print('Hello word')
#     print('Python função')

# mensagem()

# Função com argumentos

# def soma(a, b):
#     print(a+b)

# soma(12, 7)

# def mult(x, y):
#     return x * y

# a = 5
# b = 8
# c = mult(a, b)
# print(f'Produto de {a} e {b} é {c}')

# def div(k, j):
#     if j != 0:
#         return k / j
#     else:
#         return 'Impossivel dividir por 0'


# if __name__ == '__main__':
#     a = int(input('Digite um numero: '))
#     b = int(input('Digite outro numero: '))

#     r = div(a, b)
#     print(f'{a} dividido por {b} é igual a {r}')

# def quadrado(val):
#     quadrados = []
#     for x in val:
#         quadrados.append(x ** 2)
#     return quadrados

# if __name__ == '__main__':
#     valores = [2,5,7,9,12]
#     resultados = quadrado(valores)
#     for g in resultados:
#         print(g)

# def idade(x, y):
#     if x >= y:
#         return x - y
#     else:
#         return 'Não existe idade negativa'


# if __name__ == '__main__':
#     x = int(input('Digite um ano:'))
#     y = int(input('Digite outro ano:'))
#     resultado = idade(x, y)
#     print(f'A diferença de idade/anos entre {x} e {y} é de {resultado} anos')

# parte sobre parametros opcionais, obrigatorios e valor padrão

# def contar(num=11, caractere='+'):
#     for i in range(1, num):
#         print(caractere)

# if __name__ == '__main__':
#     contar(num=8,caractere='@')
#     contar(6, '$')

x = 5
y = 6
z = 3


def soma_mult(a, b, c = 0):
    if c == 0:
        return a * b
    else:
        return a + b + c


if __name__ == '__main__':
    res = soma_mult(x, y, z)
    print(res)

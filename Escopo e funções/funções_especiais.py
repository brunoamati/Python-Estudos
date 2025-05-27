# funções lambda(anonimas)
# sintaxe : lambda argumentos : expressão

# quadrado = lambda x: x**2
# for i in range(1,11):
#     print(quadrado(i))

# par = lambda x: x % 2 == 0
# print(par(9))

# f_c = lambda f: (f - 32) * 5/9
# print(f_c(32))

# função map()
# sintaxe : map(função, iteravel)

# num = [1,2,3,4,5,6,7,8]
# dobro = list(map(lambda x: x*2,num))
# print(dobro)

# palavras = ['Python','java','javascript','php','sql']
# maiusculas = list(map(str.upper,palavras))
# print(maiusculas)

# função filter
# sintaxe: filter(função, sequencia)
# def num_pares(n):
#     return n % 2 == 0

# num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# n_par = list(filter(num_pares, num))
# print(n_par)

# num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
# num_impar = list(filter(lambda x: x % 2 != 0, num))
# print(num_impar)

# função reduce()
# sintaxe: reduce(função, sequencia, valor_inicial)
from functools import reduce

# def mult(x, y):
#     return x * y

# numeros = [1,2,3,4,5,6]

# r = reduce(mult,numeros)
# print(r)

# soma cumulativa dos quadrados de valores usando lambda

numeros = [1, 2, 3, 4]
# ((1²+2²)²+3²)²+4²
total = reduce(lambda x, y: x**2+y**2, numeros)
print(total)

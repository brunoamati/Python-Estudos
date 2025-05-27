# == igual a
# != diferente de
# > maior que
# < menor que
# >= maior ou igual a
# <= menor ou igual a
a = 5
b = 5
print(a==5)
print(b==6)
print(a==b)
print(a!=b)
print(b!=a+1)
print(a*2>=b)

x = y = z = False
n1 = n2 = 0
print("digite um numero: ")
n1 = int(input(''))
n2 = int(input('Digite outro numero: '))

x = n1 == n2
print('São iguais?', x, '\n') #\n equivale a um enter e tem que estar entre aspas

z = n1 > n2
print(n1, 'é maior que', n2, '?', z, '\n')

y = n1 != n2
print('São diferentes? ' + str(y)) 
# + pode ser concatenação também, usado para criar mensagens exibidas pelo usuario

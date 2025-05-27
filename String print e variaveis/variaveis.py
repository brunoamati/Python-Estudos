name = 'Bruno'
media = 6
n1 = n2 = n3 = n4 = 6.0
nome, idade = 'gleison' , 34 #teste
estado = True

# # função type() mostrar tipo da variavel

print(name)
print(type(media))
print(type(n2))
print(type(name))
print(type(estado))
print(type(1+2j)) 

# função isinstance() verificar o tipo da variavel
a = 10
b = 'sol'
print(isinstance(a, int))
print(isinstance(b, str))
print(isinstance(b, float))
print(isinstance(b, (float, int, str)))

a = 40
c = 3
r = a * c
print(r)

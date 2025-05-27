# permite varios dados na mesma estrutura, se parece com listas, porém são imutaveis

# tupla = (2,4,6,7,9)
# # tupla[1] = 5 se executar isso da erro
# print(tupla)

halogenios = ('F', 'Cl', 'Br', 'I', 'At')
# print(len(halogenios))
# print(halogenios[3])
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
# print(elementos)
t1 = (5,2,6,3,1,5,67,5,1,5,7,8,9,0,3,2,1)
# print(t1.count(5))
# print(halogenios[0:2])
# print('Cl' in halogenios)
# print(sum(t1))

#Operações não disponiveis em tupla: .sort(), .append(), .reverse(), . pop()... tudo que altere ela não esta disponivel

# for elemento in elementos:
#     print(f'Elemento quimico: {elemento}')


# grupo17 = list(halogenios) # tupla pra lista
# print(grupo17)
# grupo17[0] = 'H'
# print(grupo17) 

# lista pra tupla
grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1) # Lista pra tupla
# print(type(alcalinos))

print(sorted(alcalinos))
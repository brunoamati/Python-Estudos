# Set
#não existe valores dublicados nos conjuntos

planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
# print(planeta_anao)
# print(len(planeta_anao))
# print('Ceres' in planeta_anao)
# print('Lua' not in planeta_anao)

# for astro in planeta_anao:
#     print(astro.upper())

# astros = ['Lua', 'Venus', 'Sirius', 'Marte', 'Lua']
# print(astros, end=' ')
# astro_set = set(astros)
# print(astro_set)

astros1 = {'Lua', 'Venus', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Venus', 'Sirius', 'Marte', 'Cometa de Halley'}
# print(astros1 == astros2)
# print(astros1 != astros2)
# print(astros1 | astros2)
# print(astros1.union(astros2)) # tanto o | quanto o .union juntam os sets
# print(astros1 & astros2)
# print(astros1.intersection(astros2)) # tento o & quanto o .intersection são para intersecção de conjuntos
# print(astros1 ^ astros2)
# print(astros1.symmetric_difference(astros2)) # tanto o ^ quanto o .symmetric_difference mostram a difeença dos conjuntos
astros1.add('Urano')
astros1.add('Sol') # para adicionar no conjunto
print(astros1)
astros1.remove('Io') # para remover
astros1.remove('Plutão') # se tentar remover da erro pois não está no conjunto
print(astros1)
astros1.discard('Plutão') # outro metodo de remoção, porem não da erro se tentar remover mesmo se não estiver no conjunto
print(astros1)
# astros1.pop() também funciona no conjunto
astros1.clear() #limpa o conjunto todo
print(astros1)
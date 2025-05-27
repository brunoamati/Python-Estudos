# nome = 'Bruno'
# sobrenome = 'Amati'
# letra = nome[2]
# print(letra)
# print(len(nome))
# print(nome + ' ' + sobrenome)

# frase = 'Vamos aprender python hoje'
# palavras = frase.split() #separa a string em partes e coloca em lista
# print(palavras)
# for letra in frase:
#     print(letra)
# print(frase[0:5])
# print(frase[6:15])
# print(frase[7:19])
# print(frase[-3:])

# email = input('Digite seu endereço de email: ')
# arroba = email.find('@')
# print(arroba)
# usuario = email[0:arroba]
# dominio = email[arroba+1:]
# print(usuario)
# print(dominio)

# produtos = 'carbonato de sodio e oxido de zinco'
# print('sodio' in produtos)
# print('magnesio' not in produtos)

item = 'hipoclorito'
pos = item.find('clor')
print(pos)
pos = item.find('flu')
print(pos) #se retornar -1 é por que não tem

# objeto_celeste = 'galaxia esPiral M31'
# print(objeto_celeste.upper()) #digitar tudo em caixa alta
# print(objeto_celeste.lower()) #digitar tudo em caixa baixa
# print(objeto_celeste.capitalize()) #digitar a primeira letra em maiusculo
# print(objeto_celeste.title()) #digitar a primeira letra de cada palavra em maiusculo

# suplemento = 'cloreto de magnesio'
# n_suplemento = suplemento.replace('magnesio', 'zinco') # substitui a string
# print(suplemento)
# print(n_suplemento)

#remover espaços em branco na string
# frase = '    Omega 3 da top therm'
# print(frase)
# print(frase.lstrip()) #espaços a mais na esquerda
# print(frase.rstrip()) #espaços a mais na direita
# print(frase.strip()) #espaços a mais em ambos os lados

# #alinhamento de texto para exibição
# fruta = 'Abacate'
# print(fruta)
# print(fruta.rjust(20)) #right justify para jsutificar a direita usando algum espaço determinado
# print(fruta.center(20)) #centralizar a palavra
# print(fruta.ljust(20, "-")) # mesmo da direita
# print(fruta.center(20, "-"))

# ver se termina ou começa com alguma letra ou coisa da string
p = 'Treinamentos Python'
print(p.startswith('Trei'))
print(p.startswith('trei'))
print(p.endswith('n'))
print(p.endswith('o'))

#docstrings
texto = """
Docstring é uma especie de docmentação que podemos inserir dentro de um modulo, função ou classe no python
entre outros locais
    respeita deslocamento do texto e é multilinhas
"""
print(texto)
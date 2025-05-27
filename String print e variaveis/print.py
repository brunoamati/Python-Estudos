# sintaxe:
# print(objetos, argumentos)

msg = 'Função print()'
print(msg)
print('Mensagem :)') 

nome = 'Bruno'
empresa = 'bk'
print('Nome de usuario e empresa', nome, '-', empresa)

nome = input('Digite seu nome: ')
print('Olá ' + nome + '! Bem vindo!')
print('outro texto')

print('Imprime a msg e muda de linha.')
print('Imprime a mensagem e permanece na linha. ', end='') #end mantem na mesma linha
print('continuo na mesma linha.')

nome = 'Maria'
idade = 30
msg_format = 'O nome dela é {0} e ela tem {1} anos'.format(nome, idade)
print(msg_format)

nome = 'Bruno'
peso = 70.50
msg = f'Olá meu nome é {nome} e meu peso é {peso} kg.' 
print(msg)
#f string deixa mais "facil" a concatenação e pode executar expressoes dentro dela

a = 10
b = 5
res = f'A soma de {a} com {b} é igual a {a+b}'
print(res)

valor = 125.57967
print(f'O valor é {valor}')
print(f'O valor é {valor:.2f}')
print(f'O valor é \'{valor:.2f}\'') 
#uso do caracter de escape de modo que a barra mostra q o ' não faz parte da string e sim um caracter a ser impresso

nome = 'João'
idade = 32
print(f'Nome: {nome}\tIdade: {idade}')
#\t = tabulação ou igual a dar um tab na linha

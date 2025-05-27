def guardar_nomes(fim):
    global names_lista
    global lista_checar
    names_lista = []
    lista_checar = []
    while len(names_lista) < fim:
        p = input('Qual nome deseja armazenar na lista? ').strip()
        p_menor = p.lower()
        if p_menor in lista_checar:
            print(f'Esse nome já tem na lista, por favor digite outro.')
        else:
            p_format = p.title()
            names_lista.append(p_format)
            lista_checar.append(p_menor)
    names_lista.sort()
    print(f'Há {len(names_lista)} nomes na lista.')
    return ', '.join(names_lista)


def pesquisar_nome(nome_pe):
    nomes_pesq = [nome for nome in names_lista if nome_pe in nome.lower()]
    if nomes_pesq:
        print(f'Existem esses nomes na lista: {nomes_pesq}')
    else:
        return 'Nenhum nome encontrado.'


def excluir_nome_simples(lista_nv):
    if lista_nv in names_lista:
        names_lista.remove(lista_nv)
        # exclui o nome que foi especificado no código
        return f'Essa é a lista atual {names_lista}'
    else:
        return 'Esse nome não está presente, lista não foi alterada.'


def excluir_nome(lista_nv):
    encontrado = [nome for nome in names_lista if lista_nv in nome.lower()]
    if encontrado:
        print(f'Esses nomes foram encontrados na lista: {encontrado}')
        nome_certo = input(
            'Digite o nome exato que deseja remover da lista: ').strip()
        if nome_certo in names_lista:
            names_lista.remove(nome_certo)
            return f'O nome {nome_certo} foi removido da lista. Essa é a nova lista: {names_lista}'
        else:
            return f'O nome digitado não está presente na lista.'
    else:
        return f'Não há nenhum nome que contenha isso na lista.'


def contar_nomes(contar_nome):
    contar = sum(1 for nome in names_lista if contar_nome in nome.lower())
    if contar:
        nome_form = contar_nome.title()
        return f'O nome {nome_form} aparece {contar} vez(es).'
    else:
        return f'Esse nome não está presente na lista.'


while True:  # while para definir a quantia de nomes
    try:
        x = int(input('Quantos nomes deseja salvar na lista? '))
        break
    except ValueError:
        print(f'Valor incorreto, tente novamente')

print(f'Nomes da Lista: {guardar_nomes(x)}')

while True:  # While pesquisar nome
    ask = input('Deseja pesquisar algum nome na lista? (S/N) ').strip().lower()
    if ask == 's':
        nome_pe = input('Qual nome deseja pesquisar? ').strip().lower()
        print(pesquisar_nome(nome_pe))
    elif ask == 'n':
        print('Pesquisa finalizada.')
        break
    else:
        print('Opção inválida, por favor responda com "S" ou "N".')

while True:  # While excluir nome
    ask = input('Deseja Remover algum nome na lista? (S/N) ').strip().lower()
    if ask == 's':
        lista_nv = input('Qual nome deseja remover? ').strip().lower()
        print(excluir_nome(lista_nv))
    elif ask == 'n':
        print('Lista intacta.')
        break
    else:
        print('Opção inválida, por favor responda com "S" ou "N".')

while True:  # While contar nomes
    ask = input(
        'Deseja ver quantas vezes o nome aparece na lista? (S/N) ').strip().lower()
    if ask == 's':
        contar_nome = input('Que nome deseja ver? ').strip().lower()
        print(contar_nomes(contar_nome))
    elif ask == 'n':
        print('Contagem finalizada.')
        break
    else:
        print('Opção inválida, por favor responda com "S" ou "N".')


while True:
    ask = input(
        'Deseja ver quantas vezes o nome aparece na lista? (S/N) ').strip().lower()
    if ask == 's':
        contar_nome = input('Que nome deseja ver? ').strip().lower()
        print(contar_nomes(contar_nome))
    elif ask == 'n':
        print('Contagem finalizada.')
        break
    else:
        print('Opção inválida, por favor responda com "S" ou "N".')


while True:  # while limpar lista
    ask = input('Deseja LIMPAR a lista? (S/N) ').strip().lower()
    if ask == 's':
        confirmacao = input('TEM CERTEZA? (S/N) ').strip().lower()
        if confirmacao == 's':
            names_lista.clear()
            print(f'Lista limpa. Segue lista vazia: {names_lista}')
        elif confirmacao == 'n':
            print('Lista continua sem alterações.')
        else:
            print('Opção inválida, por favor responda com "S" ou "N".')
        break
    elif ask == 'n':
        print('Lista continua sem alterações.')
        break
    else:
        print('Opção inválida, por favor responda com "S" ou "N".')


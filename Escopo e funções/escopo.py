# Escopo Global e local

var_global = "Curso completo python"

def escreve_texto():
    global var_global #diz que se refere a uma varivale global fora da função
    var_global = "Banco de dados"
    var_local = "Olá"
    print(f'Varialvel global: {var_global}')
    print(f'Varialvel loal: {var_local}')

if __name__ == '__main__':
    print(f'Executar a função escreve_texto()')
    escreve_texto()

    print('Tentar acessar as variaveis diretamente')
    print(f'Varialvel global: {var_global}')
    # print(f'Varialvel local: {var_local}') # não acessivel fora da função
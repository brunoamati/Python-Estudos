def lista_tuple(numeros):
    lista_numeros = numeros.split(",")
    tupla = tuple(lista_numeros)
    lista = list(lista_numeros)
    return lista, tupla

print(lista_tuple("3,6,5,3,2,8"))

#resolução sugerida

# def convert_input_to_list_and_tuple(input_string):
#     values = input_string.split(",")
#     return values, tuple(values)

# convert_input_to_list_and_tuple("3,6,5,3,2,8")
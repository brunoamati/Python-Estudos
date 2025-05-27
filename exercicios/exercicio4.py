def maiusculas():
    str = input('insira uma palavra e ela vai retornar em caixa alta: ')
    str_alta = print(str.upper())
    return str_alta

maiusculas()

# resolução sugerida

# class InputOutString:
#     def __init__(self):
#         self.s = ""

#     def get_string(self):
#         self.s = input("Enter a string: ")

#     def print_string(self):
#         print(self.s.upper())

# # Test function

# str_obj = InputOutString()
# str_obj.get_string()
# str_obj.print_string()

for i in range(100, 200):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=' ')

#Solução sugerida

# def find_numbers(start, end):
#     result = []
#     for i in range(start, end + 1):
#         if i % 7 == 0 and i % 5 != 0:  # se define uma função
#             result.append(str(i))
#     return ','.join(result)

# # Call the function with specific start and end values
# print(find_numbers(100, 200))
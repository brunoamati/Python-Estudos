def quadrado(n):
    d = dict()
    for i in range(1, n + 1):
        d[i] = i ** 2
    return d
    
print(quadrado(8))

# def generate_square_dict(n):
#     d = dict()
#     for i in range(1, n + 1):
#         d[i] = i * i
#     return d

# print(generate_square_dict(8))
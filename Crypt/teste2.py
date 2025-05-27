with open("VM-HOME-OFFICE-000002.vmdk.encrptd", "rb") as f:
    data = f.read()

# Exibir os primeiros 256 bytes em hexadecimal
print(data[:256].hex())

# Ou salvar tudo em um arquivo
with open("hex_output.txt", "w") as out:
    out.write(data.hex())
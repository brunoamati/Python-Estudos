from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import unpad
import binascii
from Crypto.Protocol.KDF import PBKDF2

ITERATIONS = 100000  # ou outro valor se suspeitar
KEY_LEN = 32  # 256 bits
# Carregar arquivo criptografado
with open("VM-HOME-OFFICE-000001.vmdk.encrptd", "rb") as f:
    data = f.read()

# Separar IV e dados criptografados
salt = data[:16]
iv = data[:16]
ciphertext = data[16:]

# Lista de senhas comuns para testar
with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
    password_list = [line.strip() for line in f]


# Tentar descriptografar com cada senha
for password in password_list:
    try:
        print(f'Senha usada: {password}')
        # Derivar chave com SHA-256
        key = SHA256.new(password.encode()).digest()  # 32 bytes

        # Criptografia AES CBC
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext)

        # Tentar remover padding
        plaintext = unpad(decrypted, AES.block_size)

        # Se chegou até aqui, a senha é válida!
        print("\n✅ Senha encontrada:", password)
        print("Prévia do conteúdo descriptografado:\n", plaintext[:200])
        break

    except Exception as e:
        # Descriptografia falhou — tentar próxima senha
        continue

for password in password_list:
    try:

        # Derivar chave com PBKDF2
        key = PBKDF2(password.encode(), salt, dkLen=KEY_LEN, count=ITERATIONS)

        # Tentar descriptografar
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(ciphertext)

        # Tentar remover padding
        plaintext = unpad(decrypted, AES.block_size)

        print("\n✅ Senha encontrada:", password)
        print("Prévia do conteúdo:\n", plaintext[:200])
        break

    except Exception:
        continue
else:
    print("❌ Nenhuma senha testada funcionou.")

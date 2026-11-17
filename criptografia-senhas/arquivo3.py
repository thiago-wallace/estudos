# cryptography (reversível): criptografar e descriptografar qualquer dado em bytes, tanto uma 

# pip install cryptography

from cryptography.fernet import Fernet
from getpass import getpass

senha = 'teste@123'

# converter de str para bytes
senha_bytes = senha.encode()

# gerar a chave
chave = Fernet.generate_key()

# instanciar a classe Fernet com a chave, para poder criptografar/descriptografar com base nessa chave
f = Fernet(chave)

# criptografar a senha
senha_criptografada = f.encrypt(senha_bytes)
print(senha_criptografada)

# solicitar ao usuário digitar a senha
senha_digitada = getpass('Digite a senha: ')
senha_digitada_bytes = senha_digitada.encode()

# descriptografar a senha
senha_descriptografada = f.decrypt(senha_criptografada)

# print convertendo de bytes para str
print('Senha dcr:', senha_descriptografada.decode())
print('Senha dig:', senha_digitada_bytes.decode())

# validar se a senha digitada bate com a senha descriptografada
validacao = senha_digitada_bytes == senha_descriptografada
print(validacao)

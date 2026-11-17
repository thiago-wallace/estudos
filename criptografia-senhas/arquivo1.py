# Werkzeug (irreversível): gerar hash de senha, recomendada para usar com Flask (integração com JavaScript para web) e apps simples
# pip install Werkzeug
# https://pypi.org/project/Werkzeug/
from werkzeug.security import generate_password_hash, check_password_hash
# getpass: semelhante ao input(), porém pensado para senhas, escondendo os caracteres 
from getpass import getpass

senha = 'teste@123'

# gerar a hash da senha
hash_senha = generate_password_hash(senha)
print(hash_senha)

# solicitar ao usuário digitar a senha
senha_digitada = getpass('Digite a senha: ')

# validar se o hash da senha bate com a senha digitada (gerando a hash da senha digitada e comparando as duas hash), retornando bool
validacao = check_password_hash(hash_senha, senha_digitada)
print(validacao)

# duas senhas iguais terão hash diferentes, porém o módulo saberá comparar se as senhas realmente são iguais, mesmo com as hashs diferentes

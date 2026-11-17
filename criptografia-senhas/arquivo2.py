# bcrypt (irreversível): gerar hash de senha em bytes, recomendada por ser mais robusto. Todos os métodos do bcrypt lê as senhas em bytes, ao invés de str
# pip install bcrypt
# https://pypi.org/project/bcrypt/
import bcrypt
# getpass: semelhante ao input(), porém pensado para senhas, escondendo os caracteres 
from getpass import getpass

senha = 'teste@123'

# converter de str para bytes
senha_bytes = senha.encode()

# gerar o salt (necessário para gerar o cálculo da hash)
salt = bcrypt.gensalt()

# gerar a hash da senha
hash_senha = bcrypt.hashpw(senha_bytes, salt)
print(hash_senha)

# solicitar ao usuário digitar a senha
senha_digitada = getpass('Digite a senha: ')
senha_digitada_bytes = senha_digitada.encode()

# validar se o hash da senha bate com a senha digitada em bytes (gerando a hash da senha digitada e comparando as duas hash), retornando bool
validacao = bcrypt.checkpw(senha_digitada_bytes, hash_senha)
print(validacao)

# duas senhas iguais terão hash diferentes, porém o módulo saberá comparar se as senhas realmente são iguais, mesmo com as hashs diferentes

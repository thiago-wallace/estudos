# pywhatkit: módulo usado para integração com whatsapp e youtube
# necessário instalação: pip install pywhatkit
# https://github.com/Ankit404butfound/PyWhatKit/wiki
from pywhatkit import whats
# tkinter: usado para criar uma message box (mesmo com o app no console)
from tkinter import messagebox

telefone = '+551142256544'
mensagem = 'teste'

# envia mensagem para o telefone, abrindo o navegador padrão, com o whatsapp web (o mesmo já deve estar escaneado) e envia mensagem para o telefone.
# no momento da execução, o usuário não pode mexer o mouse nem o teclado.
# nesse código, a execução foi programada para às 23h32min.
whats.sendwhatmsg(telefone, mensagem, 23, 32)

# exibe uma message box
messagebox.showinfo('Teste', 'Mensagem enviada com sucesso')

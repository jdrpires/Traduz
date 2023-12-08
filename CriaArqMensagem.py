import os
from googletrans import Translator

# Parâmetros de entrada
pasta = '/Users/t736796/Projetos/TestesJ/Arqs'  # '.' = diretorio atual, '..' => anterior
extensao = 'yaml'
messageDomain = 'cadastral'
messageCode = 'erro-ao-chamar-api'  # tb será o nome do arquivo e o summary
type = 'error'  # pode ser outros tipo
languages = ['en-US', 'es-ES', 'es-CL']
messagePtBr = 'Não foi possível chamar a API'

# Variaveis do sistema
trans = Translator()

# cria o arquivo na pasta
arq = pasta + '/' + messageCode + '.' + extensao
print(arq)
arquivoGerado = open(arq, 'w+', encoding='utf-8')
arquivoGerado.write('messageDomain: ' + messageDomain)
arquivoGerado.write('\n')
arquivoGerado.write('messageCode: ' + messageCode)
arquivoGerado.write('\n')
arquivoGerado.write('type: ' + type)
arquivoGerado.write('\n')
arquivoGerado.write('summary: ' + messageCode)
arquivoGerado.write('\n')
arquivoGerado.write('languages:')
arquivoGerado.write('\n')
arquivoGerado.write('  - code: pt-BR')
arquivoGerado.write('\n')
arquivoGerado.write('  message: ' + messagePtBr)
for j in languages:
    lingua = j.split('.')[-1]
    arquivoGerado.write('\n')
    arquivoGerado.write('  - code: ' + lingua)
    arquivoGerado.write('\n')
    arquivoGerado.write('  message: ' + trans.translate(messagePtBr, dest=lingua[0:2]).text)

arquivoGerado.close()

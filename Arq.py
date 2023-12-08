import os
from googletrans import Translator

# Parâmetros de entrada
pasta = '/Users/t736796/Projetos/Arqs'  # '.' = diretorio atual, '..' => anterior
extensoes = ['yaml']  # deixe em branco para todos
buscaArq = 'es-ES'
BuscaLanguage = 'pt-BR'
LinguagemTraduzir = 'es'

# Variaveis do sistema
contaArq = 1
arqAlt = 0
arqNAOAlt = 0
trans = Translator()


def geralinha(linguaincluir, textotraduzido, ultimalinha, space):
    if ultimalinha != "\n":
        if space == 4:
            textoretorno = "\n  - code: " + linguaincluir + "\n    message: " + textotraduzido
        else:
            textoretorno = "\n- code: " + linguaincluir + "\n  message: " + textotraduzido
    else:
        if space == 4:
            textoretorno = "    - code: " + linguaincluir + "\n  message: " + textotraduzido
        else:
            textoretorno = "- code: " + linguaincluir + "\n  message: " + textotraduzido

    return textoretorno
    pass


# lê arquivos na pasta
arquivos = os.listdir(pasta)
# para cada arquivo na pasta
for i in arquivos:
    print('Arquivo número:' + str(contaArq))
    # se vazio, exibir todos
    if not extensoes:
        print("*****************************************************************************")
        print("*************** Extensão do tipo de arquivo não parametrizada ***************")
        print("*****************************************************************************")
    else:
        extensao = i.split('.')[-1]
        if extensao in extensoes:
            oqueabrir = pasta + "/" + i
            arquivoAberto = open(oqueabrir, "r+")
            readfile = arquivoAberto.read()
            arquivoAberto.close()
            if buscaArq in readfile:
                print('No Arquivo: ' + i + ' a mensagem já esta cadastrada na lingua: ' + buscaArq)
                arqNAOAlt = arqNAOAlt + 1
            else:
                print('No Arquivo: ' + i + ' a mensagem NÃO esta cadastrada na lingua: ' + buscaArq)
                arquivoAberto2 = open(oqueabrir, "r+")
                readfile2 = arquivoAberto2.readlines()
                index = 0
                for line in readfile2:
                    index = index + 1
                    if BuscaLanguage in line:
                        tamanholinha = len(readfile2[index])
                        TextoTraduzir = readfile2[index].strip()
                        if TextoTraduzir[8:tamanholinha] == "":
                            print("*****************************************************************************")
                            print("*************** Mensagem em " + BuscaLanguage + " esta vazia, valide o arquivo: " + i + " ***************")
                            print("*****************************************************************************")
                            exit()
                        espacoBranco = readfile2[index].count(' ', 0, 7)
                        texto1 = trans.translate(TextoTraduzir[8:tamanholinha], dest=LinguagemTraduzir).text
                        print('A mensagem na lingua: ' + BuscaLanguage + 'é: ' + readfile2[index][11:tamanholinha])
                        print('A mensagem traduzida para a lingua: ' + buscaArq + ' é: ' + texto1)
                        break
                lastLine = readfile[len(readfile) - 1]
                textoArquivo = geralinha(buscaArq, texto1, lastLine, espacoBranco)
                arquivoAberto2.write(textoArquivo)
                arqAlt = arqAlt + 1
                arquivoAberto2.close()

    contaArq = contaArq + 1

print('*************************************')
print('TOTAL DE ARQUIVOS DA PASTA: ' + str(contaArq))
print('TOTAL DE ARQUIVOS ALTERADOS = ' + str(arqAlt))
print('TOTAL DE ARQUIVOS NÃO ALTERADOS = ' + str(arqNAOAlt))
validador = arqAlt + arqNAOAlt
print('VALIDADOR: ' + str(validador))
print('*************************************')

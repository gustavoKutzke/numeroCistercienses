from PIL import Image
import os

def encontre_imagem_identica(caminho_da_pasta, caminho_da_imagem):
    imagem_alvo = Image.open(caminho_da_imagem)
    for nome_do_arquivo in os.listdir(caminho_da_pasta):
        if nome_do_arquivo.endswith('.png'):
            caminho_do_arquivo = os.path.join(caminho_da_pasta, nome_do_arquivo)
            imagem_atual = Image.open(caminho_do_arquivo)
            if list(imagem_alvo.getdata()) == list(imagem_atual.getdata()):
                return nome_do_arquivo
    return None

nome_do_arquivo = encontre_imagem_identica('output/', 'numero.png')
if nome_do_arquivo:
    nome_do_arquivo_sem_extensao = os.path.splitext(nome_do_arquivo)[0]
    print(f'O número é: {nome_do_arquivo_sem_extensao}')
else:
    nome_do_arquivo = encontre_imagem_identica('output (white)/', 'numero.png')
    if nome_do_arquivo:
        nome_do_arquivo_sem_extensao = os.path.splitext(nome_do_arquivo)[0]
        print(f'O número é: {nome_do_arquivo_sem_extensao}')
    else:
        print('Nenhum número foi encontrado.')
   


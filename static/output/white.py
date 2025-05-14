from PIL import Image
import os

def adicione_fundo_branco(caminho_da_pasta):
    for nome_do_arquivo in os.listdir(caminho_da_pasta):
        if nome_do_arquivo.endswith('.png'):
            caminho_do_arquivo = os.path.join(caminho_da_pasta, nome_do_arquivo)
            imagem = Image.open(caminho_do_arquivo)
            imagem_com_fundo_branco = Image.new("RGBA", imagem.size, "WHITE")  # Cria uma imagem branca
            imagem_com_fundo_branco.paste(imagem, (0, 0), imagem)  # Cola a imagem original na imagem branca
            imagem_com_fundo_branco.convert('RGB').save(caminho_do_arquivo)  # Salva a imagem com fundo branco

adicione_fundo_branco('/home/vandelsoncleitoso/Documentos/Faculdade/7aFase/Algoritmos Avançados/cistericienses/output (cópia)')

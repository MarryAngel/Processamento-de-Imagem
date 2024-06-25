import matplotlib.pyplot as plt

def mostrar_imagem(imagem, titulo, colorMap = None):
    if colorMap is not None:
        plt.imshow(imagem, cmap=colorMap)
    else:
        plt.imshow(imagem)
    plt.title(titulo)
    plt.axis('off')
    plt.show()
    
def produzir_subimagem(subimagem, i, j, imagem, color_map = None, titulo = None):
    if i == 1:
        subimagem[j].imshow(imagem, cmap=color_map)
        subimagem[j].set_title(titulo)
        subimagem[j].axis('off')
    else:
        if color_map is None:
            subimagem[i][j].imshow(imagem)
        else:
            subimagem[i][j].imshow(imagem, cmap=color_map)
        subimagem[i][j].set_title(titulo)
        subimagem[i][j].axis('off')
        
def mostrar_escala(imagem, titulo, colorMap = None, escala = None):
    if escala is not None:
        plt.figure(figsize=(imagem.shape[0]*escala,imagem.shape[1]*escala))
    if colorMap is not None:
        plt.imshow(imagem, cmap=colorMap)
    else:
        plt.imshow(imagem)
    plt.title(titulo)
    plt.axis('off')
    plt.show()
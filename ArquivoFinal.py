import cv2
import numpy as np
import statistics

def mudanivel(imga, altura, largura, img):
    tons = 256 / ntons
    aux = tons

    for i in range(0, altura-1):
        for j in range(0, largura-1):
            while(imga[i,j] > aux):
                aux = aux + tons
            imga[i,j] = aux - tons
            aux = tons
    return(imga)

def redimencionar(imgs, altura, largura, alturanova, larguranova, medida, imga, metodo):
    medlar = largura/larguranova
    indice = medlar
    med = largura/larguranova
    indicey = med
    indicex = med
    indalt = (round(med))
    indlar = (round(medlar))
    x = 0
    y = 0
    lin = 0
    col = 0

    if(metodo == "media"):
        soma = 0
        while(x < altura):
            while(y < largura and (lin < larguranova)):
                if(y < largura):
                    for b in range(indalt):
                        for a in range(indlar):
                                if((y+a) < largura and (x+b) < altura):
                                    soma = soma + int(imga[x+b,y+a])
                    y = y + indlar
                    if(col < alturanova, lin < larguranova):
                        imgs[col,lin] = (soma/(indlar*indalt))
                        lin = lin + 1
                else:
                    y = y + 1
                indicey = indicey - round(indicey)
                indicey = indicey + med
                indlar = 0
                indlar = round(indicey)
                soma = 0
            indicex = indicex - round(indicex)
            indicex = indicex + med
            indalt = 0
            indalt = round(indicex)
            x = x + indalt
            col = col + 1
            lin = 0
            y = 0

            
    elif(metodo == "moda"):
        soma = []
        moda = 0
        bib = {}
        mrepet = 0
        
        while(x < altura):
            while(y < largura and (lin < larguranova)):
                bib = {}
                if(y < largura):
                    for b in range(indalt):
                        for a in range(indlar):
                             if((y+a) < largura and (x+b) < altura):
                                soma.append(imga[x+b,y+a])
                    y = y + indlar
                    for l in soma:
                        if l not in bib:
                            bib[l] = 1
                        else:
                            bib[l] += 1
                    mrepet = max(bib.values())
                    for i in bib:
                        if bib[i] == mrepet:
                            moda = i
                    if(col < alturanova and lin < larguranova):
                        imgs[col,lin]= moda
                    lin = lin + 1
                else:
                    y = y + 1
                indicey = indicey - round(indicey)
                indicey = indicey + med
                indlar = 0
                indlar = round(indicey)
                soma.clear()
                moda = 0
            indicex = indicex - round(indicex)
            indicex = indicex + med
            indalt = 0
            indalt = round(indicex)
            x = x + indalt
            col = col + 1
            lin = 0
            y = 0
            
    elif(metodo == "mediana"):
        soma = []
        median = 0

        while(x < altura):
            while(y < largura and (lin < larguranova)):
                if(y < largura):
                    for b in range(indalt):
                        for a in range(indlar):
                            if((y+a) < largura and (x+b) < altura):
                                soma.append(int(imga[x+b,y+a]))
                    soma.sort()
                    median = statistics.median(soma)
                    if(col < alturanova and lin < larguranova):
                        imgs[col,lin]= median
                    y = y + indlar
                    lin = lin + 1
                else:
                    y = y + 1
                indice = indice - round(indice)
                indice = indice + medlar
                indlar = 0
                indlar = round(indice)
                median = 0
                soma.clear()
            indicex = indicex - round(indicex)
            indicex = indicex + med
            indalt = 0
            indalt = round(indicex)
            x = x + indalt
            col = col + 1
            lin = 0
            y = 0
    return(imgs)

def gravacao(redimensao):
    cv2.imshow("Arquivo",redimensao)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("ArquivoSaida.jpg", redimensao)


foto = input("Digite o nome da foto com sua extencao: ")
ntons = int(input("Escolha entre 2, 4, 8, 16, 32, 64 ou 128 niveis de cinza: "))
medida = (int(input("Valor de reducao de pixels em %: ")))/100
metodo = input("Qual metodo utilizado na reducao: media, moda ou mediana: ")

img = cv2.imread(foto, 0)
altura, largura = img.shape[:2]
alturanova = round(altura*medida)
larguranova = round(largura*medida)
imga = img
imgs = np.zeros((alturanova,larguranova), np.uint8)

nivelcinza= mudanivel(imga, altura, largura, img)
redimensao = redimencionar(imgs, altura, largura, alturanova, larguranova, medida, nivelcinza, metodo)
gravacao(redimensao)

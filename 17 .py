metrosQuadrados = float(input("Digite a quantidade de metros a serem pintados: "))
condicao = float(input("Digite o tipo de tinta desejado 1 para lata dois para galao ou 3 para ambos: "))
litrosDeTinta = metrosQuadrados / 3
precoLata = 80
precoGalao = 25
LlataDeTinta = 18
lGalao = 3.6
latadeTinta = int(litrosDeTinta / LlataDeTinta)
galao = litrosDeTinta / lGalao
litrosComprados = 0
latasCompradas = 0
galoesComprados = 0
litrosRestantes = 0
latasEGaloesComprados = 0

def ComprarLata():

    if litrosDeTinta != 0 :
        latasCompradas = 1
        litrosComprados = 18
        while(litrosComprados <= litrosDeTinta):
            latasCompradas = latasCompradas + 1
            litrosComprados = litrosComprados + 18
            
            
    P_LataDeTinta = latasCompradas * precoLata    
    print("Você comprou %d Latas de tinta e pagará %d R$" % (latasCompradas,P_LataDeTinta)) 
    

def Comprargalao():
    if litrosDeTinta != 0 :
        galoesComprados = 1
        litrosComprados = 3.6
        while(litrosComprados <= litrosDeTinta):
            galoesComprados = galoesComprados + 1
            litrosComprados = litrosComprados + 3.6
        
    P_GalaoDeTinta = galoesComprados * precoGalao        
    print("Você comprou %d Galões de tinta e pagará %d R$" % (galoesComprados,P_GalaoDeTinta)) 

def ComprarMisto():
    if litrosDeTinta != 0 :
        litrosRestantes = litrosDeTinta
        if litrosDeTinta >= 18 :
            litrosComprados = 18
            latasCompradas = 1
            galoesComprados = 0
            litrosRestantes = litrosDeTinta - litrosComprados
            while(litrosRestantes < litrosDeTinta and litrosRestantes >= 18) :
                litrosComprados = litrosComprados + 18
                latasCompradas = latasCompradas + 1
                galoesComprados = 0
                litrosRestantes = litrosDeTinta - litrosComprados
            while(litrosRestantes <= litrosDeTinta and litrosRestantes >= 3.6) :
                litrosComprados = litrosComprados + 3.6
                galoesComprados = galoesComprados + 1
                litrosRestantes = litrosDeTinta - litrosComprados
                if litrosRestantes < 3.6 :
                    galoesComprados = galoesComprados + 1
        elif litrosRestantes < 3.6 :
            litrosComprados = 3.6
            latasCompradas = 0
            galoesComprados = 1
            litrosRestantes = litrosDeTinta
            latasEGaloesComprados = 1
            
    porCento = float(((latasCompradas * 80) + (galoesComprados * 25)) * ( 0.1))
    latasEGaloesComprados = float(((latasCompradas * 80) + (galoesComprados * 25)) - porCento)
    latasEGaloesCompradosTXT = str(latasEGaloesComprados)
    print("Você comprou %d Latas de tinta" % (latasCompradas)) 
    print("Você comprou %d Galoes de tinta" % (galoesComprados)) 
    print("Valor da compra e 10 por cento de desconto "+ latasEGaloesCompradosTXT +"  R$"  )
    


if condicao == 1 :
    ComprarLata()
elif condicao == 2 :
    Comprargalao()
elif condicao == 3 :
    ComprarMisto()






        
    

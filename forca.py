###################################################
#-------------------------------------------------#
#----------------Jogo de forca--------------------#
#-----------Autor: Mayk Caldas -------------------#
#------------Feito em 20/02/2019------------------#
#--------Em uma noite antes do sono bater---------#
#-------------------------------------------------#
###################################################



#####################################
### ESCOLHA A PALAVRA PARA JOGAR ####
#####################################

palavra="bicicleta"

#####################################
## NÃO ALTERE MAIS NADA NO CÓDIGO ###
#####################################


erros=0
letrasErradas=[]

forca="-"*len(palavra)

print(forca)

while (erros < 6):
    chute=input("Tente uma letra: ")
    
    while (chute.isalpha() != True):
        print("O input deve ser uma letra")
        chute=input("Tente uma letra: ")

    if chute in palavra:
        for k in range(palavra.count(chute)):
            posicao=palavra.find(chute)
            forca = forca[0:posicao]+chute+forca[posicao+1:]
            palavra=palavra.replace(chute,"-",1)
        print(forca)
        print("")

        if palavra=="-"*len(palavra):
            print("Ganhoooou!")
            break
    else:
        erros+=1
        letrasErradas.append(chute)
        
        if erros == 6:
            print("Mórreu")
            break
        
        print("Errou. E já errou essas aqui:")
        print(letrasErradas)
        print("")
        print("Tenta de novo: ")
        print(forca)
        print("")
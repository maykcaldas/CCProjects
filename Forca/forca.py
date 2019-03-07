###################################################
#-------------------------------------------------#
#----------------Jogo de forca--------------------#
#-----------Author: Mayk Caldas ------------------#
#-------------Done in 20/02/2019------------------#
#--------In a night before become asleepy --------#
#-------------------------------------------------#
###################################################



#####################################
####### CHOOSE A WORD TO PLAY #######
#####################################

palavra="bicicleta"

#############################################
## DO NOT CHANGE ANYTHING ELSE IN THE CODE ##
#############################################


import os

erros=0
letrasErradas=[]

forca="-"*len(palavra)

print(forca)

while (erros < 6):
    chute=input("Take a guess: ")
    
    while (chute.isalpha() != True):
        print("The input should be just a character")
        chute=input("Take a guess: ")

    if chute in palavra:
        for k in range(palavra.count(chute)):
            posicao=palavra.find(chute)
            forca = forca[0:posicao]+chute+forca[posicao+1:]
            palavra=palavra.replace(chute,"-",1)
        print(forca)
        print("")

        if palavra=="-"*len(palavra):
            print("Yeeeeay! You won!")
            break
    
    elif chute in letrasErradas or chute in forca:
        print("You have already tried this one.")
        print("You had already wrong those ones:")
        print(letrasErradas)
        print("\n Try again")
        print(forca)
        
    else:
        erros+=1
        letrasErradas.append(chute)
        
        if erros == 6:
            print("Just died")
            break
        
        print("{0} mistakes! And you already wrong those ones:".format(erros))
        print(letrasErradas)
        print("")
        print("Try again: ")
        print(forca)
        print("")

#That is needed to pause when running in a windows environment
#os.system("Pause")

from tkinter import *
from functools import partial 

import os

pasta = os.path.dirname(__file__)

tipoDeComodo = ""
#numComodos = 0
potFinal = 0.0
consuFinal = 0.0
larg = 0.0 
comp = 0.0
tomadas = 0


janela = Tk()
janela.title("Levantamento e Previsão")

imgCasa = PhotoImage(file = pasta+"\\casaBegeGrande.png")

label_imagem = Label(janela,image = imgCasa )

texto0 = Label(janela)  
texto1 = Label(janela)  
texto2 = Label(janela)  
texto3 = Label(janela)
legendaLarg = Label(janela)
legendaComp = Label(janela)

entraLarg = Entry(janela)
entraComp = Entry(janela)
entraQuant = Entry(janela)
entraComo = Entry(janela)
entraEletro1 = Entry(janela)
entraEletro2 = Entry(janela)
entraEletro3 = Entry(janela)

botao = Button(janela) 




def finalizando():
    global potFinal
    global consuFinal
    global tomadas

    entraEletro1.grid_remove()
    entraEletro2.grid_remove()
    entraEletro3.grid_remove()
    botao.grid_remove()
    
    texto0['text'] = "Resultado:"
    texto0.grid(column=0, row=1, padx=10, pady=10)

    texto1['text'] = f'''
    O cálculo da potência ativa total resulta em {potFinal} W. '''
    texto1.grid(column=0, row=2, padx=10, pady=10)

    texto2['text'] = f'''
    A previsao de consumo é de {consuFinal} kWh. '''
    texto2.grid(column=0, row=3, padx=10, pady=10)

    texto3['text'] = f'''
    Esta residência deverá ter, pelo menos, {tomadas} tomadas. '''
    texto3.grid(column=0, row=4, padx=10, pady=10)



    
    
    



# início do calculo *******************************************************************************

def calculaComodo(numComodos):
    #global numComodos
    global potFinal
    global consuFinal
    global tipoDeComodo
    global larg
    global comp 
    global tomadas

    #tipoDeComodo = ((entrada12.get()).strip()).lower()
    larg = float(larg)
    comp = float(comp)

    area = larg * comp
    perimetro = 2*larg + 2*comp

    # calculo do quarto************************************************
    if tipoDeComodo == "quarto" or tipoDeComodo == "dormitorio" :
        
        #calculo da previsão de consumo       
        arcondicionado = ((entraEletro1.get()).strip()).lower()
        if arcondicionado == "tem" or arcondicionado == "sim":
            arcondicionado = 1 
        else:
            arcondicionado = 0

        televisao = ((entraEletro2.get()).strip()).lower()
        if televisao == "tem" or televisao == "sim":
            televisao = 1
        else:
            televisao = 0
    
        #calculo da previsão total de consumo 
        consuTotal = televisao * 18  + arcondicionado * 170   #em kwh



        #Agora vou fazer o cálculo da potência de iluminação
        if area > 6.0 :
            area = area - 6.0
            acres = int( area/4.0 )
            ilum = ( 100.0 + acres * 60.0 )  # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)
        else :
            ilum = 100.0                     # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)
    
        potTotalIlum = ilum * 1.0            #convertendo em potência ativa (que é a potência em W, a potência do mundo real, digamos assim...)
    
        # Agora, fazendo o cálculo da potência das tomadas
        numTom = int(perimetro / 5.0)
        if perimetro % 5 : 
            numTom = numTom + 1
    
        #numTom = numTom + 1  # para se ter uma tomada a mais em relação à quantidade mínima de tomadas
        ptu = numTom * 100.0                # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)

        potTotalTom = ptu * 0.8             #convertendo em potência ativa (que é a potência em W, a potência do mundo real, digamos assim...)

        # E agora o cálculo da potência total deste cômodo.
        potTotal = potTotalIlum +potTotalTom

        tomadas += numTom 



    if tipoDeComodo == "sala" or tipoDeComodo == "sala de estar" or tipoDeComodo == "sala de visita" :
        
        #calculo da previsão de consumo       
        arcondicionado = ((entraEletro1.get()).strip()).lower()
        if arcondicionado == "tem" or arcondicionado == "sim":
            arcondicionado = 1 
        else:
            arcondicionado = 0

        televisao = ((entraEletro2.get()).strip()).lower()
        if televisao == "tem" or televisao == "sim":
            televisao = 1
        else:
            televisao = 0
    
        #calculo da previsão total de consumo 
        consuTotal = televisao * 25  + arcondicionado * 240   #em kwh

        #Agora vou fazer o cálculo da potência de iluminação
        if area > 6.0 :
            area = area - 6.0
            acres = int( area/4.0 )
            ilum = ( 100.0 + acres * 60.0 )  # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)
        else :
            ilum = 100.0                     # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)
    
        potTotalIlum = ilum * 1.0            #convertendo em potência ativa (que é a potência em W, a potência do mundo real, digamos assim...)
    
        # Agora, fazendo o cálculo da potência das tomadas
        numTom = int(perimetro / 5)
        if perimetro % 5 : 
            numTom = numTom + 1
    
        #numTom = numTom + 1  # para se ter uma tomada a mais em relação à quantidade mínima de tomadas
        ptu = numTom * 100.0                # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)

        potTotalTom = ptu * 0.8             #convertendo em potência ativa (que é a potência em W, a potência do mundo real, digamos assim...)

        # E agora o cálculo da potência total deste cômodo.
        potTotal = potTotalIlum +potTotalTom

        tomadas += numTom 



    # calculo do corredor, ou hall, ou copa
    if tipoDeComodo == "hall" or tipoDeComodo == "corredor" or tipoDeComodo == "copa":

        consuTotal = 0.0 

        #Agora vou fazer o cálculo da potência de iluminação
        if area > 6.0 :
            area = area - 6.0
            acres = int( area/4.0 )
            ilum = ( 100.0 + acres * 60.0 )  # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)
        else :
            ilum = 100.0                     # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)
    
        potTotalIlum = ilum * 1.0            #convertendo em potência ativa (que é a potência em W, a potência do mundo real, digamos assim...)
    
        # Agora, fazendo o cálculo da potência das tomadas
        numTom = int(perimetro / 5)
        if perimetro % 5 : 
            numTom = numTom + 1
    
        #numTom = numTom + 1  # para se ter uma tomada a mais em relação à quantidade mínima de tomadas
        ptu = numTom * 100.0                # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)

        potTotalTom = ptu * 0.8             #convertendo em potência ativa (que é a potência em W, a potência do mundo real, digamos assim...)

        # E agora o cálculo da potência total deste cômodo.
        potTotal = potTotalIlum +potTotalTom

        tomadas += numTom 



     
    if tipoDeComodo == "cozinha" :
        
        #fazendo primeiro o calculo da previsao de consumo   
        torneira = ((entraEletro1.get()).strip()).lower()
        if torneira == "tem" or torneira == "sim":
            torneira = 1
        else :
            torneira = 0

        fogao = ((entraEletro2.get()).strip()).lower()
        if fogao == "tem" or fogao == "sim":
            fogao = 1
        else :
            fogao = 0

        geladeira = ((entraEletro3.get()).strip()).lower()
        if geladeira == "tem" or geladeira == "sim":
            geladeira = 1
        else :
            geladeira = 0

        consuTotal = torneira * 52.5  + fogao * 12 + geladeira * 40  #em kwh

        
        
        #Agora vou fazer o cálculo da potência de iluminação
        if area > 6.0 :
            area = area - 6.0
            acres = int( area/4.0 )
            ilum = ( 100.0 + acres * 60.0 )  # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)
        else :
            ilum = 100.0                     # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)
    
        potTotalIlum = ilum * 1.0            #convertendo em potência ativa (que é a potência em W, a potência do mundo real, digamos assim...)

        
        if area > 6.0 :
            # Agora, fazendo o cálculo da potência das tomadas
            numTom = int( perimetro / 3.5)
            if perimetro % 3.5 : 
                numTom = numTom + 1
        else :
            numTom = 1    
    
        if numTom > 3 :
            numTom = numTom - 3
            ptu = 3 * 600 + numTom * 100
        else :
            ptu = numTom * 600.0                # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)

        potTotalTom = ptu * 0.8             #convertendo em potência ativa (que é a potência em W, a potência do mundo real, digamos assim...)

        # E agora o cálculo da potência total deste cômodo.
        potTotal = potTotalIlum + potTotalTom  + 5000 + 500 

        tomadas += numTom + 2



         
    if tipoDeComodo == "lavanderia" or tipoDeComodo == "área de serviço" :
        
        #fazendo calculo da previsao de consumo
        maqLavar = ((entraEletro1.get()).strip()).lower()
        if maqLavar == "tem" or maqLavar == "sim":
            maqLavar = 1 
        else:
            maqLavar = 0

        maqSecar = ((entraEletro2.get()).strip()).lower()
        if maqSecar == "tem" or maqSecar == "sim":
            maqSecar = 1
        else:
            maqSecar = 0

        consuTotal = maqLavar * 52.5  + maqSecar * 12  #em kwh

        #Agora vou fazer o cálculo da potência de iluminação
        if area > 6.0 :
            area = area - 6.0
            acres = int( area/4.0 )
            ilum = ( 100.0 + acres * 60.0 )  # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)
        else :
            ilum = 100.0                     # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)
    
        potTotalIlum = ilum * 1.0            #convertendo em potência ativa (que é a potência em W, a potência do mundo real, digamos assim...)
    
        if area > 6.0 :
            # Agora, fazendo o cálculo da potência das tomadas
            numTom = int( perimetro / 3.5)
            if perimetro % 3.5 : 
                numTom = numTom + 1
        else :
            numTom = 1    
    
    
        if numTom > 3 :
            numTom = numTom - 3
            ptu = 3 * 600 + numTom * 100
        else :
            ptu = numTom * 600.0                # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)

        potTotalTom = ptu * 0.8             #convertendo em potência ativa (que é a potência em W, a potência do mundo real, digamos assim...)

        # E agora o cálculo da potência total deste cômodo.
        potTotal = potTotalIlum + potTotalTom + 1000 + 6000

        tomadas += numTom + 2

    
   
    if tipoDeComodo == "banheiro" or tipoDeComodo == "banho" :
        
        #fazendo calculo da previsao de consumo
        chuveiro = ((entraEletro1.get()).strip()).lower()
        if chuveiro == "tem" or chuveiro == "sim":
            chuveiro = 1 
        else:
            chuveiro = 0

        consuTotal = chuveiro * 70  #em kwh

        #Agora vou fazer o cálculo da potência de iluminação
        if area > 6.0 :
            area = area - 6.0
            acres = int( area/4.0 )
            ilum = ( 100.0 + acres * 60.0 )  # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)
        else :
            ilum = 100.0                     # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)
    
        potTotalIlum = ilum * 1.0            #convertendo em potência ativa (que é a potência em W, a potência do mundo real, digamos assim...)
    
        if area > 6.0 :
            # Agora, fazendo o cálculo da potência das tomadas
            numTom = int( perimetro / 3.5)
            if perimetro % 3.5 : 
                numTom = numTom + 1
        else :
            numTom = 1    
    
    
        if numTom > 3 :
            numTom = numTom - 3
            ptu = 3 * 600 + numTom * 100
        else :
            ptu = numTom * 600.0                # aqui a potência está em VA, uma potência aparente (não é aquela potência do mundo real, digamos assim...)

        potTotalTom = ptu * 0.8             #convertendo em potência ativa (que é a potência em W, a potência do mundo real, digamos assim...)

        # E agora o cálculo da potência total deste cômodo.
        potTotal = potTotalIlum + potTotalTom + 5600

        tomadas += numTom + 1

     

    potFinal += potTotal       #esse é do da NBR5410
    consuFinal += consuTotal    #é da previsão de consumo   

    entraEletro1.delete(0, 'end')
    entraEletro1.grid_remove()
    entraEletro2.delete(0, 'end')
    entraEletro2.grid_remove()
    entraEletro3.delete(0, 'end')
    entraEletro3.grid_remove()
    
    texto1.grid_remove()
    texto2.grid_remove() 

    numComodos -= 1
    if numComodos == 0 :
        finalizando()
    else:
        dimensoesComodo(numComodos)


# termina o cálculo ***************************************************************************************









def eletronicosComodo(numComodos):
    global tipoDeComodo

    
    if tipoDeComodo == "quarto" or tipoDeComodo == "dormitorio" or tipoDeComodo == "sala" or tipoDeComodo == "sala de estar" or tipoDeComodo == "sala de visita" :
        texto0['text'] = "Tem ar-condicionado nesse cômodo?"
        texto0.grid(column=0, row=1, padx=10, pady=10)
        
        entraEletro1.grid(column=0, row=2, padx=10, pady=10)
        
        texto1['text'] = "Tem televisão?"
        texto1.grid(column=0, row=3, padx=10, pady=10)
        
        entraEletro2.grid(column=0, row=4, padx=10, pady=10)

        botao['text'] = "seguinte"
        botao['command'] = partial( calculaComodo, numComodos)
        botao.grid(column=0, row=5, padx=10, pady=10)

  
    if tipoDeComodo == "hall" or tipoDeComodo == "corredor" or tipoDeComodo == "copa" :

        calculaComodo(numComodos)


    if tipoDeComodo == "cozinha" :
        texto0['text'] = "Tem torneira elétrica?"
        texto0.grid(column=0, row=1, padx=10, pady=10)
        
        entraEletro1.grid(column=0, row=2, padx=10, pady=10)
        
        texto1['text'] = "Tem fogão elétrico?"
        texto1.grid(column=0, row=3, padx=10, pady=10)

        entraEletro2.grid(column=0, row=4, padx=10, pady=10)

        texto2['text'] = "Tem geladeira?"
        texto2.grid(column=0, row=5, padx=10, pady=10)

        entraEletro3.grid(column=0, row=6, padx=10, pady=10)

        botao['text'] = "seguinte"
        botao['command'] = partial( calculaComodo, numComodos)
        botao.grid(column=0, row=7, padx=10, pady=10)
        

    if tipoDeComodo == "lavanderia" or tipoDeComodo == "área de serviço" :
        texto0['text'] = "Tem máquina de lavar?"
        texto0.grid(column=0, row=1, padx=10, pady=10)
        
        entraEletro1.grid(column=0, row=2, padx=10, pady=10)
        
        texto1['text'] = "Tem máquina secadora?"
        texto1.grid(column=0, row=3, padx=10, pady=10)

        entraEletro2.grid(column=0, row=4, padx=10, pady=10)

        botao['text'] = "seguinte"
        botao['command'] = partial( calculaComodo, numComodos)
        botao.grid(column=0, row=5, padx=10, pady=10)


    if tipoDeComodo == "banheiro" or tipoDeComodo == "banho" :
        texto0['text'] = "Tem chuveiro elétrico?"
        texto0.grid(column=0, row=1, padx=10, pady=10)
        
        entraEletro1.grid(column=0, row=2, padx=10, pady=10)
        
        botao['text'] = "seguinte"
        botao['command'] = partial(calculaComodo, numComodos)
        botao.grid(column=0, row=3, padx=10, pady=10)

        




def preparaEletro(numComodos):
    global tipoDeComodo
    global larg  
    global comp  

    tipoDeComodo = ((entraComo.get()).strip()).lower()

    larg = entraLarg.get()
    comp = entraComp.get()
    
    texto1.grid_remove()   
    legendaLarg.grid_remove() 
    legendaComp.grid_remove() 
    entraComo.delete(0, 'end')
    entraComo.grid_remove() 
    entraLarg.delete(0, 'end')
    entraLarg.grid_remove()
    entraComp.delete(0, 'end')
    entraComp.grid_remove()

    eletronicosComodo(numComodos)







def dimensoesComodo(numComodos):  #aqui também é perguntado o tipo de cômodo
    
    texto0['text'] = "Qual é o cômodo?"
    texto0.grid(column=0, row=1, padx=10, pady=10)
    
    entraComo.grid(column=0, row=2, padx=10, pady=10)

    texto1['text'] = "Digite a largura e o comprimento: "
    texto1.grid(column=0, row=3, padx=10, pady=10)
    
    legendaLarg['text'] = "Largura: "
    legendaLarg.grid(column=0, row=4, padx=1, pady=1)
    entraLarg.grid(column=0, row=5, padx=10, pady=10)

    legendaComp['text'] = "Comprimento: "
    legendaComp.grid(column=0, row=6, padx=1, pady=1)
    entraComp.grid(column=0, row=7, padx=10, pady=10)

    botao['text'] ="seguinte"
    botao['command'] = partial(preparaEletro,numComodos)
    botao.grid(column=0, row=8, padx=10, pady=10)






def  decidirOqueFazer():
    #global numComodos
    numComodos = int(entraQuant.get())
    entraQuant.grid_remove()
    dimensoesComodo(numComodos)




def numeroComodos():
    
    texto0['text'] = "Quantos cômodos tem a casa?"
    texto0.grid(column=0, row=1, padx=10, pady=10)

        
    entraQuant.grid(column=0, row=2, padx=10, pady=10)
    
    botao['text'] = "seguinte"   
    botao['command'] = decidirOqueFazer   
    botao.grid(column=0, row=3, padx=10, pady=10)    
    

#***************************************************************************************
#Apresentação inicial       

label_imagem.grid(column=0, row=0, padx=10, pady=10)

texto0['text'] = f'''
Olá, aqui você pode fazer um levantamento da 
potência total que uma residência pode tomar,
em consonância com a NBR 5410.''' 
texto0.grid(column=0, row=1, padx=10, pady=10)


botao['text'] = "  Começar  "
botao['command'] = numeroComodos
botao.grid(column=0, row=2, padx=10, pady=10)


janela.mainloop()



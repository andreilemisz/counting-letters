# Código para escrever uma frase e identificar #
# qual ou quais letras apareceram mais vezes #

letra_atual = ""    # Letra usada pelo loop na sua iteração
qtd_vezes_letra_atual = 0   # Quantas repetições da letra atual existem
qtd_vezes_letra_anterior = 0    # Verificar se a letra anterior teve mais repetições
letra_mais_apareceu = ""    # Primeira letra do loop que mais apareceu
qtd_letra_mais_apareceu = 0 # Número de vezes que apareceu a letra mais repetida
segunda_letra_mais_apareceu = ""    # Se houver uma segunda letra com o mesmo número de repetições
terceira_letra_mais_apareceu = ""   # Se houver uma terceira que também tem o mesmo número
contador = 0    # Contador para a iteração na palavra ou frase

frase = input("Escreva uma frase ou palavra: ").lower()

# Início do ciclo que vai verificar letra por letra o seu tamanho
while contador < len(frase):
    letra_atual = frase[contador]
    qtd_vezes_letra_atual = frase.count(letra_atual)
    
    # Momento de eliminar os espaços vazios para que não sejam computados
    if letra_atual == " ":
        contador += 1
        continue
    
    # Nesse momento o programa vai identificar se a letra atual mais utilizada é 
    # diferente da letra mais utilizada com o mesmo número de repetições. Assim é 
    # possível encontrar até 3 letras que tenham o mesmo número de usos
    if qtd_vezes_letra_atual == qtd_vezes_letra_anterior and letra_atual != letra_mais_apareceu:
        if segunda_letra_mais_apareceu == "":
            segunda_letra_mais_apareceu = letra_atual
        
        elif letra_atual != segunda_letra_mais_apareceu and terceira_letra_mais_apareceu == "":
            terceira_letra_mais_apareceu = letra_atual
        
        else:
            contador += 1
            continue
    
    # Momento de armazenar na variável a letra mais utilizada e a sua quantidade de repetições
    if qtd_vezes_letra_atual > qtd_vezes_letra_anterior:
        letra_mais_apareceu = letra_atual
        qtd_letra_mais_apareceu = qtd_vezes_letra_atual
        qtd_vezes_letra_anterior = qtd_vezes_letra_atual
    
    contador += 1

# Mostra dos resultados com base na quantidade de letras que mais se repetiram, até 3
if terceira_letra_mais_apareceu != "":
    print(f'As três letras que mais apareceram foram "{letra_mais_apareceu}", "{segunda_letra_mais_apareceu}",' \
        f' e "{terceira_letra_mais_apareceu}", que apareceram {qtd_letra_mais_apareceu}x. ')
    
elif segunda_letra_mais_apareceu != "":
    print(f'As duas letras que mais apareceram foram "{letra_mais_apareceu}" e "{segunda_letra_mais_apareceu}",' \
        f' que apareceram {qtd_letra_mais_apareceu}x. ')
    
else:
    print(f'A letra que mais apareceu foi "{letra_mais_apareceu}", que apareceu {qtd_letra_mais_apareceu}x. ')
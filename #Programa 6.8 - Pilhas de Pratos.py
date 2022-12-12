#Programa 6.8 - Pilhas de Pratos
prato = 5 
pilha = list(range(1, prato + 1 ))
while True :
    print(f"\nExistem {len(pilha)} pratos na pilha")
    print(f"Pilha atual: {pilha}")
    print("Digite E para empilhar um novo prato,")
    print("ou D para desempilhar. S para sair.")
    operação = input("Operação (E, D ou S):")
    if operação == 'D':
        if len(pilha) > 0 :
            lavado = pilha.pop(-1)
            print(f'Prato {lavado} lavado')
        else:
            print('pilha vazia! nada para lavar.')
    elif operação == 'E' :
        prato += 1 # Novo Prato
        pilha.append(prato)
    elif operação == "S":
        break
    else:
        print("Operação inválida! Digite apenas E, D ou S!")
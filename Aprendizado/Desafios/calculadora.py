

opcao = int(input("Qual operação você quer fazer ?: 1 - soma, 2 - subtração, 3 - multiplicação, 4 - divisão"))


if opcao == 1:
    numA = int(input("Digite o primeiro numero: "))
    numB = int(input("Digite o primeiro numero: "))
    
    resultado = numA + numB
    
    print(resultado)
    
elif opcao == 2 :
    numA = int(input("Digite o primeiro numero: "))
    numB = int(input("Digite o primeiro numero: "))
    
    resultado = numA - numB
    
    print(resultado)
    
elif opcao == 3 :
    numA = int(input("Digite o primeiro numero: "))
    numB = int(input("Digite o primeiro numero: "))
    
    resultado = numA * numB
    
    print(resultado)
    
elif opcao == 4 :
    numA = int(input("Digite o primeiro numero: "))
    numB = int(input("Digite o primeiro numero: "))
    resultado = numA / numB
    
    print(resultado)
    
else:
    print("Opção inválida")
# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print('Selecione o número da  operação desejada: \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')

escolha = input("Digite sua opção (1/2/3/4): ")

def soma():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    soma = num1 + num2
    print(num1,"+",num2,"=",soma)
    
def subtracao():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    subtracao = num1 - num2
    print(num1,"-",num2,"=",subtracao)
    
def multiplicacao():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    multiplicacao = num1 * num2
    print(num1,"x",num2,"=",multiplicacao)
    
def divisao():
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    divisao = num1 / num2
    print(num1,"/",num2,"=",divisao)


if escolha == '1':
    soma()
elif escolha == '2':
    subtracao()
elif escolha == '3':
    multiplicacao()
elif escolha == '4':
    divisao()
else:
    print("Escolha inválida!")
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 14:22:42 2024

@author: 202307164143, Lais Facure IBMEC Centro Direito
"""
print("Olá", "mundo", sep="-") # Saída: Olá-mundo
print("Olá", "Python", end="!\n") # Saída: Olá Python!
# Saída: 18/04/2023 (formato de data)
print("18", "04", "2023", sep="/")
# Saída: nome; sobrenome; email (útil em CSVs)
print("nome", "sobrenome", "email", sep="; ")
print("Loading", end=" ")
print("[OK]") # Saída: Loading [OK]
#nome = input("Digite seu nome: ")
#print("Olá", nome)



#nome = input("Digite seu nome: ")
#print("Olá", nome)

#itens = input("Digite itens separados por vírgula: ").split(',')
#print("Itens:", itens)

#idade = int(input("Digite sua idade: "))
#print("Daqui a cinco anos, você terá", idade + 5, "anos.")

#altura = float(input("Digite sua altura em metros: "))
#print("Sua altura é", altura, "metros.")

def trinta_por_cento():
    print("Digite números para adicionar à lista (digite 'done' para terminar):")
    numeros = []
    while True:
        entrada = input()
        if entrada.lower() == 'done':
            break
        else:
            numeros.append(int(entrada))
    print("Números coletados:", numeros)


#7 de maio, exercicio 1.
def imprimir_informacoes():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    cidade = input("Digite a cidade: ")
    print("Nome:", nome, end=" - ")
    print("Idade:", idade, end=" - ")
    print("Cidade:", cidade + "!")
imprimir_informacoes()

#exercicio 2.
def calcular_operacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: divisão por zero.")
            return

    print("Resultado:", resultado)


calcular_operacao()

#exercicio 3.
def criar_lista_compras():
    itens = input("Digite os itens da lista de compras, separados por vírgula: ")
    lista_compras = itens.split(", ")

    print("Lista de compras:")
    for i, item in enumerate(lista_compras, start=1):
        print("Item", i, ":", item)


criar_lista_compras()

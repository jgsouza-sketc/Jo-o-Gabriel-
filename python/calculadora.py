print("===== CALCULADORA =====")

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("\nEscolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite a opção: ")

if opcao == "1":
    resultado = numero1 + numero2
    print("Resultado:", resultado)

elif opcao == "2":
    resultado = numero1 - numero2
    print("Resultado:", resultado)

elif opcao == "3":
    resultado = numero1 * numero2
    print("Resultado:", resultado)

elif opcao == "4":
    if numero2 == 0:
        print("Não é possível dividir por zero.")
    else:
        resultado = numero1 / numero2
        print("Resultado:", resultado)

else:
    print("Opção inválida.")

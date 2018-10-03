from business.models import Calculadora as calc

print("------------------")
print("------------------")
print("CALCULADORA MALUCA")
print("------------------")
print("------------------")
print("")
print("Digite 1 para soma")
print("Digite 2 para subtração")
print("Digite 3 para multiplicação")
print("Digite 4 para divisão")

escolha = int(input("--> "))

if escolha == 1:
	numero1 = int(input("Digite o primeiro número: "))
	numero2 = int(input("Digite o primeiro número: "))

	print(calc.soma('', numero1, numero2))

elif escolha == 2:
	numero1 = int(input("Digite o primeiro número: "))
	numero2 = int(input("Digite o primeiro número: "))

	print(calc.subtrai('', numero1, numero2))

elif escolha == 3:
	numero1 = int(input("Digite o primeiro número: "))
	numero2 = int(input("Digite o primeiro número: "))

	print(calc.multiplica('', numero1, numero2))

elif escolha == 4:
	numero1 = int(input("Digite o primeiro número: "))
	numero2 = int(input("Digite o primeiro número: "))

	print(calc.divide('', numero1, numero2))

else:
	print("Entrada inválida...")
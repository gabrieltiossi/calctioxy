def somar(a, b):
   return a + b
def subtrair(a, b):
   return a - b
def multiplicar(a, b):
   return a * b
def dividir(a, b):
   return a / b

print("Escolha uma das operacoes")
print("1: Soma")
print("2: Subtracao")
print("3: Multiplicacao")
print("4: Divisao")
menu = input("Escolha 1, 2, 3 ou 4:")

v1 = int(input("Digite o primeiro numero: "))
v2 = int(input("Digite o segundo numero: "))

if menu == "1":
   print(v1,"+",v2,"=", somar(v1,v2))

elif menu == "2":
   print(v1,"-",v2,"=", subtrair(v1,v2))

elif menu == "3":
   print(v1,"*",v2,"=", multiplicar(v1,v2))

elif menu == "4":
   print(v1,"/",v2,"=", dividir(v1,v2))
else:
   print("Como voce conseguiu errar a escolha do menu?")

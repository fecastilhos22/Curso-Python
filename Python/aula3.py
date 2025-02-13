#estruturas_condicionais
# senha =  int(input("Digite sua senha: "))

# if senha == "1324":
#     print("Acesso liberado")
# else:
#     print("Acesso negado") 

#Desafio1_2
# numero = int(input("Digite um número: "))

# if numero % 2 == 0:
#     print("Esse número é par")

# else:
#     print("Esse número é ímpar")    

#Questao1 (rever a questão por causa do else)
# numero = int(input("Digite um número: "))

# if numero > 0:
#     print("Esse número é par")
# elif numero < 0:
#     print("Esse número é ímpar")    
# elif numero == 0:
#     print("Esse número é zero")
# else:
#     print("Número inválido")        

#Questao_2
# idade = int(input("Digite sua idade: "))

# if idade >= 16:
#      print("Você pode votar!")

# else:
#      print("Você não pode votar!") 

#Questao3 
# nota = int(input("Digite uma nota: "))

# if nota >= 9 and nota < 10:
#      print("Sua nota é A")
# elif nota >= 7:
#      print("Sua nota é B")    
# elif nota >= 5:
#      print("Sua nota é C")
# else:
#      print("Você está reprovado") 

#Questao4 
# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o segundo número: "))
# operacao = str(input("Digite qual operação deseja realizar? "))
# soma = n1 + n2
# subtracao = n1 - n2
# divisao = n1 / n2
# multiplicacao = n1 * n2

# if operacao == "+":
#       print(f"A soma dos números é: {soma}")
# elif operacao == "-":
#       print(f"A subtração dos números é: {subtracao}")  
# elif operacao == "/":
#       print(f"A divisão dos números é: {divisao}")
# elif operacao == "*":
#       print(f"A multiplicacao dos números é: {multiplicacao}")      
# else:
#       print("Operação inválida!")

#Questao5
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura)**2

if imc < 18.5:
      print("Você está baixo do peso")
elif imc > 18.5 and imc < 25:
    #elif imc > 18.5 and <= 25:
      print("Seu peso está normal")    
elif imc > 25 and imc <30 :
      print("Você está com sobrepeso")
else:
      print("Você está obeso") 
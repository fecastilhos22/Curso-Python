#Nível1
#1
# print("Bem vindo ao mundo Python!")

# #2
# nome = str (input("Digite seu nome:"))
# idade = int (input("Digite sua idade:"))
# cidade = str (input("Digite sua cidade:"))
# print (f"Olá, {nome} você tem {idade} anos e mora em {cidade}!")

#3
# soma = 15 + 8
# subtracao = 20 - 5
# multiplicacao = 7 * 4
# divisao = 36 / 6
# print (f"O resultado da soma é: {soma}, da subtração: {subtracao}, da multiplicação é: {multiplicacao} e da divisão é: {divisao} ")

#4
# print (" ---- Tabuada do 7 ----")
# numero = 7
# contador = 1

# while contador <= 10:
#     print(f"{numero} x {contador} = {numero*contador}")
#     tabuada = numero + contador
#     contador = contador + 1

#5
# nome = str (input("Digite seu nome:"))
# print (f"Olá, {nome}! É um prazer conhêce-lo!")

#6
# n1 = int (input("Digite o primeiro número:"))
# n2 = int (input("Digite o segundo número:"))
# soma = n1 + n2
# print(f"A soma dos números é: {soma}!")

#7
# c = float (input("Digite a temperatura em Celsius: "))
# fahrenheit = (c * (9 / 5)) + 32
# print (f"A temperatura que você digitou em Fahrenheit é: {fahrenheit}")

#Desafio
# nome = str(input("Digite seu nome?"))
# idade = int(input("Digite sua idade:"))
# mais_10a = idade + 10
# print (f"Você é o/a {nome}, tens {idade} anos e daqui a 10 anos terá {mais_10a} anos.")

#Nível2
#1
# raio = float(input("Digite o raio de um círculo:"))
# area = 3.14 + (raio)**2
# print(f"A área do círculo é: {area}")

#2
# raio = float(input("Digite o raio da base:"))
# altura = float(input("Digite a altura do cilindro:"))
# v = 3.14 * ((raio)**2 * altura)
# print(f"O volume é: {v}")

#3
# dinheiro = float (input("Digite quanto de dinheiro você tem  R$"))
# cotacao = float (input("Digite a cotação do dolar hoje R$ "))
# valor_em_dolares = dinheiro / cotacao
# print (f"Você tem R$ {dinheiro} em reais e ${valor_em_dolares} em dólares")

#4
# distancia = float(input("Digite a distância que você percorreu em KM: "))
# tempo = int (input("Digite em quantas horas você percorreu esse trajeto: "))
# velocidade_media = distancia / tempo
# print (f"Você percorreu {distancia} km em {tempo} horas e a velocidade média gaste foi de {velocidade_media} km/h")

#5
distancia = float(input("Digite a distância que você irá percorrer em KM: "))
consumo = int (input("Digite o consumo médio de combustível: "))
combustivel = distancia / consumo
print (f"Você irá percorrer {distancia} km e consumirá {consumo} litros em média de combustível, então será necessário abastecer {combustivel} de gasolina")


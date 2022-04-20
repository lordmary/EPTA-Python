# declaração de variaveis e tipos type(t)
inteiro = 5
print(type(inteiro))
flutuante = 5.0
print(type(flutuante))

# operações matemáticas básicas e comparações
# (+ - * / % ** //) / (> < >= <= != ==)

primeiro_valor = 1
segundo_valor = 2
soma = primeiro_valor + segundo_valor
print(soma)
print(segundo_valor - primeiro_valor)
print(segundo_valor * primeiro_valor)
print(10/2)
print(10//2)
print(10%2)
print(5**2)

# booleanos, lógica condicional e operadores lógicos (and, or...)
# True, False, if, else, elif

# if(CONDICAO):
# elif(CONDICAO):
# else:

# condicao_1 and condicao_2
# condicao_1 or condicao_2
# !condicao_1

verdadeiro = True
falso = False

if(verdadeiro):
  print('eh verdadeiro :D')
else:
  print('nunca vai ser printado :(')

# listas
lista_de_compras = ['ovos','maçã','banana','melancia']
lista_de_numeros = [1,2,3,4,5]

# métodos para lista
print('lista de numeros inicial:',lista_de_numeros)
lista_de_numeros.append(6)
print('lista de numeros com um 6 no final:',lista_de_numeros)
lista_de_numeros.insert(0,0)
print('lista de numeros com um 0 inserido na posicao 0:',lista_de_numeros)
print('lista de compras inicial:',lista_de_numeros)
lista_de_compras.remove('maçã')
print(lista_de_compras)
lista_de_compras.sort()
print(lista_de_compras)

# Demonstração for

super_herois = ['batman','homem de ferro','homem aranha']

for super_heroi in super_herois:
  print(super_heroi)

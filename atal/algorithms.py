#coding: utf-8

#Aluno: Pedro Guedes Braga - 115210544

import sys

# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem crescente de matriculas
def retorna_matriculas_decrescente(alist):
	k = 1
	for j in xrange(len(alist)):
		houveTrocas = False	
		for i in xrange(len(alist)-k):
			if alist[i] < alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
				houveTrocas = True
		k = k+1
		if(not houveTrocas):
			break
	
	return alist


# Esse metodo recebe e valor para ser dado o troco e uma lista com os tipos de moedas possiveis
# e retorna o numero minimo de moedas possiveis em que o troco pode ser dado
#
# Caso o valor não possa ser alcançado pela combinação de moedas o valor -1 é retornado Ex: valor = 11  moedas = {5, 10, 25}
# Assuma que existe uma quantidade infinita de cada tipo de moeda

def retorna_minimo_moedas(valor, tipos_moedas):
	print valor, tipos_moedas
	resultado = retorna_minimo_moedas_backtracking(tipos_moedas, valor)
	if resultado == sys.maxint:
		return -1
	else:
		return resultado

def retorna_minimo_moedas_FB(tipos_moedas, valor):
	if valor == 0:
		return 0
	
	resultado = sys.maxint
	
	for moeda in tipos_moedas:
		
		if (moeda <= valor):
			resultado = min(resultado, retorna_minimo_moedas_FB(tipos_moedas, valor - moeda) + 1) 
		
	return resultado	 


# Mochila Binaria interativo
  
# Retorna o valor maximo que cabe na mochila com 
# capacidade peso_maximo
def mochila_binaria(peso_maximo, pesos, valores, n): 
    return dynamic_mochila_binaria(peso_maximo, pesos, valores)



def dynamic_mochila_binaria(peso_maximo, pesos, valor):
	#Inicializa as linhas da matriz com o caso base
	matrix = []
	#Caso base: Para o peso 0, o valor maximo que se consegue eh 0!
	for i in range(len(pesos)):
		matrix.append([0])
	
	#Caso base: Preenchimento da primeira linha da matriz
	for j in range(1, peso_maximo + 1):
		if(pesos[0] > j):
			matrix[0].append(0)
		else:
			matrix[0].append(valor[0])

	#Preenchimento do restante da matriz usando a subestrutura otima!
	for i in range(1, len(pesos)):
		for j in range(1, peso_maximo + 1):
			if(pesos[i] > j):
				matrix[i].append(matrix[i-1][j])
			else:
				matrix[i].append(max(valor[i] + matrix[i-1][j-pesos[i]], matrix[i-1][j]))

	
			
	return matrix[len(pesos) - 1][peso_maximo]


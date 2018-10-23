#coding: utf-8

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


#################### Pratica 2 #############################


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


def retorna_minimo_moedas_backtracking(tipos_moedas, valor):
	return retorna_minimo_moedasBT(tipos_moedas, valor, [])

def retorna_minimo_moedasBT(tipos_moedas, valor, possible_solution):
	tamanho_solution = -1
	if(is_a_solution(possible_solution, valor)):
		return len(possible_solution)
	else:
		for i in range(len(tipos_moedas)):
			possible_solution.append(tipos_moedas[i])
			if(its_promissing(possible_solution, valor)):
				tamanho = retorna_minimo_moedasBT(tipos_moedas, valor, possible_solution)
				if(tamanho_solution == -1):
					tamanho_solution = tamanho
				else:
					if(tamanho_solution >= tamanho):
						tamanho_solution = tamanho
			possible_solution.pop()
	return tamanho_solution

#funcao auxiliar que verifica se um conjunto de moedas corresponde a determinado valor, ou seja, se eh uma solucao
def is_a_solution(moedas, valor):
	sum = 0
	for i in range(len(moedas)):
		sum = sum + moedas[i]
	return sum == valor

#funcao de validacao: Verifica se uma possivel solucao eh promissora. (Necessaria para "descer" a arvore)
#uma possivel solucao eh promissora se a soma das moedas eh menor ou igual
def its_promissing(possible_solution, valor):
	sum = 0
	for i in range(len(possible_solution)):
		sum = sum + possible_solution[i]
	return sum <= valor


print(retorna_minimo_moedas(200, [50,100,150]))



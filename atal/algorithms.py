#coding: utf-8
#Estrategia Gulosa - Aluno: Pedro Guedes Braga
import sys

# Esse metodo recebe uma lista com as matriculas dos alunos
# e retorna essa lista em ordem crescente de matriculas
def retorna_matriculas_decrescente(alist):
	for j in xrange(len(alist)):
		for i in xrange(len(alist)-1):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	return alist

# Esse metodo recebe e valor para ser dado o troco e uma lista com os tipos de moedas possiveis
# e retorna o numero minimo de moedas possiveis em que o troco pode ser dado

# Caso o valor não possa ser alcançado pela combinação de moedas o valor -1 é retornado Ex: valor = 11  moedas = {5, 10, 25}
# Assuma que existe uma quantidade infinita de cada tipo de moeda
def retorna_minimo_moedas(valor, tipos_moedas):
	print valor, tipos_moedas
	return troco_greedy_strategy(valor, tipos_moedas)


# Abordagem gulosa para o problema do troco
def troco_greedy_strategy(valor, tipos_moedas):
	tipos_moedas.sort()
	tipos_moedas.reverse() # decrescente
	troco = []
	i = 0
	while(sum(troco) < valor and i < len(tipos_moedas)):
		if(tipos_moedas[i] + sum(troco) <= valor):
			troco.append(tipos_moedas[i])
		if(tipos_moedas[i] + sum(troco) > valor):
			i = i + 1
	if(sum(troco) == valor):
		return len(troco)
	else:
		return -1
	

def retorna_minimo_moedas_FB(tipos_moedas, valor):
	if valor == 0:
		return 0
	
	resultado = sys.maxint
	
	for moeda in tipos_moedas:
		
		if (moeda <= valor):
			resultado = min(resultado, retorna_minimo_moedas_FB(tipos_moedas, valor - moeda) + 1) 
		
	return resultado	 


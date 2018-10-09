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

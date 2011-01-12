#!/usr/bin/env python
#coding: utf-8
import random
import os
import time



#autor
#Douglas Barbosa dos Santos
#douglas.makubex@gmail.com

#debuger
#Elias

# Controle da Versão: Version "1.5"
#
# version 0.1: 03/01/2011 - Sorteia 6 dezenas aleatoriamente um número de 
#cada lista. Considerar 00 como sendo o número 60.

# version 0.2: 05/01/2011 - Escolhe o número de dezenas que quer jogar.

# version 0.3: 05/01/2011 - Adcionado menu2 para perguntar se quer
# continuar jogando

# version 0.4 - 05/01/2011 -  BUG(RESOLVIDO) - Se colocar letras na 
# primeira pergunta ao invés de numeros na hora em que o programa 
# pedir para sair vai fazer a pergunta
# o mesmo número de vezes que errou na primeira pergunta

# version 0.5 05/01/2011 - Resovido bug que dava erro quando se escolhia
# sair do programa após ter digitado uma opçẽo errada.

# version 0.6 06/01/2011 - Mudado a forma de escolher o numero aleatório.
# Acrecentado o método random.choice() que escolhe aleatóriamente um
# número no range - Foi colocada a trava que impde jogos menores que 6
# dezenas ou maiores que 15 Dezenas. - O programa mostra a aposta com as
# Dezenas ordenadas

# Versão 1.0 06/01/2011 - Todos os Bugs resolvidos até a versão 0.6.

# Versão 1.1 06/01/2011 - Acrescentado a opção de quantos jogos fazer
# de uma unica vez.

# Versão 1.1-1 BETA 06/01/2011 - Melhora na saida dos numeros na tela

# Versão 1.4-Beta - 10/01/2011 - Agora o programa salva em um arquivo 
# na mesma pasta que o programa esta e pergunta se quer imprimir.
# Usa o comando lpr do Linux para imprimir. 

# Versão 1.4.1-Beta - 11/01/2011 - Programa salva arquivo com nome baseado
# na hora e data de criação do arquivo. Função nomeArquivo() - pode-se 
# formatar de varias maneiras.

# Versão 1.5 - 12/01/2011- Programa sem bugs. As mesmas caracteristicas da versão
# beta


# TODO - implementar funcionalidade de impresão também no windows.
versao = '1.5'
def nomeArquivo():
	ano=str(time.localtime()[0])
	mes=str(time.localtime()[1])
	dia=str(time.localtime()[2])
	hora=str(time.localtime()[3])
	min=str(time.localtime()[4])
	seg=str(time.localtime()[5])
	
	nome='mg_%s-%s-%s_%s-%s-%s' %(dia,mes,ano,hora,min,seg)
	return nome

def imprimir(arquivo1):
	resp = raw_input('\tGOSTARIA DE IMPRIMIR O RESULTADO? (s|n) ->')
	if resp == 's' or resp == 'S':
		os.system('lpr %s' %arquivo1)
		print 'JOGO IMPRESSO'

def salvaMostraNaTela(sorteioNum):
	"""Função que mostra na tela os numeros escolhidos
	e salva em um arquivo"""
	 
	arquivo = (nomeArquivo())
	jogomega = open(arquivo,'w')
	jogomega.write('\tGERADO POR MEGASENA-%s\n' %versao)
	jogomega.write('\tARQUIVO %s\n' %arquivo)
	jogomega.write('\t-----------------------')
	for j in sorteioNum:
		print '\n'
		jogomega.write('\n\n')
		for i in j:
			print '\t %2.i' %i,
			jogomega.write("\t%s" %(str(i))+' '),
	jogomega.close()
	print '\n'
	imprimir(arquivo)
	

def embaralhaSorteia(nJgos,nNum):		
	n1 = range(1,61)
	agrupaJogos = []			
	for i in range(nJgos):
		sorteados = []
		contador = 0
		while contador < nNum:
			random.shuffle(n1)
			random.shuffle(n1)
			numSorteado = random.choice(n1)
			if sorteados.count(numSorteado) == 0:
				sorteados.append(numSorteado)
				contador+=1
	
		sorteados.sort()
		agrupaJogos.append(sorteados)
	return agrupaJogos

def menu():
	"""Uma Simples mensagem de inicio do programa"""
	print '	------------------------------------------------'
	print '	GERADOR DE IMPROBABILIDADE ALEATÓRIA DE NÚMEROS'
	print '	ESCOLHA QUANTAS DEZENAS QUER JOGAR'
	print '	------------------------------------------------\n'	
	main() 

def menu2():	
	continuar = raw_input('\tDESEJA CONTINUAR? (s|n)  ')
	if continuar == 's':
		menu()
	else:
		print '\n\tOBRIGADO POR TER JOGADO'
		#exit()
def outro():
	"""Pergunta quantos jogos e quantos numeros por jogo o apostador
	quer fazer."""
	
	try:
		qntJogos = input('\tQUANTOS JOGOS DESEJA FAZER? ->')
		qntNum = int(raw_input('\tQUANTOS NUMEROS DESEJA JOGAR? '))
		if (qntNum < 6 or qntNum > 15):
			print '\tSÃO ACEITAS APENAS DE 6 A 15 DEZENAS!!! '
			outro()
		else:
			print '\t A SUA APOSTA: '
			numSorteados = embaralhaSorteia(qntJogos,qntNum)	
			salvaMostraNaTela(numSorteados)
		print '\n'
	except:
		print '\tAPENAS NUMEROS POR FAVOR'
		outro()	
		
def main():	
	outro()
	menu2() #Entra no menu que pergunta se quer tentar novamente
	
# Inicia o programa 	
if __name__ == "__main__":
	menu()

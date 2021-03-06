#!/usr/bin/env python
#coding: utf-8
import random
import os
import time
import sys


#autor
#Douglas Barbosa dos Santos
#douglas.makubex@gmail.com

#debuger
#Elias

# Controle da Versão: Version "1.5"

# Pega o nome do programa diretamente do parametro de execução,
# no caso é o próprio nome. 

versao = '%s' %(sys.argv[0][:-3])
if versao[:2] == './':
	versao = '%s' %sys.argv[0][2:-3]


def nomeArquivo():
	ano=str(time.localtime()[0])
	mes=str(time.localtime()[1])
	if len(mes)==1:
		mes = '%s%s' %('0',mes)
		
	dia=str(time.localtime()[2])
	if len(dia)==1:
		mes = '%s%s' %('0',dia)
		
	hora=str(time.localtime()[3])
	if len(hora)==1:
		mes = '%s%s' %('0',hora)
		
	min=str(time.localtime()[4])
	if len(min)==1:
		mes = '%s%s' %('0',min)
		
	seg=str(time.localtime()[5])	
	if len(seg) == 1:
		seg = '%s%s' %('0',seg)
	
	nome='MS_%s-%s-%s_%s-%s-%s' %(ano,mes,dia,hora,min,seg)
	return nome

def imprimir(arquivo1):
	resp = raw_input('\tGOSTARIA DE IMPRIMIR O RESULTADO? (s|n) ->')
	if resp == 's' or resp == 'S':
		#os.system('lpr %s' %arquivo1) #desativada por enquanto
		os.system('gedit %s' %arquivo1)
		print '\tJOGO IMPRESSO'

def salvaMostraNaTela(sorteioNum):
	"""Função que mostra na tela os numeros escolhidos
	e salva em um arquivo"""
	 
	arquivo = (nomeArquivo())
	jogomega = open(arquivo,'w')
	jogomega.write('\tGERADO POR : %s\n' %versao)
	jogomega.write('\tARQUIVO %s\n' %arquivo)
	jogomega.write('\t--------------------------------')
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

"""
AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : WILLIAM SIMÕES BARBOSA
  NUSP : 9837646
  Turma: TURMA 07
  Prof.: ALAN DURHAM
"""

def numeroAleatorio(i):
	xZero = 3
	a = 22695477
	b = 1
	m = potencia(2, 32)
	numeroAnterior = xZero
	j = 1
	while (j <= i):
		numeroAtual = (a * numeroAnterior + b) % m
		numeroAnterior = numeroAtual
		j += 1	
	return numeroAtual


def potencia(numero, potencia):
	resultado = 1
	i = 1
	while i <= potencia:
		resultado = numero * resultado
		i += 1		
	return resultado


def imprimePontos(n):
	i = 1
	while i <= n:
		print("*", end = "")
		i += 1
	print("")


def main():
	tipoDeJogo = int(input("Escolha o tipo de jogo (1: Facil; 2: Dificil):"))
	numeroDeJogadas = int(input("Entre com o numero de jogadas:"))
	pontosJogador = 0
	pontosMaquina = 0
	i = 1
	
	if (tipoDeJogo == 1):
		while (i <= numeroDeJogadas):
			numAleatorio = numeroAleatorio(i)

			#print("Faca sua", i, end = "")
			#print("a jogada:", end = "")
			#jogadaPessoa = int(input())
			jogadaPessoa = int(input("Faca sua %da jogada:" %i))

			if numAleatorio <= potencia(2,31):
				jogadaMaquina = 0
			else:
				jogadaMaquina = 1

			print("jogador =", jogadaPessoa, "maquina =", jogadaMaquina, end = " ")

			if jogadaMaquina == jogadaPessoa:
				print("Maquina ganha!")
				pontosMaquina += 1
			else:
				print("Jogador ganha!")
				pontosJogador += 1
			
			print("JOGADOR:", end = " ")
			imprimePontos(pontosJogador)

			print("MAQUINA:", end = " ")
			imprimePontos(pontosMaquina)

			i += 1
		if pontosMaquina > pontosJogador:
			print("A maquina venceu!")
		elif pontosMaquina < pontosJogador:
			print("Voce venceu!")
		else:
			print("Houve empate!")

	elif (tipoDeJogo == 2):
		lance00 = 0 #n de vezes que escolheu 0, sendo que antes escolheu 0
		lance01 = 0 #n de vezes que escolheu 0, sendo que antes escolheu 1
		lance10 = 0 #n de vezes que escolheu 1, sendo que antes escolheu 0
		lance11 = 0 #n de vezes que escolheu 1, sendo que antes escolheu 1

		while(i <= numeroDeJogadas):
			numAleatorio = numeroAleatorio(i)

			#print("Faca sua", i, end = "")
			#print("a jogada:", end = "")
			#jogadaPessoa = int(input())
			jogadaPessoa = int(input("Faca sua %da jogada:" %i))


			if i == 1:
				if numAleatorio <= potencia(2,31):
					jogadaMaquina = 0
				else:
					jogadaMaquina = 1
			else:

				if jogadaAnterior == 0:
					if lance10 > lance00:
						jogadaMaquina = 1
					elif lance10 < lance00:
						jogadaMaquina = 0
					else:
						if numAleatorio <= potencia(2,31):
							jogadaMaquina = 0
						else:
							jogadaMaquina = 1
				elif jogadaAnterior == 1:
					if lance11 > lance01:
						jogadaMaquina = 1
					elif lance11 < lance01:
						jogadaMaquina = 0
					else:
						if numAleatorio <= potencia(2,31):
							jogadaMaquina = 0
						else:
							jogadaMaquina = 1

				if jogadaPessoa == 1:
					if jogadaAnterior == 1:
						lance11 += 1
					elif jogadaAnterior == 0:
						lance10 += 1
				elif jogadaPessoa == 0:
					if jogadaAnterior == 1:
						lance01 += 1
					elif jogadaAnterior == 0:
						lance00 += 1

			print("jogador =", jogadaPessoa, "maquina =", jogadaMaquina, end = " ")

			if jogadaMaquina == jogadaPessoa:
				print("Maquina ganha!")
				pontosMaquina += 1
			else:
				print("Jogador ganha!")
				pontosJogador += 1
			
			print("JOGADOR:", end = " ")
			imprimePontos(pontosJogador)

			print("MAQUINA:", end = " ")
			imprimePontos(pontosMaquina)

			jogadaAnterior = jogadaPessoa
			i += 1
			
		if pontosMaquina > pontosJogador:
			print("A maquina venceu!")
		elif pontosMaquina < pontosJogador:
			print("Voce venceu!")
		else:
			print("Houve empate!")



main()
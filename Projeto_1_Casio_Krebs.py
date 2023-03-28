import csv
import os

# Portas logicas
def AND (a, b):
	if a == 1 and b == 1:	return 1
	else:					return 0

def OR(a, b):
	if a == 1 or b ==1:	return 1
	else:				return 0 

def NOT(a):
	if a == 0:	return 1
	else:		return 0 

def NAND (a, b):
	if a == 1 and b == 1:	return 0
	else:					return 1

def NOR(a, b):
	if a == 0 and b == 0:	return 1
	else:					return 0

def XOR (a, b):
	if a != b:	return 1
	else:		return 0


#########################################################
#
#
#					ATRASO 0
#
#
#########################################################

def print_linha_0(Tempo,w,Circuito_0):
	linha = [Tempo]
	for y in range(26):
		if(Circuito_0[y][1]==True):
			linha.append(Circuito_0[y][3])
	w.writerow(linha)


def atraso_0_aux(portas,Circuito_0):
	ent1 = Circuito_0[ord(portas[2])-ord("A")][3]
	ent2 = 0;
	if (portas[1]!= "NOT"): ent2 = Circuito_0[ord(portas[3])-ord("A")][3]

	if portas[1] == "AND": 		saida = AND(ent1,ent2)
	elif portas[1] == "OR":		saida = OR(ent1,ent2)
	elif portas[1] == "NOT":	saida = NOT(ent1)
	elif portas[1] == "NAND":	saida = NAND(ent1,ent2)
	elif portas[1] == "NOR":	saida = NOR(ent1,ent2)
	elif portas[1] == "XOR":	saida = XOR(ent1,ent2)

	return saida


def atraso_0(DIR,Circuito_0,sinais):

	sinais.append(1)
	sinais.append(1)

	valido = []		

	# Criando o arquivo saida0.csv
	f = open(DIR + 'saida0.csv', 'w', newline='', encoding='utf-8')
	w = csv.writer(f)

	# Gerando cabeçalho
	linha = ["Tempo"]
	for y in range(26):
		if(Circuito_0[y][1]==True):
			linha.append(Circuito_0[y][2])
		if(Circuito_0[y][0]==True):
			if (Circuito_0[y][4]!= "NOT"):
				valido.append([Circuito_0[y][2],Circuito_0[y][4],Circuito_0[y][5],Circuito_0[y][6]])
			else:
				valido.append([Circuito_0[y][2],Circuito_0[y][4],Circuito_0[y][5]])

	w.writerow(linha)

	# Inicializa o contador de relógio
	Tempo = 0

	# Inicializa a pilha de variáveis modificadas
	Modificado = []

	for x in sinais:
		
		# Modificação de sinal
		if (x != 1):
			# Configurando o novo Nivel Lógico do sinal de entrada
			ID = ord(x[0])-ord("A")
			Circuito_0[ID][3]=x[1]

			#Identificando a variável modificada
			Modificado.append(x[0]) 

		# Avanço no tempo
		else:
			while (len(Modificado) != 0):

				sinal_pai = Modificado[0]
				Modificado.pop(0);

				# Identica se o sinal Modificado é entrada de alguma porta lógica 
				for portas in (valido):
					
					att = False

					if (portas[1] != "NOT"):
						if(portas[2] == sinal_pai or portas[3] == sinal_pai):
							att = True

					elif(portas[2] == sinal_pai):
						att = True

					# Atualizar porta lógica?
					if (att):

						saida = atraso_0_aux(portas,Circuito_0)
						ID_saida = ord(portas[0])-ord("A")

						if (Circuito_0[ID_saida][3] != saida):
							Circuito_0[ID_saida][3] = saida
							# Adicona na pilha de sinais Modificados
							if (portas[0] not in Modificado):	
								Modificado.append(portas[0])

			print_linha_0(Tempo,w,Circuito_0)
			Tempo +=1
	f.close()	
	
#########################################################
#
#
#					ATRASO 1
#
#
#########################################################

def print_linha_1(Tempo, w,Circuito_1):
	linha = [Tempo]
	for y in range(26):
		if(Circuito_1[y][1]==True):
			linha.append(Circuito_1[y][3])
	w.writerow(linha)


def atraso_1_aux(portas,Circuito_1):
	ent1 = Circuito_1[ord(portas[2])-ord("A")][3]
	ent2 = 0;
	if (portas[1]!= "NOT"): ent2 = Circuito_1[ord(portas[3])-ord("A")][3]

	if portas[1] == "AND": 		saida = AND(ent1,ent2)
	elif portas[1] == "OR":		saida = OR(ent1,ent2)
	elif portas[1] == "NOT":	saida = NOT(ent1)
	elif portas[1] == "NAND":	saida = NAND(ent1,ent2)
	elif portas[1] == "NOR":	saida = NOR(ent1,ent2)
	elif portas[1] == "XOR":	saida = XOR(ent1,ent2)

	return saida


def atraso_1(DIR,Circuito_1,sinais):

	sinais.append(1)
	sinais.append(1)

	valido = []	

	# Criando o arquivo saida0.csv
	f = open(DIR + 'saida1.csv', 'w', newline='', encoding='utf-8')
	w = csv.writer(f)

	# Gerando cabeçalho
	linha = ["Tempo"]
	for y in range(26):
		if(Circuito_1[y][1]==True):
			linha.append(Circuito_1[y][2])
		if(Circuito_1[y][0]==True):
			if (Circuito_1[y][4]!= "NOT"):
				valido.append([Circuito_1[y][2],Circuito_1[y][4],Circuito_1[y][5],Circuito_1[y][6]])
			else:
				valido.append([Circuito_1[y][2],Circuito_1[y][4],Circuito_1[y][5]])
	w.writerow(linha)

	# Inicializa o contador de relógio
	Tempo = 0

	# Inicializa a pilha de variáveis modificadas
	Modificado = []
	Modificado_filho = []

	for x in sinais:
		
		# Modificação de sinal
		if (x != 1):
			# Configurando o novo NL do sinal de entrada
			ID = ord(x[0])-ord("A")
			Circuito_1[ID][3]=x[1]

			#Identificando a variável modificada
			Modificado.append(x[0])

		# Avanço no tempo
		else:
			print_linha_1(Tempo,w,Circuito_1)

			Tempo +=1
			Modificado_filho = []
			for sinal_pai in (Modificado):

				# Identica se o sinal Modificado é entrada de alguma porta lógica 
				for portas in (valido):

					att = False

					if (portas[1] != "NOT"):
						if(portas[2] == sinal_pai or portas[3] == sinal_pai):
							att = True

					elif(portas[2] == sinal_pai):
							att = True

					if (att):
					
						saida = atraso_1_aux(portas,Circuito_1)
						ID_saida = ord(portas[0])-ord("A")

						if (Circuito_1[ID_saida][3] != saida):
							Circuito_1[ID_saida][3] = saida

							# Identifica quais são os sinais de saida modificados
							Modificado_filho.append(portas[0])
			
			# Adicona os sinais modificanos na piulha para serem 
			# verificados, no ciclo de clock seguinte
			Modificado = []	
			for x in Modificado_filho:	
				if (x not in Modificado):	
					Modificado.append(x)	

	while (len(Modificado) != 0):

		print_linha_1(Tempo,w,Circuito_1)

		Tempo +=1
		Modificado_filho = []
		for sinal_pai in (Modificado):

			for portas in (valido):

				att = False

				if (portas[1] != "NOT"):
					if(portas[2] == sinal_pai or portas[3] == sinal_pai):
						att = True

				elif(portas[2] == sinal_pai):
					att = True

				if (att):
				
					saida = atraso_1_aux(portas,Circuito_1)
					ID_saida = ord(portas[0])-ord("A")

					if (Circuito_1[ID_saida][3] != saida):
						Circuito_1[ID_saida][3] = saida
						Modificado_filho.append(portas[0])

		Modificado = []	
		for x in Modificado_filho:	
			if (x not in Modificado):	
				Modificado.append(x)
	
	print_linha_1(Tempo,w,Circuito_1)
	f.close()
			

#########################################################
#
#
#					MAIN
#
#
#########################################################
def main():

	# Identificando todos os circuitos
	DIR = [] 
	dir_atual = os.listdir()
	for pastas in dir_atual:
		if (os.path.isdir(pastas) and pastas == "test"):
			circuitos = os.listdir(pastas)
			for x in circuitos:
				DIR.append(["test/"+x+"/"])
			
	for dir_circ in DIR:

		try:
			#Inicialização histórico dos circuitos
			Circuito_0 = []
			Circuito_1 = []

			#Inicialização do circuito
			for x in range(26):
				Circuito_0.append([False,False,chr(ord("A")+x),0])
				Circuito_1.append([False,False,chr(ord("A")+x),0])

			#Inicialização dos sinais de entrada
			sinais = []

			sinal_E = []
			sinal_S = []


			# Leitura do circuito
			f = open(dir_circ[0] + 'circuito.hdl', 'r')

			for line in f:
				termos = line.split();

				# Leitura sinal de saida
				ID = ord(termos[0])-ord("A")
				sinal_S.append(termos[0])
				if (termos[0] in sinal_E):
					sinal_E.remove(termos[0])

				# Leitura da porta
				Circuito_0[ID].append(termos[2])	
				Circuito_0[ID][0]=True
				Circuito_0[ID][1]=True
				Circuito_1[ID].append(termos[2])	
				Circuito_1[ID][0]=True
				Circuito_1[ID][1]=True

				# Leitura da primeira entrada
				Circuito_0[ID].append(termos[3])							
				Circuito_0[ord(termos[3])-ord("A")][1]=True
				Circuito_1[ID].append(termos[3])							
				Circuito_1[ord(termos[3])-ord("A")][1]=True
				sinal_E.append(termos[3])

				# Leitura condicional da segunda entrada
				if (termos[2]!= "NOT"): 
					Circuito_0[ID].append(termos[4])	
					Circuito_0[ord(termos[4])-ord("A")][1]=True
					Circuito_1[ID].append(termos[4])	
					Circuito_1[ord(termos[4])-ord("A")][1]=True
					sinal_E.append(termos[4])
			f.close()

			# Leitura do sinais de entrada
			f = open(dir_circ[0] + 'estimulos.txt', 'r')

			for x in sinal_S:
				if (x in sinal_E):
					sinal_E.remove(x)

			aux = 0;
			for line in f:
				if ("+"in line):
					# Identificando o avanço de tempo
					for x in range (int(line[1::])):
						sinais.append(1)
				else:	
					termos = line.split();

					# Interpretando a notação simplificada
					entrada = list(termos[0])
					sinal = list(termos[2])

					for x in range(len(entrada)):
						sinais.append([entrada[x],int(sinal[x])])
			f.close()

			sinais_1 = sinais.copy()

			atraso_0(dir_circ[0],Circuito_0,sinais)
			atraso_1(dir_circ[0],Circuito_1,sinais_1)

			print("Simulação do diretório:",dir_circ,"concluida com sucesso")

		except :
			print("Falha ao abrir os arquivos circuito.hdl e estimulos.txt do diretório:", dir_circ)
			pass
		

if __name__ == "__main__":
    main()
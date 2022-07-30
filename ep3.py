# -*- coding: latin-1 -*-
"""
  AO PREENCHER ESSE CABE�ALHO COM O MEU NOME E O MEU N�MERO USP,
  DECLARO QUE SOU A �NICA PESSOA AUTORA E RESPONS�VEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERC�CIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRU��ES
  DESSE EP E, PORTANTO, N�O CONSTITUEM ATO DE DESONESTIDADE ACAD�MICA,
  FALTA DE �TICA OU PL�GIO.
  DECLARO TAMB�M QUE SOU A PESSOA RESPONS�VEL POR TODAS AS C�PIAS
  DESSE PROGRAMA E QUE N�O DISTRIBU� OU FACILITEI A
  SUA DISTRIBUI��O. ESTOU CIENTE QUE OS CASOS DE PL�GIO E
  DESONESTIDADE ACAD�MICA SER�O TRATADOS SEGUNDO OS CRIT�RIOS
  DIVULGADOS NA P�GINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA N�O SER�O CORRIGIDOS E,
  AINDA ASSIM, PODER�O SER PUNIDOS POR DESONESTIDADE ACAD�MICA.

  Nome : WILLIAM SIM�ES BARBOSA
  NUSP : 9837646
  Turma: 07
  Prof.: ALAN DURHAM

  Refer�ncias: Com exce��o das rotinas fornecidas no enunciado
  e em sala de aula, caso voc� tenha utilizado alguma refer�ncia,
  liste-as abaixo para que o seu programa n�o seja considerado
  pl�gio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em
  https://pt.wikipedia.org/wiki/Quicksort
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""

# **********************************************************
# **                 IN�CIO DA PARTE 1                    **
# **********************************************************


def calcula_id(matriz):
    """ Retorna o valor de identifica��o de uma matriz computada pelo
    algoritmo adler32

    A fun��o :func:'calcula_id' computa um identificador para uma matriz
    usando a seguinte vers�o adaptada do algoritmo de espalhamento Adler32:

        - A = 1 + matriz[0][0] + matriz[0][1] +...+ matriz[m-1][n-1] MOD 65521,
            onde m � o n�mero de linhas e n � o n�mero de colunas da matriz
        - B = (1 + matriz[0][0]) + (1 + matriz[0][0]+matriz[0][1]) + ... +
          (1 + matriz[0][0] + matriz[0][1] + ... + matriz[m-1][n-1]) MOD 65521
        - retorna B * (2**16) + A


    :param matriz: Uma matriz de inteiros
    :type matriz: <class 'list'>
    :return identificador: O identificador inteiro da matriz computado segundo
        a nossa vers�o adaptada do Adler32
    :rtype: <class 'int'>

    :Examples:

    >>> matriz_A = [[0,1,2], [3,4,5]]
    >>> matriz_B = [[3,4,5], [0,1,2]]
    >>> matriz_C = [[0,1], [1,0]]
    >>> matriz_D = [[1,0,2], [3,4,5]]
    >>> calcula_id(matriz_A)
    2686992
    >>> calcula_id(matriz_B)
    4456464
    >>> calcula_id(matriz_C)
    589827
    >>> calcula_id(matriz_D)
    2752528

    .. seealso::
        Consulte o enunciado para um exemplo mais detalhado.
    """
    A = 1
    B = 0
    somaB = 1

    #Determina��o de A e B:
    for i in range(len(matriz)): #la�o para percorrer todas as linhas da matriz
        for j in range(len(matriz[0])): #la�o para percorrer todas as colunas da matriz
            A += matriz[i][j]
            somaB += matriz[i][j]
            B += somaB
    A = A % 65521
    B = B % 65521
            
    return B * (2**16) + A


# ----------------------------------------------------------
# --                  FIM DA PARTE 1                      --
# ----------------------------------------------------------


# **********************************************************
# **                 IN�CIO DA PARTE 2                    **
# **********************************************************


def carrega_identificador(nome_arquivo):
    """ Carrega o identificador de uma imagem presente em um arquivo.

    A fun��o :func:'carrega_identificador' abre um arquivo de nome
    'nome_arquivo' presente na mesma pasta que o programa ep3.py, l� sua
    primeira linha e retorna o inteiro representando o identificador  
    presente nessa linha.

    :param nome_arquivo: String com o nome do arquivo com o identificador
    :type nome_arquivo: <class 'str'>
    :return identificador: Inteiro contendo identificador 
    :rtype: <class 'int'>

    :Example:

    >>> identificador = carrega_identificador('img01.adler32')
    >>> print(identificador)
    297286
    

    .. note::
        Embora pelas regras da disciplina voc� possa assumir que o arquivo
        'nome_arquivo' est� presente na mesma pasta do programa ep3.py,
        boas pr�ticas de programa��o sugerem que para escrita e leitura de
        arquivos, voc� sempre deve verificar � exist�ncia/permiss�es.
        Com rela��o ao identificador, voc� pode assumir que o arquivo cont�m
        um identificador v�lido na primeira linha.
    """
    arquivo = open(nome_arquivo, 'r')
    primeira_linha = arquivo.readline()
    identificador = int(primeira_linha)
    
    arquivo.close()
    return identificador


def carrega_imagem(nome_imagem):
    """ Carrega do arquivo 'nome_imagem' uma imagem em formato PGM do tipo P2 e
    retorna � imagem em formato de matriz de pixels.

    A fun��o :func:'carrega_imagem' l� uma imagem em formato PGM do tipo P2
    presente em um arquivo na mesma pasta do programa ep3.py e retorna uma
    matriz de inteiros de tamanho N-por-M, onde N � a altura da imagem, e M �
    largura da imagem, ambos medidos em pixels e obtidos atrav�s do cabe�alho
    da imagem.

    :param nome_imagem: String com o nome de imagem na mesma pasta de ep3.py
    :type nome_imagem: <class 'str'>
    :return matriz: Matriz de inteiros representando os pixels da imagem
    :rtype: <class 'list'>

    :Example:

    >>> A = carrega_imagem('imagem.pgm')
    >>> print(A)
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

    .. seealso::
        Vide enunciado para uma explica��o mais detalhada acerca do formato PGM
    .. note::
        Voc� pode assumir que a imagem est� no formato correto e que o valor
        da intensidade de cada pixel � um inteiro entre 0 e 255 (inclusive).
    """
    matriz = [] #matriz que vai ser retornada com os valores inteiros
    arquivo_imagem = open(nome_imagem, 'r') #abrindo a 'nova_imagem'

    string_imagem = arquivo_imagem.readlines() #colocando todas a linhas do arquivo em uma lista, cada linha ocupa uma posi��o na lista
    lista_com_numero_de_colunas_e_linhas = string_imagem[1].split() #a posi��o n�mero 1 da string_imagem cont�m o n�mero de colunas e linhas, respectivamente
    
    numero_colunas = int(lista_com_numero_de_colunas_e_linhas[0])
    numero_linhas = int(lista_com_numero_de_colunas_e_linhas[1])

    for i in range(3, len(string_imagem)): #la�o que vai percorrer as linhas do arquivo que cont�m a matriz
        lista_com_conteudo_de_cada_linha = string_imagem[i].split() #cada valor estar� salvo em uma posi��o dessa lista, ainda s�o strings
        linha_matriz = []
        for j in range(numero_colunas): #percorrendo todos os valores da linha a fim de adicion�-los na matriz, j� como inteiros
            linha_matriz.append(int(lista_com_conteudo_de_cada_linha[j]))
        matriz.append(linha_matriz)

    arquivo_imagem.close()

    return matriz


def salva_imagem(nome_arquivo, matriz):
    """ Cria (se n�o existir) e escreve a imagem representada pela matriz no
    arquivo de nome nome_arquivo no formato PGM (tipo 2).

    A fun��o :func:'salva_imagem' recebe uma matriz de inteiros (0-255)
    representando uma imagem em tons de cinza e salva essa imagem no arquivo
    'nome_arquivo' no formato Portable GrayMap (PGM) do tipo P2 na mesma pasta.


    :param nome_arquivo: String contendo o nome de um arquivo (ex.'imagem.ppm')
    :param matriz: Matriz de inteiros representando uma imagem em tons de cinza
    :type nome_arquivo: <class 'str'>
    :type matriz: <class 'list'>

    :Example:

    >>> M = carrega_imagem('imagem.pgm')
    >>> print(M)
    [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    >>> M[0][0] = 255
    >>> print(M)
    [[255, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    >>> salva_imagem('nova_imagem.pgm', M)

    .. seealso::
        Consulte o enunciado para informa��es espec�ficas do formato PGM tipo 2
    """

    numero_linhas = len(matriz)
    numero_colunas = len(matriz[0])

    arquivo = open(nome_arquivo, 'w')
    #ADICIONANDO O CABE�ALHO DO ARQUIVO QUE SER� CRIADO
    arquivo.write('P2\n')
    arquivo.write(str(numero_colunas) + ' ' + str(numero_linhas) + '\n')
    arquivo.write('255\n')
    #ADICIONANDO A MATRIZ NO ARQUIVO, CONVERTENDO OS INTEIRAS PARA STRINGS
    for i in range(numero_linhas):
        string_dos_numeros = ''
        string_dos_numeros += str(matriz[i][0])
        for j in range(1, numero_colunas):
            string_dos_numeros += ' '
            string_dos_numeros += str(matriz[i][j])
        string_dos_numeros += '\n'
        arquivo.write(string_dos_numeros)
    
    arquivo.close()


def carrega_transforma��es(nome_arquivo):
    """Carrega transforma��es de um arquivo de texto.

    A fun��o :func:'carrega_transforma��es' recebe uma string com o nome de um
    arquivo presente na mesma pasta do programa ep3.py que cont�m as matrizes
    de transforma��o.
    Neste arquivo:

        - A primeira linha representa o n�mero total de transforma��es
        - Todas as outras linhas trazem ou transforma��es ou coment�rios

    Uma linha come�ando com # indica um coment�rio e deve ser ignorada.
    Todas as outras linhas representam matrizes 2-por-3 de modo que a matriz
    inteira est� representada em uma �nica linhado arquivo e cada elemento da
    matriz � separado por um (ou mais) espa�os.
    O exemplo abaixo mostra o conte�do de um poss�vel arquivo de transforma��es

    **Exemplo de arquivo de transforma��es**:
    2
    # Meu conjunto de transforma��es
    # transforma��o identidade
    1 0 0 0 1 0
    # espelhamento
    -1 0 0 0 -1 0


    :param nome_arquivo: String com nome de um arquivo texto contendo as
        transforma��es
    :type nome_arquivo: <class 'str'>
    :return lista: Uma lista de matrizes de transforma��o
    :rtype: <class 'list'>

    :Example:

    >>> transforma��es = carrega_transforma��es('duas_transforma��es.txt')
    >>> print(transforma��es)
    [[[1, 0, -20], [0, 1, -20]], [[1, 0, 0], [0, 1, 0]]]

    .. seealso::
        Veja o enunciado para maiores detalhes da estrutura desse arquivo.
    .. note::
        Voc� pode considerar que o arquivo de transforma��es s� cont�m os
        tr�s tipos de linhas mencionados (n�mero total de transforma��es,
        coment�rios e transforma��es), voc� n�o precisa tratar outros formatos.
    """
    lista_de_matrizes = [] #lista que vai devolver as matrizes de transforma��o

    arquivo = open(nome_arquivo, 'r') #abrinco o arquivo 'nome_arquivo' em modo leitura
    string_arquivo = arquivo.readlines() #criando uma vari�vel que vai conter cada linha do arquivo em uma posi��o da string
    numero_tranformacoes = 0

    for i in range(1, len(string_arquivo)): #percorrer a string do arquivo pra pegar as matrizes de transforma��o
    #n�o pegar a posi��o 0 pois nela h� o n�mero de transforma��es, e n�o precisa dele para pegar todas as transforma��es
        lista_com_conteudo_de_cada_linha = string_arquivo[i].split() #cada valor estar� salvo em uma posi��o dessa lista, ainda s�o strings
        if (lista_com_conteudo_de_cada_linha[0] != '#'): #se a linha n�o � um coment�rio, ent�o pegar os valores e converte-los
            matriz = [] #matriz onde vou colocar uma transforma��o linear por vez
            primeira_linha_string = lista_com_conteudo_de_cada_linha[:3] #primeira linha que vai na matriz, valores ainda s�o strings
            segunda_linha_string = lista_com_conteudo_de_cada_linha[3:] #segunda linha que vai na matriz, valores ainda s�o strings
            #convers�o dos valores do tipo string para o tipo inteiro
            primeira_linha_int = [] 
            segunda_linha_int = [] 
            for j in range(3):
                primeira_linha_int.append(int(primeira_linha_string[j]))
                segunda_linha_int.append(int(segunda_linha_string[j]))
            #adicionando as linhas, j� contendo inteiros, na matriz (essa ser� uma das transforma��es lineares)
            matriz.append(primeira_linha_int)
            matriz.append(segunda_linha_int)

            lista_de_matrizes.append(matriz)
    
    arquivo.close()
    return lista_de_matrizes


# ----------------------------------------------------------
# --                  FIM DA PARTE 2                      --
# ----------------------------------------------------------


# **********************************************************
# **                 IN�CIO DA PARTE 3                    **
# **********************************************************

def transforma(matriz, transforma��o):
    """ Devolve uma transforma��o geom�trica linear da matriz.

    A fun��o :func:'transforma' recebe uma matriz de pixels e uma transforma��o
    afim representada matricialmente e retorna a matriz transformada, **sem**
    modificar a matriz original.


    :param matriz: Matriz representando imagem em tons de cinza (0-255)
    :param transforma��o: Matriz 2-por-3 representando transforma��o linear
    :type matriz: <class 'list'>
    :type transforma��o: <class 'list'>
    :return matriz_transformada: Matriz resultado da transforma��o aplicada
        sobre todos os pontos
    :rtype: <class 'list'>

    :Example:

    >>> matriz1 = [[1, 2, 3], [4, 5, 6]]
    >>> print(matriz1)
    [[1, 2, 3], [4, 5, 6]]
    >>> transla��o_diagonal_por_1_pixel = [[1, 0, 1], [0, 1, 1], [0, 0, 1]]
    >>> matriz2 = transforma(matriz1, transla��o_diagonal_por_1_pixel)
    >>> print(matriz1)
    [[1, 2, 3], [4, 5, 6]]
    >>> print(matriz2)
    [[6, 4, 5], [3, 1, 2]]

    .. seealso::
        Vide enunciado para maiores exemplos da aplica��o dessa transforma��o

    .. note::
        Voc� pode assumir que s� ser�o utilizadas transforma��es invers�veis
        cujos coeficientes s�o inteiros.
    """
    matriz_transformada = []
    numero_linhas = len(matriz)
    numero_colunas = len(matriz[0])

    #preenchendo a matriz 'matriz_transformada' com zeros para usar no la�o abaixo
    for i in range(numero_linhas):
        linha = []
        for j in range(numero_colunas):
            linha.append(0)
        matriz_transformada.append(linha)

    # A = n�mero de linhas
    # L = n�mero de colunas
    #Ny',x' = My,x
    #x' = T0,0 . x + T0,1 . y + T0,2   mod L
    #y' = T1,0 . x + T1,1 . y + T1,2   mod A

    
    for y in range(numero_linhas):#La�o para fazer y variar de 0 a A - 1 = n�mero de linhas
        for x in range(numero_colunas):#La�o para fazer x variar de 0 a L - 1 = n�mero de colunas
            x_linha = (transforma��o[0][0] * x + transforma��o[0][1] * y + transforma��o[0][2]) % numero_colunas
            y_linha = (transforma��o[1][0] * x + transforma��o[1][1] * y + transforma��o[1][2]) % numero_linhas
            matriz_transformada[y_linha][x_linha] = matriz[y][x]

    return matriz_transformada


# ----------------------------------------------------------
# --                  FIM DA PARTE 3                      --
# ----------------------------------------------------------


# **********************************************************
# **                 IN�CIO DA PARTE 4                    **
# **********************************************************


def busca(matriz, transforma��es, identifica��o, max_transfs):
    """ Busca imagem com identifica��o dada usando no m�ximo um conjunto de
    max_transfs transforma��es.

    A fun��o :func:'busca' recebe uma matriz representando uma imagem
    monocrom�tica, uma lista de transforma��es poss�veis, um identificador
    correspondente � dispers�o criptogr�fica da imagem original e o valor do
    n�mero m�ximo de transforma��es em sequencia � serem realizadas sobre �
    matriz nessa busca e devolve:

        - A matriz da imagem original (caso encontrada) OU
        - None (caso contr�rio)

    :param matriz: Uma matriz de inteiros representando uma imagem
    :transforma��es: Uma lista de matrizes de transforma��o
    :identifica��o: Uma string com o identificador da imagem original
    :max_transfs: N�mero m�ximo de sequencias de transforma��es � testar
    :type matriz: <class 'list'>
    :type transforma��es: <class 'list'>
    :type identifica��o: <class 'str'>
    :type max_transfs: <class 'int'>
    :return resultado: Matriz com imagem restaurada ou None se ela n�o for
        encontrada.
    :rtype: <class 'list'> OU <class 'NoneType'>

    :Example:

    >>> original = [[1,2,3], [4,5,6], [7,8,9]]
    >>> identificador = calcula_id(imagem)
    >>> print(identificador)
    11403310
    >>> nova = transforma(imagem, [[1,0,1], [0,1,0]]) # Aplica desloc em eixo x
    >>> print(nova)
    [[3, 1, 2], [6, 4, 5], [9, 7, 8]]
    >>> nova2 = transforma(nova, [[1,0,1], [0,1,1]]) # Aplica Desloc x+1 e y+1
    >>> print(nova2)
    [[8, 9, 7], [2, 3, 1], [5, 6, 4]]
    >>> transfs = [[[1,0,-1], [0,1,0]], [[1,0,-1],[0,1,-1]], [[1,0,1],[0,1,1]]]
    >>> resultado = busca(nova2, transfs, identificador, 2)
    >>> print(resultado)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> resultado2 = busca(nova2, transfs, identificador, 1)
    >>> print(resultado2)
    None
    """
    if (calcula_id(matriz) == identifica��o): #verificando se encontrou uma matriz com mesmo identificador
        return matriz
    
    if (max_transfs == 0): #verificando se fez a busca o n�mero m�ximo de vezes
        return None
    
    for T in transforma��es: #pegando cada uma das transforma��es em 'transforma��es'
        N = transforma (matriz, T)
        R = busca (N, transforma��es, identifica��o, max_transfs - 1)
        
        if (R != None):
            return R
    
    return None


# ----------------------------------------------------------
# --                  FIM DA PARTE 4                      --
# ----------------------------------------------------------


# **********************************************************
# **                 IN�CIO DA PARTE 5                    **
# **********************************************************

def main():
    """ Aqui voc� deve implementar � interface de comunica��o com o usu�rio

    Sua interface deve (necessariamente nessa ordem):
        1. Escrever uma mensagem de identifica��o do autor e descri��o do programa.
        2. Solicitar ao usu�rio que digite o nome do arquivo da imagem transformada.
        3. Solicitar ao usu�rio que digite o nome do arquivo contendo o identificador.
        4. Solicitar ao usu�rio que digite o nome do o arquivo com as transforma��es.
        5. Solicitar ao usu�rio que digite o nome do arquivo no qual ser� salva a imagem restaurada (se encontrada).
        6. Informar se a busca foi exitosa ou n�o.

    :Example:

    >>> $ python3 ep3.py
    *****************************
    *** Programa desfaz v�rus ***
    *****************************

    Autor: Denis Mau�
    NUSP: 3730790

    Entre com o nome do arquivo contendo imagem transformada: img00.pgm
    Entre com o nome do arquivo contendo o identificador da imagem original: img00.adler
    Entre com o nome do arquivo contendo as transforma��es dispon�veis: transforma��es00.txt
    Entre com o nome do arquivo onde a imagem original deve ser salva: resultado00.pgm
    Entre com o n�mero m�ximo de transforma��es: 2

    Tentando restaurar imagem 'img00.pgm'... Falhou!

    N�o foi poss�vel encontrar uma imagem com o identificador 870647247 utilizando uma sequ�ncia de no m�ximo 2 transforma��es em 'transforma��es00.txt'!

    Voc� pode tentar aumentar o n�mero m�ximo de transforma��es ou mudar o arquivo de transforma��es.

    >>> $ python3 ep3.py
    *****************************
    *** Programa desfaz v�rus ***
    *****************************

    Autor: Denis Mau�
    NUSP: 3730790

    Entre com o nome do arquivo contendo imagem transformada: img01.pgm
    Entre com o nome do arquivo contendo o identificador da imagem original: img01.adler
    Entre com o nome do arquivo contendo as transforma��es dispon�veis: transforma��es.txt
    Entre com o nome do arquivo onde a imagem original deve ser salva: resultado01.pgm
    Entre com o n�mero m�ximo de transforma��es: 6

    Tentando restaurar imagem 'img01.pgm'... Pronto!

    Imagem com o identificador 870647247 salva em 'resultado01.pgm'!

    .. seealso::
        Consulte o enunciado para mais exemplos.
    """
    print("*****************************")
    print("*** Programa desfas v�rus ***")
    print("*****************************")
    print()
    print("Autor: William Sim�es Barbosa")
    print("NUSP: 9837646")
    print()

    imagem_transformada = input("Entre com o nome do arquivo contendo a imagem transformada: ")
    arquivo_identificador_original = input("Entre com o nome do arquivo contendo o identificador da imagem original: ")
    arquivo_transformacoes = input("Entre com o nome do arquivo contendo as transforma��es dispon�veis: ")
    salvar_imagem_original = input("Entre com o nome do arquivo onde a imagem original deve ser salva: ")
    maximo_transformacoes = int(input("Entre com o n�mero m�ximo de transforma��es: "))

    print("\nTentando restaurar a imagem '" + imagem_transformada + "'...", end = " ")

    matriz_transformada = carrega_imagem(imagem_transformada)
    identificador_original = carrega_identificador(arquivo_identificador_original)
    tranformacoes = carrega_transforma��es(arquivo_transformacoes)

    matriz_imagem_restaurada = busca(matriz_transformada, tranformacoes, identificador_original, maximo_transformacoes)

    if (matriz_imagem_restaurada == None):
        print("Falhou!")
        print()
        print("N�o foi poss�vel encontrar uma imagem com o identificador ", identificador_original, " utilizando uma sequ�ncia de no m�ximo ", 
            maximo_transformacoes, " transforma��es em " + arquivo_transformacoes + "!")
        print()
        print("Voc� pode tentar aumentar o n�mero m�ximo de transforma��es ou mudar o arquivo de transforma��es.")
        salva_imagem(salvar_imagem_original, matriz_transformada)

    else:
        print("Pronto!")
        print()
        print("Imagem com o identificador " + str(identificador_original) + " salva em '" + salvar_imagem_original + "'!")
        salva_imagem(salvar_imagem_original, matriz_imagem_restaurada)


# ----------------------------------------------------------
# --                  FIM DA PARTE 4                      --
# ----------------------------------------------------------


# ******************************************************
# **  IMPORTANTE: N�O MODIFIQUE AS PR�XIMAS LINHAS!   **
# ******************************************************
if __name__ == "__main__":
    main()

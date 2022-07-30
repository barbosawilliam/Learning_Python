# -*- coding: latin-1 -*-
"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP,
  DECLARO QUE SOU A ÚNICA PESSOA AUTORA E RESPONSÁVEL POR ESSE PROGRAMA.
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E, PORTANTO, NÃO CONSTITUEM ATO DE DESONESTIDADE ACADÊMICA,
  FALTA DE ÉTICA OU PLÁGIO.
  DECLARO TAMBÉM QUE SOU A PESSOA RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE NÃO DISTRIBUÍ OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome : WILLIAM SIMÕES BARBOSA
  NUSP : 9837646
  Turma: 07
  Prof.: ALAN DURHAM

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma referência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.

  Exemplo:
  - O algoritmo Quicksort foi baseado em
  https://pt.wikipedia.org/wiki/Quicksort
  http://www.ime.usp.br/~pf/algoritmos/aulas/quick.html
"""

# **********************************************************
# **                 INÍCIO DA PARTE 1                    **
# **********************************************************


def calcula_id(matriz):
    """ Retorna o valor de identificação de uma matriz computada pelo
    algoritmo adler32

    A função :func:'calcula_id' computa um identificador para uma matriz
    usando a seguinte versão adaptada do algoritmo de espalhamento Adler32:

        - A = 1 + matriz[0][0] + matriz[0][1] +...+ matriz[m-1][n-1] MOD 65521,
            onde m é o número de linhas e n é o número de colunas da matriz
        - B = (1 + matriz[0][0]) + (1 + matriz[0][0]+matriz[0][1]) + ... +
          (1 + matriz[0][0] + matriz[0][1] + ... + matriz[m-1][n-1]) MOD 65521
        - retorna B * (2**16) + A


    :param matriz: Uma matriz de inteiros
    :type matriz: <class 'list'>
    :return identificador: O identificador inteiro da matriz computado segundo
        a nossa versão adaptada do Adler32
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

    #Determinação de A e B:
    for i in range(len(matriz)): #laço para percorrer todas as linhas da matriz
        for j in range(len(matriz[0])): #laço para percorrer todas as colunas da matriz
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
# **                 INÍCIO DA PARTE 2                    **
# **********************************************************


def carrega_identificador(nome_arquivo):
    """ Carrega o identificador de uma imagem presente em um arquivo.

    A função :func:'carrega_identificador' abre um arquivo de nome
    'nome_arquivo' presente na mesma pasta que o programa ep3.py, lê sua
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
        Embora pelas regras da disciplina você possa assumir que o arquivo
        'nome_arquivo' está presente na mesma pasta do programa ep3.py,
        boas práticas de programação sugerem que para escrita e leitura de
        arquivos, você sempre deve verificar à existência/permissões.
        Com relação ao identificador, você pode assumir que o arquivo contém
        um identificador válido na primeira linha.
    """
    arquivo = open(nome_arquivo, 'r')
    primeira_linha = arquivo.readline()
    identificador = int(primeira_linha)
    
    arquivo.close()
    return identificador


def carrega_imagem(nome_imagem):
    """ Carrega do arquivo 'nome_imagem' uma imagem em formato PGM do tipo P2 e
    retorna à imagem em formato de matriz de pixels.

    A função :func:'carrega_imagem' lê uma imagem em formato PGM do tipo P2
    presente em um arquivo na mesma pasta do programa ep3.py e retorna uma
    matriz de inteiros de tamanho N-por-M, onde N é a altura da imagem, e M é
    largura da imagem, ambos medidos em pixels e obtidos através do cabeçalho
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
        Vide enunciado para uma explicação mais detalhada acerca do formato PGM
    .. note::
        Você pode assumir que a imagem está no formato correto e que o valor
        da intensidade de cada pixel é um inteiro entre 0 e 255 (inclusive).
    """
    matriz = [] #matriz que vai ser retornada com os valores inteiros
    arquivo_imagem = open(nome_imagem, 'r') #abrindo a 'nova_imagem'

    string_imagem = arquivo_imagem.readlines() #colocando todas a linhas do arquivo em uma lista, cada linha ocupa uma posição na lista
    lista_com_numero_de_colunas_e_linhas = string_imagem[1].split() #a posição número 1 da string_imagem contém o número de colunas e linhas, respectivamente
    
    numero_colunas = int(lista_com_numero_de_colunas_e_linhas[0])
    numero_linhas = int(lista_com_numero_de_colunas_e_linhas[1])

    for i in range(3, len(string_imagem)): #laço que vai percorrer as linhas do arquivo que contém a matriz
        lista_com_conteudo_de_cada_linha = string_imagem[i].split() #cada valor estará salvo em uma posição dessa lista, ainda são strings
        linha_matriz = []
        for j in range(numero_colunas): #percorrendo todos os valores da linha a fim de adicioná-los na matriz, já como inteiros
            linha_matriz.append(int(lista_com_conteudo_de_cada_linha[j]))
        matriz.append(linha_matriz)

    arquivo_imagem.close()

    return matriz


def salva_imagem(nome_arquivo, matriz):
    """ Cria (se não existir) e escreve a imagem representada pela matriz no
    arquivo de nome nome_arquivo no formato PGM (tipo 2).

    A função :func:'salva_imagem' recebe uma matriz de inteiros (0-255)
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
        Consulte o enunciado para informações específicas do formato PGM tipo 2
    """

    numero_linhas = len(matriz)
    numero_colunas = len(matriz[0])

    arquivo = open(nome_arquivo, 'w')
    #ADICIONANDO O CABEÇALHO DO ARQUIVO QUE SERÁ CRIADO
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


def carrega_transformações(nome_arquivo):
    """Carrega transformações de um arquivo de texto.

    A função :func:'carrega_transformações' recebe uma string com o nome de um
    arquivo presente na mesma pasta do programa ep3.py que contém as matrizes
    de transformação.
    Neste arquivo:

        - A primeira linha representa o número total de transformações
        - Todas as outras linhas trazem ou transformações ou comentários

    Uma linha começando com # indica um comentário e deve ser ignorada.
    Todas as outras linhas representam matrizes 2-por-3 de modo que a matriz
    inteira está representada em uma única linhado arquivo e cada elemento da
    matriz é separado por um (ou mais) espaços.
    O exemplo abaixo mostra o conteúdo de um possível arquivo de transformações

    **Exemplo de arquivo de transformações**:
    2
    # Meu conjunto de transformações
    # transformação identidade
    1 0 0 0 1 0
    # espelhamento
    -1 0 0 0 -1 0


    :param nome_arquivo: String com nome de um arquivo texto contendo as
        transformações
    :type nome_arquivo: <class 'str'>
    :return lista: Uma lista de matrizes de transformação
    :rtype: <class 'list'>

    :Example:

    >>> transformações = carrega_transformações('duas_transformações.txt')
    >>> print(transformações)
    [[[1, 0, -20], [0, 1, -20]], [[1, 0, 0], [0, 1, 0]]]

    .. seealso::
        Veja o enunciado para maiores detalhes da estrutura desse arquivo.
    .. note::
        Você pode considerar que o arquivo de transformações só contém os
        três tipos de linhas mencionados (número total de transformações,
        comentários e transformações), você não precisa tratar outros formatos.
    """
    lista_de_matrizes = [] #lista que vai devolver as matrizes de transformação

    arquivo = open(nome_arquivo, 'r') #abrinco o arquivo 'nome_arquivo' em modo leitura
    string_arquivo = arquivo.readlines() #criando uma variável que vai conter cada linha do arquivo em uma posição da string
    numero_tranformacoes = 0

    for i in range(1, len(string_arquivo)): #percorrer a string do arquivo pra pegar as matrizes de transformação
    #não pegar a posição 0 pois nela há o número de transformações, e não precisa dele para pegar todas as transformações
        lista_com_conteudo_de_cada_linha = string_arquivo[i].split() #cada valor estará salvo em uma posição dessa lista, ainda são strings
        if (lista_com_conteudo_de_cada_linha[0] != '#'): #se a linha não é um comentário, então pegar os valores e converte-los
            matriz = [] #matriz onde vou colocar uma transformação linear por vez
            primeira_linha_string = lista_com_conteudo_de_cada_linha[:3] #primeira linha que vai na matriz, valores ainda são strings
            segunda_linha_string = lista_com_conteudo_de_cada_linha[3:] #segunda linha que vai na matriz, valores ainda são strings
            #conversão dos valores do tipo string para o tipo inteiro
            primeira_linha_int = [] 
            segunda_linha_int = [] 
            for j in range(3):
                primeira_linha_int.append(int(primeira_linha_string[j]))
                segunda_linha_int.append(int(segunda_linha_string[j]))
            #adicionando as linhas, já contendo inteiros, na matriz (essa será uma das transformações lineares)
            matriz.append(primeira_linha_int)
            matriz.append(segunda_linha_int)

            lista_de_matrizes.append(matriz)
    
    arquivo.close()
    return lista_de_matrizes


# ----------------------------------------------------------
# --                  FIM DA PARTE 2                      --
# ----------------------------------------------------------


# **********************************************************
# **                 INÍCIO DA PARTE 3                    **
# **********************************************************

def transforma(matriz, transformação):
    """ Devolve uma transformação geométrica linear da matriz.

    A função :func:'transforma' recebe uma matriz de pixels e uma transformação
    afim representada matricialmente e retorna a matriz transformada, **sem**
    modificar a matriz original.


    :param matriz: Matriz representando imagem em tons de cinza (0-255)
    :param transformação: Matriz 2-por-3 representando transformação linear
    :type matriz: <class 'list'>
    :type transformação: <class 'list'>
    :return matriz_transformada: Matriz resultado da transformação aplicada
        sobre todos os pontos
    :rtype: <class 'list'>

    :Example:

    >>> matriz1 = [[1, 2, 3], [4, 5, 6]]
    >>> print(matriz1)
    [[1, 2, 3], [4, 5, 6]]
    >>> translação_diagonal_por_1_pixel = [[1, 0, 1], [0, 1, 1], [0, 0, 1]]
    >>> matriz2 = transforma(matriz1, translação_diagonal_por_1_pixel)
    >>> print(matriz1)
    [[1, 2, 3], [4, 5, 6]]
    >>> print(matriz2)
    [[6, 4, 5], [3, 1, 2]]

    .. seealso::
        Vide enunciado para maiores exemplos da aplicação dessa transformação

    .. note::
        Você pode assumir que só serão utilizadas transformações inversíveis
        cujos coeficientes são inteiros.
    """
    matriz_transformada = []
    numero_linhas = len(matriz)
    numero_colunas = len(matriz[0])

    #preenchendo a matriz 'matriz_transformada' com zeros para usar no laço abaixo
    for i in range(numero_linhas):
        linha = []
        for j in range(numero_colunas):
            linha.append(0)
        matriz_transformada.append(linha)

    # A = número de linhas
    # L = número de colunas
    #Ny',x' = My,x
    #x' = T0,0 . x + T0,1 . y + T0,2   mod L
    #y' = T1,0 . x + T1,1 . y + T1,2   mod A

    
    for y in range(numero_linhas):#Laço para fazer y variar de 0 a A - 1 = número de linhas
        for x in range(numero_colunas):#Laço para fazer x variar de 0 a L - 1 = número de colunas
            x_linha = (transformação[0][0] * x + transformação[0][1] * y + transformação[0][2]) % numero_colunas
            y_linha = (transformação[1][0] * x + transformação[1][1] * y + transformação[1][2]) % numero_linhas
            matriz_transformada[y_linha][x_linha] = matriz[y][x]

    return matriz_transformada


# ----------------------------------------------------------
# --                  FIM DA PARTE 3                      --
# ----------------------------------------------------------


# **********************************************************
# **                 INÍCIO DA PARTE 4                    **
# **********************************************************


def busca(matriz, transformações, identificação, max_transfs):
    """ Busca imagem com identificação dada usando no máximo um conjunto de
    max_transfs transformações.

    A função :func:'busca' recebe uma matriz representando uma imagem
    monocromática, uma lista de transformações possíveis, um identificador
    correspondente à dispersão criptográfica da imagem original e o valor do
    número máximo de transformações em sequencia à serem realizadas sobre à
    matriz nessa busca e devolve:

        - A matriz da imagem original (caso encontrada) OU
        - None (caso contrário)

    :param matriz: Uma matriz de inteiros representando uma imagem
    :transformações: Uma lista de matrizes de transformação
    :identificação: Uma string com o identificador da imagem original
    :max_transfs: Número máximo de sequencias de transformações à testar
    :type matriz: <class 'list'>
    :type transformações: <class 'list'>
    :type identificação: <class 'str'>
    :type max_transfs: <class 'int'>
    :return resultado: Matriz com imagem restaurada ou None se ela não for
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
    if (calcula_id(matriz) == identificação): #verificando se encontrou uma matriz com mesmo identificador
        return matriz
    
    if (max_transfs == 0): #verificando se fez a busca o número máximo de vezes
        return None
    
    for T in transformações: #pegando cada uma das transformações em 'transformações'
        N = transforma (matriz, T)
        R = busca (N, transformações, identificação, max_transfs - 1)
        
        if (R != None):
            return R
    
    return None


# ----------------------------------------------------------
# --                  FIM DA PARTE 4                      --
# ----------------------------------------------------------


# **********************************************************
# **                 INÍCIO DA PARTE 5                    **
# **********************************************************

def main():
    """ Aqui você deve implementar à interface de comunicação com o usuário

    Sua interface deve (necessariamente nessa ordem):
        1. Escrever uma mensagem de identificação do autor e descrição do programa.
        2. Solicitar ao usuário que digite o nome do arquivo da imagem transformada.
        3. Solicitar ao usuário que digite o nome do arquivo contendo o identificador.
        4. Solicitar ao usuário que digite o nome do o arquivo com as transformações.
        5. Solicitar ao usuário que digite o nome do arquivo no qual será salva a imagem restaurada (se encontrada).
        6. Informar se a busca foi exitosa ou não.

    :Example:

    >>> $ python3 ep3.py
    *****************************
    *** Programa desfaz vírus ***
    *****************************

    Autor: Denis Mauá
    NUSP: 3730790

    Entre com o nome do arquivo contendo imagem transformada: img00.pgm
    Entre com o nome do arquivo contendo o identificador da imagem original: img00.adler
    Entre com o nome do arquivo contendo as transformações disponíveis: transformações00.txt
    Entre com o nome do arquivo onde a imagem original deve ser salva: resultado00.pgm
    Entre com o número máximo de transformações: 2

    Tentando restaurar imagem 'img00.pgm'... Falhou!

    Não foi possível encontrar uma imagem com o identificador 870647247 utilizando uma sequência de no máximo 2 transformações em 'transformações00.txt'!

    Você pode tentar aumentar o número máximo de transformações ou mudar o arquivo de transformações.

    >>> $ python3 ep3.py
    *****************************
    *** Programa desfaz vírus ***
    *****************************

    Autor: Denis Mauá
    NUSP: 3730790

    Entre com o nome do arquivo contendo imagem transformada: img01.pgm
    Entre com o nome do arquivo contendo o identificador da imagem original: img01.adler
    Entre com o nome do arquivo contendo as transformações disponíveis: transformações.txt
    Entre com o nome do arquivo onde a imagem original deve ser salva: resultado01.pgm
    Entre com o número máximo de transformações: 6

    Tentando restaurar imagem 'img01.pgm'... Pronto!

    Imagem com o identificador 870647247 salva em 'resultado01.pgm'!

    .. seealso::
        Consulte o enunciado para mais exemplos.
    """
    print("*****************************")
    print("*** Programa desfas vírus ***")
    print("*****************************")
    print()
    print("Autor: William Simões Barbosa")
    print("NUSP: 9837646")
    print()

    imagem_transformada = input("Entre com o nome do arquivo contendo a imagem transformada: ")
    arquivo_identificador_original = input("Entre com o nome do arquivo contendo o identificador da imagem original: ")
    arquivo_transformacoes = input("Entre com o nome do arquivo contendo as transformações disponíveis: ")
    salvar_imagem_original = input("Entre com o nome do arquivo onde a imagem original deve ser salva: ")
    maximo_transformacoes = int(input("Entre com o número máximo de transformações: "))

    print("\nTentando restaurar a imagem '" + imagem_transformada + "'...", end = " ")

    matriz_transformada = carrega_imagem(imagem_transformada)
    identificador_original = carrega_identificador(arquivo_identificador_original)
    tranformacoes = carrega_transformações(arquivo_transformacoes)

    matriz_imagem_restaurada = busca(matriz_transformada, tranformacoes, identificador_original, maximo_transformacoes)

    if (matriz_imagem_restaurada == None):
        print("Falhou!")
        print()
        print("Não foi possível encontrar uma imagem com o identificador ", identificador_original, " utilizando uma sequência de no máximo ", 
            maximo_transformacoes, " transformações em " + arquivo_transformacoes + "!")
        print()
        print("Você pode tentar aumentar o número máximo de transformações ou mudar o arquivo de transformações.")
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
# **  IMPORTANTE: NÃO MODIFIQUE AS PRÓXIMAS LINHAS!   **
# ******************************************************
if __name__ == "__main__":
    main()

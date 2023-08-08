from random import choice, shuffle


def criar_amostra(nome='Nova Amostra'):
    """
    Esta função cria e formata novas amostras de jogos.
    Os numeros de cada aposta ocupam dois digitos.
    Espaços são eliminados automaticamente.
    O ultimo valor digitado é considerado o jogo mais recente.
    :param nome: é o nome dado ao arquivo que será criado.
    :return: Um arquivo .txt, com os jogos inseridos.
    """
    gravar = []
    n = 1
    while True:
        novo = ''.join(input(f'(x_cancela) Novo Valor n.{n}:').split())
        n = n + 1
        if novo in 'xX':
            break
        jogo = []
        for a in range(0, len(novo)):
            if (a % 2) == 0:
                valor = novo[a:a+2]
                jogo.append(valor)
        jg = '-'.join(jogo[:])
        j = jg + '\n'
        gravar.append(j)
    with open(nome + '.txt', 'wt+') as arquivo:
        arquivo.writelines(gravar)


def universo(uni):
    """
    Esta função cria uma lista de strings para simular um universo de numeros.
    Seu limite é de 100 numeros, sendo o numero 100 representado por "00".
    :param uni: valor inteiro até 100.
    :return: list[str]
    """
    if uni > 100:
        verso = 100
    else:
        verso = uni
    u = list(range(0, verso))
    for n in range(1, verso+1):
        if n == 100:
            u[99] = '00'
        else:
            u[n - 1] = str(n)
        if len(u[n-1]) == 1:
            u[n-1] = '0'+u[n-1]
    u.sort()
    return u


def menu(itens=('Cabeçalho', 'Opções', 'Sua escolha:')):
    """
    Esta função cria um menu com opções apartir de uma lista.
    A largura do menu se ajusta automaticamente.
    O primeiro item será o cabeçalho, e o ultimo será o print do input.
    :param itens: Lista com N opções, exceto a primeira e a ultima posição.
    :return: Um input qualquer, apesar das opções estarem organizadas numericamente.
    """
    largura = 0
    for x1 in itens:
        maior = len(x1)
        if maior > largura:
            largura = maior
    lg = 16 + largura
    lg1 = ((lg - len(itens[0])) // 2) - 1
    lg2 = (lg - len(itens[0])) - lg1
    print('=' * lg)
    print(' ' * lg1, f'{itens[0]}', ' ' * lg2)
    print('=' * lg, '\n')
    for x2 in range(1, len(itens) - 1):
        print(f'[{x2}] - {itens[x2]}')
    print('[0] - Sair\n')
    escolha = input(f'{itens[len(itens) - 1]}')
    return escolha


def acumulativa(s, uni, amo):
    """
    Esta função cria um levantamento de credito/debito (CD) para cada valor de um universo,
    ao longo de uma amostra de jogos realizados.
    Numeros que caem mais que o esperado recebem um valor de CD negativo.
    Numeros que caem menos que o esperado recebem um valor de CD positivo.
    :param s: Quantidade de numeros sorteados por jogo.
    :param uni: Lista com o universo do jogo.
    :param amo: Lista com a amostra a ser analisada.
    :return: Uma lista com os valores de CD para cada numero do universo.
    """
    u = len(uni)
    a = len(amo)
    e = a * s   # Numero de elementos na amostra.
    rm = e / u  # Repetição média esperada.
    filtro = list(range(0, u))
    for indice, valor in enumerate(uni):
        r = 0   # Repetição observada.
        for jogo in amo:
            if valor in jogo:
                r = r + 1
        cd = (rm - r) / e
        filtro[indice] = cd    # Lista dos CD para cada numero no universo, respectivamente.
    return filtro


def sequencial(s, uni, amo):
    """
    Esta função cria um levantamento de sequências,
    de valores que foram sorteados ou ausentados por vezes consecutivas.
    Entendendo que o ultimo valor na lista de amostra foi o ultimo jogo realizado.
    No final, o levantamento irá mostrar as chances de sucesso de cada valor, para o próximo jogo.
    :param s: Quantidade de numeros sorteados por jogo.
    :param uni: Lista com o universo do jogo.
    :param amo: Lista com a amostra a ser analisada.
    :return: Uma lista com as chances que cada valor tem de cair no próximo jogo.
    """
    u = len(uni)
    a = len(amo)
    su = 0.0    # su são as chances de um elemento qualquer ser sorteado.
    for x in range(0, s):
        su = su + (1 / (u - x))
    fr = 1 - su     # fr são as chances de um elemento qualquer ser ausentado.
    amostra = amo[a:0:-1]
    amostra.append(amo[0])  # O fatiamento regressivo também ignora a ultima posição.
    filtro = list(range(0, u))
    for indice, valor in enumerate(uni):
        r = 0
        for jogo in amostra:
            if r > 0:
                if valor in jogo:
                    r = r + 1
                else:
                    break
            if r < 0:
                if valor in jogo:
                    break
                else:
                    r = r - 1
            if r == 0:
                if valor in jogo:
                    r = r + 1
                else:
                    r = r - 1
        if r > 0:
            cn = su ** (r + 1)
            filtro[indice] = cn
        else:
            cn = 1 - (fr ** ((r * (-1)) + 1))
            filtro[indice] = cn
    to = sum(filtro)
    for ind, el in enumerate(filtro):   # Arredondamento dos valores das chances para cada elemento.
        nv = (el/to)
        filtro[ind] = nv
    return filtro


def jogar(s, uni, fixar=()):
    """
    Esta função retorna um jogo aleatório, de um numero s de escolhas em um universo.
    Com a possibilidade de fixar valores por meio de uma lista de valores.
    :param s: Quantidade de numeros sorteados por jogo.
    :param uni: Universo do jogo.
    :param fixar: Valores opcionais para fixação (str).
    :return: Um jogo aleatório em formato de str.
    """
    jogo = []
    if len(fixar) > 0:
        for x1 in fixar:
            jogo.append(x1)             # Fixação de valores.
    x = len(jogo)
    for x2 in range(0, s - x):
        novo_uni = []
        for x3 in uni:
            if x3 not in jogo:
                novo_uni.append(x3)     # Reconstituição parcial do universo.
        shuffle(novo_uni)
        valor = choice(novo_uni)        # Escolha do elemento ao acaso.
        jogo.append(valor)
    jogo.sort()
    jg = '-'.join(jogo[:])              # Formatação do resultado final.
    return jg


def resultados(uni, apostas, jogo):
    """
    Esta função retorna uma lista de acertos, correspondente a lista de apostas.
    :param uni: Universo.
    :param apostas: Jogos apostados.
    :param jogo: Jogo realizado.
    :return: Lista com os acertos de cada aposta realizada.
    """
    ap = len(apostas)
    resultado = list(range(0, ap))
    for indice, jogada in enumerate(apostas):
        pontos = 0
        for valor in uni:
            if (valor in jogo) and (valor in jogada):
                pontos = pontos + 1
        resultado[indice] = pontos
    return resultado

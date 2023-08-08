import loteria

# Este script utiliza a lotofácil como exemplo de jogo (15 sorteados, universo de 25 numeros)
opcoes = ['Menu', 'Criar Universo', 'Criar Amostra', 'Analise acumulativa',
          'Analise Sequêncial', 'Jogar', 'Resultados', 'Escolha:']

# Exemplo de uso da função "menu"
escolha = loteria.menu(opcoes[:])

# Exemplo de uso da função "universo"
if escolha == '1':
    universo = loteria.universo(25)
    print(universo)

# Exemplo de uso da função "criar_amostra"
if escolha == '2':
    loteria.criar_amostra('Testando')

# Exemplo de uso da função "acumulativa"
if escolha == '3':
    sorteados = 15
    universo = loteria.universo(25)
    with open('exemplo de amostra.txt', 'rt') as arquivo:
        amostra = arquivo.readlines()
    frequencia = loteria.acumulativa(sorteados, universo, amostra[:])
    print(frequencia)

# Exemplo de uso da função "sequencial"
if escolha == '4':
    sorteados = 15
    universo = loteria.universo(25)
    with open('exemplo de amostra.txt', 'rt') as arquivo:
        amostra = arquivo.readlines()
    chances = loteria.sequencial(sorteados, universo, amostra[:])
    print(chances)

# Exemplo de uso da função "jogar"
if escolha == '5':
    sorteados = 15
    universo = loteria.universo(25)
    numeros_fixos = ['02', '11', '24']
    aposta = loteria.jogar(sorteados, universo, numeros_fixos[:])
    print(aposta)

# Exemplo de uso da função "resultados"
if escolha == '6':
    sorteados = 15
    universo = loteria.universo(25)
    jogo = loteria.jogar(sorteados, universo)   # Aqui a função jogar está simulando um novo jogo.
    with open('exemplo de amostra.txt', 'rt') as arquivo:    # Neste caso, o arquivo lotofacil.txt
        aposta = arquivo.readlines()    # está simulando uma lista de apostas, e não de amostras.
    acertos = loteria.resultados(universo, aposta[:], jogo)
    print(acertos)

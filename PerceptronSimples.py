entradas = [[-1, 0.1, 0.4, 0.7],
            [-1, 0.3, 0.7, 0.2],
            [-1, 0.6, 0.9, 0.8],
            [-1, 0.5, 0.7, 0.1]]

respostas = [1, -1, -1, 1]
epocas = 0
taxa = 0.085
erro = False
pesos = [0.2, 0.3, 0.4, 0.5]


def novoPeso(y, u, x):   # y resposta esperada, u resposta calculada, x entrada
    for i in range(0, 4):
        pesos[i] = pesos[i] + (taxa * (y - u) * x[i])


def multiplica(ent):
    u = []
    for x in range(0, 4):
        u.append(ent[x] * pesos[x])
    return u


def step(u):   # degrau bipolar
    # return round(u, 0) # função degrau
    if u > 0:
        return 1
    elif u < 0:
        return -1
    return 0


def soma(lista):
    s = 0           # soma total
    valores = multiplica(lista)
    for x in valores:
        s += x
    return step(s)


# treinamento
while True:  # emulate do while
    erro = False     # so para com a resposta 100% certa, só é possível em problemas lineares
    for f in range(0, 4):   # numero de casos de testes e nao de entradas
        saida = (soma(entradas[f]))  # uma variavel única pois da trabalho resetar a lista a cada treinamento
        if saida != respostas[f]:
            erro = True
            novoPeso(respostas[f], saida, entradas[f])
            print(f"Novos pesos: {pesos}")
    epocas += 1      # numero de treinamentos
    if not erro:    # emulate do while
        break


# depois da rede estar treinada - pronta
saidas = []
for entrada in entradas:
    saidas.append(soma(entrada))   # calcula as entradas uma última vez com os pesos corretos


print(f"Saida: {saidas}")
print(f"Pesos Iniciais: {[0.2, 0.3, 0.4, 0.5]}")
print(f"Pesos Finais: {pesos}")
print(f"Taxa de Aprendizado: {taxa} ")
print(f"Epocas: {epocas}")

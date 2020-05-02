entradas = [[-1, 0.1, 0.4, 0.7],
            [-1, 0.3, 0.7, 0.2],
            [-1, 0.6, 0.9, 0.8],
            [-1, 0.5, 0.7, 0.1]]

respostas = [1, -1, -1, 1]
# saidas = []
epocas = 0
taxa = 0.085
erro = False
pesos = [0.2, 0.3, 0.4, 0.5]


def novoPeso(y, u, x):   # y resposta esperada, u resposta calculada, x entrada
    for i in range(0, 4):
        pesos[i] = pesos[i] + (taxa * (y - u) * x[i])


def multiplica(entrada):
    u = []
    for x in range(0, 4):
        u.append(entrada[x] * pesos[x])
    return u


def step(u):
    # return round(u, 0)
    if u > 0:
        return 1
    elif u < 0:
        return -1
    return 0


def soma(lista):
    soma = 0
    valores = multiplica(lista)
    for x in valores:
        soma += x
    return step(soma)


while True:  # emulate do while
    erro = False
    for f in range(0, 4):
        saida = (soma(entradas[f]))
        if saida != respostas[f]:
            erro = True
            novoPeso(respostas[f], saida, entradas[f])
            print(f"Novos pesos: {pesos}")
    epocas += 1
    if not erro:    # emulate do while
        break


saidas = []
for entrada in entradas:
    saidas.append(soma(entrada))

print(f"Saida: {saidas}")
print(f"Pesos Iniciais: {[0.2, 0.3, 0.4, 0.5]}")
print(f"Pesos Finais: {pesos}")
print(f"Taxa de Aprendizado: {taxa} ")
print(f"Epocas: {epocas}")

import random
entradas = []
respostas = []
taxa = 0.001
epocas = 0
erroMedio = 1
erroMedioAntigo = 0
precisao = 0.000001
numeroEntradas = len(entradas[0])
numeroAmostras = len(entradas)
pesos = []
for a in range(0, numeroEntradas):
    pesos.append(round(random.random(), 3))
pesosIniciais = pesos.copy()


# ---------  Cálculo ------------


def multiplica(ent):
    u = []
    for x in range(0, numeroEntradas):
        u.append(ent[x] * pesos[x])   # com dúvida sobre - pesos[0] e ou  - pesos[x] ou sem subtração nenhuma
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


# ---------  Treinamento ------------
def erro():
    errom = 0
    for x in range(0, numeroAmostras):
        u = soma(entradas[x])
        errom = errom + ((respostas[x] - u) ** 2)

    return errom/numeroAmostras


def novoPeso(y, u, x):   # y resposta esperada, u resposta calculada, x entrada
    for i in range(0, numeroEntradas):
        pesos[i] = pesos[i] + (taxa * (y - u) * x[i])


while (erroMedio - erroMedioAntigo) > precisao:
    erroMedio = 0
    erroMedioAntigo = erroMedio
    for a in range(0, numeroAmostras):
        saida = soma(entradas[a])
        novoPeso(respostas[a], saida, entradas[a])
    epocas += 1
    erroMedio = erro()
    print(f"Erro Médio: {erroMedio - erroMedioAntigo}")


# ---------  Rede Treinada ------------

entradasFinais = []
saidas = []
for entrada in entradasFinais:
    saidas.append(soma(entrada))

print(f"Saida: {saidas}")
print(f"Pesos Iniciais: {pesosIniciais}")
print(f"Pesos Finais: {pesos}")
print(f"Taxa de Aprendizado: {taxa} ")
print(f"Erro Mínimo: {precisao} ")
print(f"Epocas: {epocas}")
print(f"Erro Médio: {erroMedio - erroMedioAntigo}")

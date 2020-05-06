# Modelo Rede Perceptron, com -1 na primeira entrada, bias

import random
entradas = []
respostas = []
taxa = 0.01
epocas = 0
erro = True
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


def novoPeso(y, u, x):   # y resposta esperada, u resposta calculada, x entrada
    for i in range(0, numeroEntradas):
        pesos[i] = pesos[i] + (taxa * (y - u) * x[i])


while erro:
    erro = False  # so para com a resposta 100% certa, só é possível em problemas lineares

    for f in range(0, numeroAmostras):  # numero de casos de testes e nao de entradas
        saida = (soma(entradas[f]))  # uma variavel única pois da trabalho resetar a lista a cada treinamento

        if saida != respostas[f]:  # verifica
            erro = True
            novoPeso(respostas[f], saida, entradas[f])
            print(f"Novos pesos: {pesos}")

    epocas += 1  # numero de treinamentos


# ---------  Rede Treinada ------------


entradasFinais = []
saidas = []
for entrada in entradasFinais:
    saidas.append(soma(entrada))

print(f"Saida: {saidas}")
print(f"Pesos Iniciais: {pesosIniciais}")
print(f"Pesos Finais: {pesos}")
print(f"Taxa de Aprendizado: {taxa} ")
print(f"Epocas: {epocas}")

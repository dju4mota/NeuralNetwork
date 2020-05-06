import random
entradas = [[-1, -0.6508, 0.1097, 4.0009], [-1, -1.4492, 0.8896, 4.4005],
            [-1, 2.0850, 0.6876, 12.0710], [-1, 0.2626, 1.1476, 7.7985],
            [-1, 0.6418, 1.0234, 7.0427], [-1, 0.2569, 0.6730, 8.3265],
            [-1, 1.1155, 0.6403, 7.4446], [-1, 0.0914, 0.3399, 7.0677],
            [-1, 0.0121, 0.5256, 4.6316], [-1, -0.0429, 0.4660, 5.4323],
            [-1, 0.4340, 0.6870, 8.2287], [-1, 0.2735, 1.0287, 7.1934],
            [-1, 0.4839, 0.4851, 7.4850], [-1, 0.4089, -0.1267, 5.5019],
            [-1, 1.4391, 0.1614, 8.5843], [-1, -0.9115, -0.1973, 2.1962],
            [-1, 0.3654, 1.0475, 7.4858], [-1, 0.2144, 0.7515, 7.1699],
            [-1, 0.2013, 1.0014, 6.5489], [-1, 0.6483, 0.2183, 5.8991],
            [-1, -0.1147, 0.2242, 7.2435], [-1, -0.7970, 0.8795, 3.8762],
            [-1, -1.0625, 0.6366, 2.4707], [-1, 0.5307, 0.1285, 5.6883],
            [-1, -1.2200, 0.7777, 1.7252], [-1, 0.3957, 0.1076, 5.6623],
            [-1, -0.1013, 0.5989, 7.1812], [-1, 2.4482, 0.9455, 11.2095],
            [-1, 2.0149, 0.6192, 10.9263], [-1, 0.2012, 0.2611, 5.4631]
            ]
respostas = [-1, -1, -1, 1, 1,
             -1, 1, -1, 1, 1,
             -1, 1, -1, -1, -1,
             -1, 1, 1, 1, 1,
             -1, 1, 1, 1, 1,
             -1, -1, 1, -1, 1
             ]
taxa = 0.01
epocas = 0
erro = True
pesos = [round(random.random(), 3), round(random.random(), 3), round(random.random(), 3), round(random.random(), 3)]
pesosIniciais = pesos.copy()
numeroEntradas = 4
numeroAmostras = 30


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


# treinamento


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


# rede ja treinada

saidas = []

entradasFinais = [[-1, -0.3665, 0.0620, 5.9891], [-1, -0.7842, 1.1267, 5.5912],
                  [-1, 0.3012, 0.5611, 5.8234], [-1, 0.7757, 1.0648, 8.0677],
                  [-1, 0.1570, 0.8028, 6.3040], [-1, -0.7014, 1.0316, 3.6005],
                  [-1, 0.3748, 0.1536, 6.1537], [-1, -0.6920, 0.9404, 4.4058],
                  [-1, -1.3970, 0.7141, 4.9263], [-1, -1.8842, -0.2805, 1.2548]]


for entrada in entradasFinais:
    saidas.append(soma(entrada))

print(f"Saida: {saidas}")
print(f"Pesos Iniciais: {pesosIniciais}")
print(f"Pesos Finais: {pesos}")
print(f"Taxa de Aprendizado: {taxa} ")
print(f"Epocas: {epocas}")

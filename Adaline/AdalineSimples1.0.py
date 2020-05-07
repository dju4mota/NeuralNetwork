import random
entradas = [[-1, 0.4329, -1.3719, 0.7022, -0.8535], [-1, 0.3024, 0.2286, 0.8630, 2.7909],
            [-1, 0.1349, -0.6445, 1.0530, 0.5687], [-1, 0.3374, -1.7163, 0.3670, -0.6283],
            [-1, 1.1434, -0.0485, 0.6637, 1.2606], [-1, 1.3749, -0.5071, 0.4464, 1.3009],
            [-1, 0.7221, -0.7587, 0.7681, -0.5592], [-1, 0.4403, -0.8072, 0.5154, -0.3129],
            [-1, -0.5231, 0.3548, 0.2538, 1.5776], [-1, 0.3255, -2.000, 0.7112, -1.1209],
            [-1, 0.5824, 1.3915, -0.2291, 4.1735], [-1, 0.1340, 0.6081, 0.4450, 3.2230],
            [-1, 0.1480, -0.2988, 0.4778, 0.8649], [-1, 0.7359, 0.1869, -0.0872, 2.3584],
            [-1, 0.7115, -1.1469, 0.3394, 0.9573], [-1, 0.8251, -1.2840, 0.8452, 1.2382],
            [-1, 0.1569, 0.3712, 0.8825, 1.7633], [-1, 0.0033, 0.6835, 0.5389, 2.8249],
            [-1, 0.4243, 0.8313, 0.2634, 3.5855], [-1, 1.0490, 0.1326, 0.9138, 1.9792],
            [-1, 1.4276, 0.5331, -0.0145, 3.7286], [-1, 0.5971, 1.4865, 0.2904, 4.6069],
            [-1, 0.8475, 2.1479, 0.3179, 5.8235], [-1, 1.3967, -0.4171, 0.6443, 1.3927],
            [-1, 0.0044, 1.5378, 0.6099, 4.7755],  [-1, 0.2201, -0.5668, 0.0515, 0.7829],
            [-1, 0.6300, -1.2480, 0.8591, 0.8093],  [-1, -0.2479, 0.8960, 0.0547, 1.7381],
            [-1, -0.3088, -0.0929, 0.8659, 1.5483], [-1, -0.5180, 1.4974, 0.5453, 2.3993],
            [-1, 0.6833, 0.8266, 0.0829, 1.5483], [-1, 4353, -1.4066, 0.4207, -0.4879],
            [-1, -0.1069, -3.2329, 0.1856, -2.4572], [-1, 0.4662, 0.6261, 0.7304, 3.4370],
            [-1, 0.8298, -1.4089, 0.3119, 1.3235]]
respostas = [1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, 1, -1, -1, 1,
             -1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1]
taxa = 0.0025
epocas = 0
erroMedio = 1
erroMedioAntigo = 0
precisao = 0.000001
pesos = [round(random.random(), 3), round(random.random(), 3), round(random.random(), 3), round(random.random(), 3),
         round(random.random(), 3)]
pesosIniciais = pesos.copy()
numeroEntradas = len(entradas[0])
numeroAmostras = len(entradas)


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

entradasFinais = [[-1, 0.4329, -1.3719, 0.7022, -0.8535], [-1, 0.3024, 0.2286, 0.8630, 2.7909],
                  [-1, 0.1349, -0.6445, 1.0530, 0.5687], [-1, 0.3374, -1.7163, 0.3670, -0.6283],
                  [-1, 1.1434, -0.0485, 0.6637, 1.2606], [-1, 1.3749, -0.5071, 0.4464, 1.3009]]
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

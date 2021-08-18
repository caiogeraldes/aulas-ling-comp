#! /usr/bin/python3

# Algoritmo besta de multiplicação sem utilizar multiplicação

def multiplicacao_besta (base, fator):
    saida = 0
    for i in range(fator):
        saida += base
    return saida

if __name__ == "__main__":
    print(multiplicacao_besta(2,5))


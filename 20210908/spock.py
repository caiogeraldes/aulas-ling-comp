#!/usr/bin/python3

spocky = "Ozhika tor wuh palikaya t' kau; ri wuh shaht"

letras = [x for x in list(spocky) if x.isalpha()]
# Ou
letras2 = []
for letra in list(spocky):
    if letra.isalpha():
        letras2.append(letra)


alfabeto = set([x.lower() for x in letras])
# Ou
alfabeto2 = set()
for letra in letras:
    alfabeto2.add(letra.lower())

alfabeto_ord = sorted(alfabeto)  # ou alfabeto2


spocky_limpo = "".join([x for x in spocky if x not in [";"]])
vocab_num = [(x, len(x)) for x in spocky_limpo.split()]
# Ou
vocab_num2 = []
for palavra in spocky_limpo.split():
    vocab_num2.append((palavra, len(palavra)))


if __name__ == "__main__":
    print(spocky)
    print(letras)
    print(alfabeto)
    print(alfabeto_ord)
    print(vocab_num)

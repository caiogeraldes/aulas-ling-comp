"""
    Criar um dicionário cujas chaves sejam os ingredientes (ex.: açúcar mascavo) e os valores sejam uma tupla contendo a medida (ex. colher (chá)) e as respectivas quantidades (ex.: 1).

    Feito o dicionário, imprima com base nele a lista completa de ingredientes no mesmo formato que você vê no site da Bela Gil (ex.: 3 colheres (sopa) de cacau em pó). Dica: os ingredientes não precisam aparecer na mesma ordem que está no site.

    Mostre a quantidade de cacau em pó usada na receita.

    Você não tem a impressão de quem açúcar demais ali? Diminua a quantidade de açúcar pela metade.

    Acrescente o licor de sua preferência à lista de ingredientes.

    O que acontece se você procurar no dicionário por um ingrediente inexistente (ex.: leite condensado)?


    Ingredientes:

biomassa de 2 bananas verdes
5 colheres (sopa) de açúcar mascavo
3 colheres (sopa) de cacau em pó
1 colher (chá) de manteiga ghee
5 gotas de essência de baunilha
"""


# 1  Criar um dicionário cujas chaves sejam os ingredientes (ex.: açúcar mascavo) e os valores sejam uma tupla contendo a medida (ex. colher (chá)) e as respectivas quantidades (ex.: 1).

ingredientes = {"biomassa": ("banana verde", 2),
                "açúcar mascavo": ("colher (sopa)", 5),
                "cacau em pó": ("colher (sopa)", 3),
                "manteiga ghee": ("colher (chá)", 1),
                "essência de baunilha": ("gotas", 5)
                }


# 2 Feito o dicionário, imprima com base nele a lista completa de ingredientes no mesmo formato que você vê no site da Bela Gil (ex.: 3 colheres (sopa) de cacau em pó). Dica: os ingredientes não precisam aparecer na mesma ordem que está no site.

nomes = list(ingredientes.keys())

for i in range(len(nomes)):
    print(ingredientes[nomes[i]][1], ingredientes[nomes[i]][0], "de", nomes[i])


# 3 Mostre a quantidade de cacau em pó usada na receita.
print("Quantidade de cacau em pó em",
      ingredientes["cacau em pó"][0], ":", ingredientes["cacau em pó"][1])

# 4 Você não tem a impressão de quem açúcar demais ali? Diminua a quantidade de açúcar pela metade.
ingredientes["açúcar mascavo"] = (ingredientes["açúcar mascavo"][0],
                                  ingredientes["açúcar mascavo"][1] / 2)
print(f'açúcar mascavo: {ingredientes["açúcar mascavo"]}')

# 5 Acrescente o licor de sua preferência à lista de ingredientes.

ingredientes["licor"] = ("ml", 10)
print(ingredientes)

# 6 O que acontece se você procurar no dicionário por um ingrediente inexistente (ex.: leite condensado)?

ingredientes["pipoca"]

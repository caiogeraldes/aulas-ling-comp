"""
exercício
"""

from string import punctuation
from collections import Counter

PUNCTUATION = punctuation + "—"


def limpa(texto: str) -> str:
    """
    Remove pontuação do texto.
    """
    return ''.join([x for x in texto.lower() if x not in PUNCTUATION])


def tokeniza(texto: str, tipo: str) -> list[str]:
    """
    Retorna tokenização em sent(enças), pal(alavras) e car(acteres).
    """
    output = []
    if tipo == 'sent':
        output = [x for x in texto.split('\n') if len(x) > 0]
    elif tipo == 'pal':
        output = limpa(texto).split()
    elif tipo == 'car':
        output = list(limpa(texto))

    return output


def mais_comuns(vocabulario: Counter, num: int) -> list[tuple[str, int]]:
    """
    Retorna uma lista de dimensão num das palavras mais frequentes.
    """
    return vocabulario.most_common(num)


def hapax(vocabulario: Counter) -> list[str]:
    """
    Retorna uma lista das palavras com apenas uma ocorrência.
    """
    return [x for x, y in vocabulario.items() if y == 1]


def principal(arquivo: str) -> None:
    """
    Principal
    """
    with open(arquivo, 'r', encoding='utf8') as file:
        corpus = file.read()

    print(f'Análise do arquivo:\t{arquivo}')
    print()
    print(f'Número de sentenças:\t{len(tokeniza(corpus, "sent"))}')
    print()

    palavras = tokeniza(corpus, 'pal')
    print(f'Número de palavras:\t{len(palavras)}')
    print()
    print(f'Número de caracteres:\t{len(tokeniza(corpus,"car"))}')
    print()

    vocabulario = Counter(palavras)
    print(f'Tamanho vocabulário:\t{len(vocabulario)}')
    print()
    print("Cem palavras mais frequentes:")
    print(vocabulario.most_common(100))
    print()

    print("Hapax Legomena (100)")
    hapaxes = hapax(vocabulario)
    print(hapaxes[0:100])


if __name__ == '__main__':
    principal('../data/guarani.txt')

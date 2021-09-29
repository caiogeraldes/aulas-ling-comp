#!/usr/bin/python3
"""
Exercício usando NLTK
"""
import random

try:
    from nltk.tokenize import word_tokenize, sent_tokenize
    from nltk.stem import RSLPStemmer
    from nltk.stem.snowball import EnglishStemmer
    from nltk.corpus import stopwords
except Exception as e:
    raise e


def tokeniza_sem_stops(texto: str, lingua: str = 'portuguese') -> list[str]:
    """
    Retorna lista de tokens excluindo palavras vazias.
    """
    tokens = word_tokenize(texto, language=lingua)
    stops = stopwords.words(lingua)

    return [x for x in tokens if x not in stops]


def limpa_punct(tokens: list[str]) -> list[str]:
    """
    Remove pontuação da lista de tokens.
    """
    return [x for x in tokens if x.isalpha()]


def stemizacao(texto: str, lingua: str = 'portuguese') -> list[str]:
    """
    Retorna lista de stems dos tokens limpos de palavras vazias.
    """
    if lingua == 'portuguese':
        raiz = RSLPStemmer().stem
    elif lingua == 'english':
        raiz = EnglishStemmer().stem
    return [raiz(x) for x in limpa_punct(tokeniza_sem_stops(texto, lingua))]


def main(arquivo: str, lingua: str = 'portuguese') -> None:
    """
    Main
    """
    with open(arquivo, "r", encoding="utf8") as file:
        corpus = sent_tokenize(file.read(), language=lingua)

    texto = corpus[random.randint(0, len(corpus)-1)]
    print(texto)
    print("Tokens sem as stop:")
    print(tokeniza_sem_stops(texto, lingua))
    print()
    print("Stems")
    print(stemizacao(texto, lingua))


if __name__ == '__main__':
    ARQUIVO = "../../data/guarani.txt"
    main(ARQUIVO)
    print()
    ARQUIVO2 = "../../data/ratoroeu.txt"
    main(ARQUIVO2)
    print()
    ARQUIVO3 = "../../data/ataque_carangueijos.txt"
    main(ARQUIVO3, lingua="english")

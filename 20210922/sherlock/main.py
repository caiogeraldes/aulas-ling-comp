import pandas as pd
from string import punctuation
from collections import Counter

punctuation = punctuation + "—"

def limpa(texto: str) -> str:
    return ''.join([x for x in texto.lower() if x not in punctuation])


def tokeniza(texto: str, tipo: str) -> list[str]:
    if tipo == 'sent':
        return [x for x in texto.split('\n') if len(x) > 0]
    elif tipo == 'pal':
        return limpa(texto).split()
    elif tipo == 'car':
        return list(limpa(texto))
    else:
        print('O argumento tipo deve ser sent, pal ou car')
        raise BaseException


def principal(arquivo: str) -> None:
    with open(arquivo, 'r') as file:
        corpus = file.read()

    print(f'Análise do arquivo:\t{arquivo}')
    print(f'Número de sentenças:\t{len(tokeniza(corpus, "sent"))}')

    palavras = tokeniza(corpus, 'pal')
    print(f'Número de palavras:\t{len(palavras)}')

    print(f'Número de caracteres:\t{len(tokeniza(corpus,"car"))}')

    vocabulario = Counter(palavras)
    print(f'Tamanho vocabulário:\t{len(vocabulario)}')


    print("Dez palavras mais frequentes:")
    for k, v in vocabulario.most_common(10):
        print(f'\t\t{k}\t{v}')

    # Salva dicionário como csv
    df = pd.DataFrame.from_dict(vocabulario, orient='index').reset_index()
    df.to_csv(arquivo.replace(".txt", ".csv"), sep=',', encoding='utf-8')



if __name__ == '__main__':
    principal('guarani.txt')

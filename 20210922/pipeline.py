import statistics as st

def palavras(texto: str) -> list[str]:
    return [palavra.lower() for palavra in texto.split()]


def limpar(palavras: list[str]) -> list[str]:
    return [palavra for palavra in palavras if palavra.isalpha()]


def pipeline(texto: str) -> list[str]:
    return limpar(palavras(texto))


def vocab(texto: str) -> set:
    return set(pipeline(texto))


def conta_vocab(texto: str) -> list[tuple[str, int]]:
    lst_texto = pipeline(texto)
    return [(lexema, lst_texto.count(lexema)) for lexema in  vocab(texto)]


def car_total(texto_input: str) -> int:
    return len(texto_input)


def car_sem_espaco(texto_input: str) -> int:
    return len(texto_input.replace(" ", ""))


def conta_palavra(texto_input: str) -> int:
    return len(pipeline(texto_input))


def tamanho_vocab(texto_input: str) -> int:
  return len(vocab(texto_input))


def tamanho_medio(texto_input: str, vocabulario: bool = False) -> float:
  tamanhos = []
  if vocabulario:
    tamanhos = [len(palavra) for palavra in vocab(texto_input)]
  else:
      tamanhos = [len(palavra) for palavra in pipeline(texto_input)]

  return st.mean(tamanhos)


def desvio_padrao(texto_input: str, vocabulario: bool = False) -> float:
  tamanhos = []
  if vocabulario:
    tamanhos = [len(palavra) for palavra in vocab(texto_input)]
  else:
      tamanhos = [len(palavra) for palavra in pipeline(texto_input)]

  return st.stdev(tamanhos)


if __name__ == "__main__":
    with open("../data/ataque_carangueijos.txt", "r") as file:
        TEXTO = file.read()

    print("Caracteres")
    print("Total:\t\t\t", car_total(TEXTO))
    print("Sem espaço:\t\t", car_sem_espaco(TEXTO))
    print()
    print("Palavras:\t\t", conta_palavra(TEXTO))
    print()
    print("Vocabulário:\t\t", tamanho_vocab(TEXTO))
    print()
    print("Tamanho médio das palavras")
    print("Contando repetições:\t", tamanho_medio(TEXTO,
                                                vocabulario = False))
    print("Do vocabulário:\t\t", tamanho_medio(TEXTO,
                                                  vocabulario = True))
    print()
    print("Desvio padrão do tamanho das palavras")
    print("Contanto repetições:\t", desvio_padrao(TEXTO,
                                           vocabulario = False))
    print("Do vocabulário:\t\t", desvio_padrao(TEXTO,
                                                  vocabulario = True))


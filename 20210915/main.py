import statistics as st
import pandas as pd
from typing import List, Tuple


def palavras(texto: str) -> List[str]:
    return [palavra.lower() for palavra in texto.split()]


def limpar(palavras: List[str]) -> List[str]:
    return [palavra for palavra in palavras if palavra.isalpha()]


def pipeline(texto: str) -> List[str]:
    return limpar(palavras(texto))


def vocab(texto: str, limpo: bool = True) -> List[str]:
  if limpo:
    return set(pipeline(texto))
  else:
    return set(palavras(texto))


def conta_vocab(texto: str) -> List[Tuple[str, int]]:
  lst_texto = pipeline(texto)
  return [(lexema, lst_texto.count(lexema)) for lexema in  vocab(texto)]


def car_total(texto: str) -> int:
  return len(texto)


def car_sem_espaco(texto: str, espacos_brancos: List[str] = [" "]) -> int:
  return len([x for x in texto if x not in espacos_brancos])


def conta_palavra(texto: str, limpo: bool = False) -> int:
  if limpo:
    return len(pipeline(texto))
  else:
    return len(palavras(texto))


def tamanho_vocab(texto: str, limpo: bool = False) -> int:
  return len(vocab(texto, limpo))


def tamanho_medio(texto: str, limpo: bool = False, vocabulario: bool = False) -> float:
  tamanhos = []
  if vocabulario:
    tamanhos = [len(palavra) for palavra in vocab(texto, limpo)]
  else:
    if limpo:
      tamanhos = [len(palavra) for palavra in pipeline(texto)]
    else:
      tamanhos = [len(palavra) for palavra in palavras(texto)]
  return st.mean(tamanhos)


def desvio_padrao(texto: str, limpo: bool = False, vocabulario: bool = False):
  tamanhos = []
  if vocabulario:
    tamanhos = [len(palavra) for palavra in vocab(texto, limpo)]
  else:
    if limpo:
      tamanhos = [len(palavra) for palavra in pipeline(texto)]
    else:
      tamanhos = [len(palavra) for palavra in palavras(texto)]
  return st.stdev(tamanhos)


if __name__ == '__main__':
    TEXTO = """Apparently we have one of those biological freaks resulting from an overdose of radiation poisoning. The way to explain it is... Look. Electricity. The free electron in the copper atom breaks off to circle the next atom, taking the charge along the wire. The free electrons jump from atom to atom along the copper at the speed of light.

Well, something like that has happened to our crab. But instead of free electrons, the crab has free atoms... All disconnected. It's like a mass of liquid... with a permanent shape.

Any metal, therefore, that the crab eats will be assimilated in his body of solid energy, becoming part of the crab."""
    print("Caracteres")
    print("Total: ", car_total(TEXTO))
    print("Sem espaço: ", car_sem_espaco(TEXTO))
    print("Sem espaço, sem quebra de linha: ", car_sem_espaco(TEXTO, [" ", "\n"]))
    print()
    print("Palavras")
    print("Total: ", conta_palavra(TEXTO, limpo = False))
    print("Limpo: ", conta_palavra(TEXTO, limpo = True))
    print()
    print("Vocabulário")
    print("Total: ", tamanho_vocab(TEXTO, limpo = False))
    print("Limpo: ", tamanho_vocab(TEXTO, limpo = True))
    print()
    print("Tamanho médio das palavras")
    print("Considerando todas:\t", tamanho_medio(TEXTO, limpo = False, vocabulario = False))
    print("Apenas limpas:\t\t", tamanho_medio(TEXTO, limpo = True, vocabulario = False))
    print("Do vocabulário todo:\t", tamanho_medio(TEXTO, limpo = False, vocabulario = True))
    print("Do vocabulário limpo:\t", tamanho_medio(TEXTO, limpo = True, vocabulario = True))
    print()
    print("Desvio padrão do tamanho das palavras")
    print("Considerando todas:\t", desvio_padrao(TEXTO, limpo = False, vocabulario = False))
    print("Apenas limpas:\t\t", desvio_padrao(TEXTO, limpo = True, vocabulario = False))
    print("Do vocabulário todo:\t", desvio_padrao(TEXTO, limpo = False, vocabulario = True))
    print("Do vocabulário limpo:\t", desvio_padrao(TEXTO, limpo = True, vocabulario = True))
    print()
    print("Contagem de ocorrências")
    print(pd.DataFrame(conta_vocab(TEXTO), columns = ["Lexema", "n"]).sort_values(by="n", ascending = False))

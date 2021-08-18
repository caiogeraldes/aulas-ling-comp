# Curso de Linguística Computacional

Anotações do curso de Linguística Computacional do programa de pós da
Linguística oferecida pelo DL FFLCH-USP. Segundo semestre de 2021.

Todas as anotações e código são de minha responsabilidade.

## Introdução

Aula de 2021-08-18

### Algoritmos e programas

Algumas informações sobre diferença entre algoritmo e implementação.

Algo como: para multiplicar sem uma tabuada, deve-se adicionar
n vezes o número de base. A implementação poderá ser feita em várias
línguas:

- Python
```{python}
# Apenas para positivos
def multiplicacao (base, fator):
    saida = 0
    for i in range(fator):
        saida += base
    return saida
```

- R
```{r}
# Apenas para positivos
multiplicacao <- function(base, fator) {
    saida = 0
    while (fator > 0) {
        saida = saida + base
        fator = fator -1
    }
    return(saida)
}
```

### IA

#### IA Geral

Não há um método geral de solução de problemas em IA, i.e. um modelo para resolver toda e qualquer tarefa.

#### IA e LC/NLP/PLN

A tradução automática foi uma das primeira tarefas dada à IA e um dos seu primeiros desafios.
Hoje se considera ela uma tarefa *IA-completa*, uma tarefa de IA cujo desempenho satisfatório exige que
várias sub-tarefas dela tenham sido solucionadas.
As tarefas da PLN tem sido essas sub-tarefas.

### Tarefas linguísticas da IA

- *Bag of words* (`BoW`) é o nome dado para técnicas de processamento baseada em palavras ou termos isolados, desprezando consideração à sintaxe ou contexto.

- Tokenização é o isolamento das unidades de uma `BoW`.
    - Outro uso: type: `VERBO`, token: `cantar`

- Eliminação das palavras vazias, as *stop-words*: preposições, artigos etc.

- Stemização (tematização): `comprar` -> `compr` etc.
    - computacionalmente rápido e executado em tempo linear, mas gera formas irreais e artificialmente ambíguas.
    - o mr. 𐤢𐤬𐤬𐤢𐤩𐤤 usa isso desde 2003


- POS tagging ~ análise morfossintática
- Análise de dependências sintáticas

- Tarefas integradas
    - Tradução automática (Machine Translation)
    - Geração de Texto
    - Sumarização de Texto
    - Análise de Sentimento
    - Reconhecimento de Entidades Nomeadas (`NER`)
    - Desambiguação de Sentidos de Palavras (`WSD`)
    - Inferência em Linguagem Natural (`NLI`)
    - Perguntas e Respostas (`Q&A`)
    - Reconhecimento de Voz
    - Síntese de Voz
    - Reconhecimento de Linguagem Natural (`NLU`)


### Aprendizado de máquina (`ML`)

Os primeiro sistemas eram baseados em tabelas alinhadas, depois se incrementou o modelo com regras probabilísticas baseadas em corpora.
Sistemas baseados em regras de maneira escalonada (tokenização, etiquetamento etc) até sistemas integrados.
Algumas regras podem ser pulados em um ML.
A conversão dos sistemas é relativamente simples.

## Aula 1

[Anotações](./20210818/LC_Pós_Python_1.ipynb).

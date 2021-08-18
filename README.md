# Curso de Linguística Computacional

Anotações do curso de Linguística Computacional do programa de pós da
Linguística oferecida pelo DL FFLCH-USP. Segundo semestre de 2021.

Todas as anotações e código são de minha responsabilidade.

## Introdução

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

## IA

### IA Geral

Não há um método geral de solução de problemas em IA, i.e. um modelo para resolver toda e qualquer tarefa.

### IA e LC/NLP/PLN

A tradução automática foi uma das primeira tarefas dada à IA e um dos seu primeiros desafios.
Hoje se considera ela uma tarefa *IA-completa*, uma tarefa de IA cujo desempenho satisfatório exige que
várias sub-tarefas dela tenham sido solucionadas.




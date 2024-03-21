# TPC6: Gramática Independente de Contexto LL(1)

## Autor
- A100600
- Diogo Rafael dos Santos Barros

## Resumo

- **Definição da Linguagem**: possui **terminais** como números, variáveis, operadores aritméticos, parênteses, igualdade, leitura e impressão. Os **não-terminais** incluem o programa (P), declaração (D), expressão (E), termo (T) e fator (F).

- **Produções da Gramática**: descrevem como os diferentes símbolos da linguagem podem ser combinados para formar expressões válidas. 

- **Lookahead Sets**: são determinados para cada **produção**, indicando os símbolos que podem seguir imediatamente após a expansão da produção.

- **Interseções dos Lookahead**: são calculadas para garantir que a gramática seja LL(1).

### Frases Exemplo

- `? a`
- `b = a * 2 / (27 - 3)`
- `! a + b`
- `c = a * b / (a / b)`
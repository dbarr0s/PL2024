# Gramática Independente de Contexto LL(1)

## Terminais:

- **Números**: `num`
- **Variáveis**: `var`
- **Operadores Aritméticos**: `+ | - | * | /`
- **Parênteses**: `( | )`
- **Igualdade**: `=`
- **Leitura**: `?`
- **Impressão**: `!`

## Não-Terminais

- **Programa**: `P`
- **Declaração** (variável ou um comando de leitura/impressão): `D`
- **Expressão**: `E`
- **Termo**: `T`
- **Fator** (uma variável ou uma expressão entre parênteses): `F`

## Produções

1. `P -> D P | ε`
2. `D -> var = E | ? var | ! E`
3. `E -> T | + T E | - T E`
4. `T -> F | * F T | / F T`
5. `F -> var | num | ( E )`

## Lookahead Sets

1. **LA(P → D P)**: `var` `?` `!`
2. **LA(P → ε)**: `$` (espaço)

3. **LA(D → var = E)**: `var`
4. **LA(D → ? var)**: `?`
5. **LA(D → ! E)**: `!`

6. **LA(E → T)**: `var` `num` `(`
7. **LA(E → + T E)**: `+`
8. **LA(E → - T E)**: `-`

9. **LA(T → F)**: `var` `num` `(`
10. **LA(T → * F T)**: `*`
11. **LA(T → / F T)**: `/`

12. **LA(F → var)**: `var`
13. **LA(F → num)**: `num`
14. **LA(F → ( E ))**: `(`

## Interseções dos Look Ahead

1. **LA(1) ∩ LA(2)** = {`var`, `?`, `!`} ∩ {`$`} = {}

2. **LA(3) ∩ LA(4) ∩ LA(5)** = {`var`} ∩ {`?`} ∩ {`!`} = {}

3. **LA(6) ∩ LA(7) ∩ LA(8)** = {`var`, `num`, `(`} ∩ {`+`} ∩ {`-`} = {}

4. **LA(9) ∩ LA(10) ∩ LA(11)** = {`var`, `num`, `(`} ∩ {`*`} ∩ {`/`} = {}

5. **LA(12) ∩ LA(13) ∩ LA(14)** = {`var`} ∩ {`num`} ∩ {`(`} = {}
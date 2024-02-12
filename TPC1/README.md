# TPC1 - Processamento de Dados de Atletas (Análise de um Dataset)
Este projeto consiste em um programa de Python para analisar/processar os dados de atletas contidos num arquivo CSV.      

O objetivo é realizar análises estatísticas sobre os atletas e gerar resultados como:
- Uma lista ordenada de modalidades desportivas;
- Percentagem de atletas aptos e inaptos; 
- Distribuição de atletas por faixas etárias.

## Autor
- Diogo Rafael dos Santos Barros
- A100600

## Funcionalidades Implementadas:
1. Parser de um Arquivo CSV (parse_csv):
- Função para ler um arquivo CSV e converter seus dados em uma estrutura de lista de listas. Esta funcção devolve o cabeçalho do arquivo CSV e os dados sem o cabeçalho.

2. Obtenção de Modalidades Desportivas (obter_modalidades):
- Função para extrair e ordenar alfabeticamente as modalidades desportivas presentes nos dados. Esta função devolve uma lista ordenada das modalidades desportivas.

3. Percentagem de Atletas Aptos e Inaptos (percentagem_aptos_inaptos):
- Função para calcular a percentagem de atletas aptos e inaptos para a prática desportiva. Esta função devolve um par, com a percentagem de atletas aptos e a percentagem de atletas inaptos.

4. Distribuição de Atletas por Faixas Etárias (faixas_etarias):
- Função para agrupar os atletas em faixas etárias de 5 anos e contar o número de atletas em cada faixa. Esta função devolve um dicionário onde as chaves são as faixas etárias e os valores são listas de pares, que contêm o primeiro e último nome dos atletas.

5. Criação de Resultados e Escrita em Arquivo .txt (main):
- Função principal que executa todas as etapas do processamento de dados e gera os resultados. Escreve os resultados num arquivo de texto chamado results.txt na pasta TPC1.

## Utilização:
- Execute o script tpc1.py para processar os dados e gerar os resultados.
- Verifique o arquivo results.txt, localizado na pasta TPC1 para aceder aos resultados.


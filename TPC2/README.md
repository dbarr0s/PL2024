# TPC2 - Conversor de MD para HTML
Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:

- **Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"**
   ```
   In: # Exemplo
   Out: <h1>Exemplo</h1>
   ```
- **Bold: pedaços de texto entre "**":**
  ```
  In: Este é um **exemplo** ...
  Out: Este é um <b>exemplo</b> ...
  ```
- **Itálico: pedaços de texto entre "*":**
  ```
  In: Este é um *exemplo* ...
  Out: Este é um <i>exemplo</i> ...
  ```
- **Lista numerada:**
  ```
  In:
      1. Primeiro item
      2. Segundo item
      3. Terceiro item
  Out:
      <ol>
      <li>Primeiro item</li>
      <li>Segundo item</li>
      <li>Terceiro item</li>
      </ol>
  ```
- **Link: [texto](endereço URL)**
  ```
  In: Como pode ser consultado em [página da UC](http://www.uc.pt)
  Out: Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>
  ```
- **Imagem: ![texto alternativo](path para a imagem)**
  ```
  In: Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
  Out: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...
  ```

## Autor
- Diogo Rafael dos Santos Barros
- A100600

## Resumo:
1. **markdown_to_html(markdown):**
- Esta função usa expressões para substituir padrões específicos encontrados no texto Markdown por tags HTML correspondentes.

2. **create_html_file(filename, content):**
- Esta função cria um arquivo HTML com o nome especificado e o conteúdo fornecido.

3. **main():**
- Esta função é a principal do programa. Ela lê o conteúdo de um arquivo Markdown especificado (exemplo.md), converte-o para HTML usando a função markdown_to_html, e então cria um arquivo HTML (exemplo.html) com o conteúdo convertido.

Em resumo, este código é capaz de converter um arquivo Markdown em HTML, mantendo a formatação básica, como títulos, texto em negrito e itálico, listas ordenadas e não ordenadas, links e imagens.






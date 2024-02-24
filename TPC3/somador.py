import re

def somador(arquivo):
    # Inicializa o somador e o estado do somador
    soma = 0
    ligado = False

    # Abre o arquivo em modo de leitura
    with open(arquivo, 'r') as file:
        # Lê o conteúdo do arquivo
        texto = file.read()

        # Ajuste da expressão regular para capturar números inteiros positivos e negativos
        lista = re.findall(r'(off|on|=|-?\d+)', texto, flags=re.IGNORECASE)
        print(lista)
        # Itera sobre as sequências encontradas
        for element in lista:
            if element.lower() == 'on':
                ligado = True
            elif element.lower() == 'off':
                ligado = False
            elif element == '=':
                print(f'Resultado do momento = {soma}')
            else:
                num = int(element)
                if ligado:
                    soma += num
    # Retorna a soma final
    return soma

def main():
    resultado_final = somador("somador.txt")
    print(f'Resultado Final = {resultado_final}')

if __name__ == '__main__':
    main()
def parse_csv(file_path):
    # Abrir o arquivo CSV e ler as linhas
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Remover quebras de linha e dividir os campos por vírgulas
    data = [line.strip().split(',') for line in lines]

    header = data[0] # Este cabeçalho é o formato do csv
    dados = data[1:] # Os dados representados pelo formato do cabeçalho, num array

    return header, dados

def obter_modalidades(data):    
    # Criar um conjunto para armazenar as modalidades únicas
    modalidades_unicas = set()
    
    for linha in data:
        modalidades_unicas.add(linha[8])
    
    # Ordenar alfabeticamente as modalidades e retornar como uma lista
    modalidades_ordenadas = sorted(modalidades_unicas)
    
    return modalidades_ordenadas

def percentagem_aptos_inaptos(data):
    aptos = 0
    total_atletas = 0
    
    for linha in data:
        total_atletas = len(data)
        if (linha[12] == "true"):
            aptos = aptos + 1
            
    percentagem_aptos = (aptos / total_atletas) * 100
    percentagem_inaptos = 100 - percentagem_aptos
    
    return (percentagem_aptos, percentagem_inaptos)

def faixas_etarias(data):   
    faixas_etarias = {
        '[20-24]': [],
        '[25-29]': [],
        '[30-34]': [],
        '[35-39]': []
    }

    for row in data:
        primeiro_nome = row[3]
        ultimo_nome = row[4]
        idade = int(row[5])

        if 20 <= idade <= 24:
            faixas_etarias['[20-24]'].append((primeiro_nome, ultimo_nome))
        elif 25 <= idade <= 29:
            faixas_etarias['[25-29]'].append((primeiro_nome, ultimo_nome))
        elif 30 <= idade <= 34:
            faixas_etarias['[30-34]'].append((primeiro_nome, ultimo_nome))
        elif 35 <= idade <= 39:
            faixas_etarias['[35-39]'].append((primeiro_nome, ultimo_nome))

    return faixas_etarias

def main():
    file_path = '../PL2024/TPC1/emd.csv'
    header, data = parse_csv(file_path)
    
    modalidades = obter_modalidades(data)
    
    (percentagem_aptos, percentagem_inaptos) = percentagem_aptos_inaptos(data)
        
    faixas_etaria = faixas_etarias(data)

    with open('TPC1/results.txt', 'w', encoding='utf-8') as file:
        file.write("\n")
                
        file.write(f"Lista ordenada alfabeticamente das modalidades desportivas:\n")
        for modalidade in modalidades:
            file.write(f"- " +modalidade+ "\n")
    
        file.write("\n")
    
        file.write(f"Percentagem de Atletas Aptos: " +str(percentagem_aptos)+ "%\n")
        file.write(f"Percentagem de Atletas Inaptos: " +str(percentagem_inaptos)+ "%\n")
        
        file.write("\n")
        
        # Escrever os nomes dos atletas num arquivo, dividido por faixas etárias e cada uma com o nº de atletas
        idades = [int(row[5]) for row in data]
        idade_min = min(idades)
        idade_max = max(idades)
        file.write(f"Idade Mínima: " +str(idade_min)+ "\n")
        file.write(f"Idade Máxima: " +str(idade_max)+ "\n") 
        
        file.write("\n")
         
        for faixa, nomes in faixas_etaria.items():
            file.write(f"\nFaixa etária {faixa}: {len(nomes)} atletas nesta faixa.\n")
            for primeiro_nome, ultimo_nome in nomes:
                file.write(f"{primeiro_nome} {ultimo_nome}\n")
                
        file.write("\n")

# Chamada da função main
if __name__ == "__main__":
    main()


import pandas as pd
import random
import os

# Carregar o arquivo CSV
file_path = "base_dados_idades.csv"
df = pd.read_csv(file_path)

# Tamanho total da população (N)
N = len(df)

# Proporção da amostra (20%)
P = 0.2

# Calcular o tamanho da amostra (n)
n = int(P * N)

# Gerar um número aleatório entre 1 e 10
numero_aleatorio = random.randint(1, 10)

# Criar uma lista para armazenar os IDs selecionados
ids_selecionados = []

# Loop para selecionar os IDs adicionando 5 a cada iteração
i = numero_aleatorio
while len(ids_selecionados) < n:
    if i < N:  
        ids_selecionados.append(i)
    i += 5
    i %= N  

# Selecionar os dados com base nos IDs selecionados
amostra_aas = df.iloc[ids_selecionados]

# Exibir a amostra no prompt
print("Amostra Aleatória Simples (20% da base):")
print(amostra_aas)

# Calcular a média de idade da amostra
media_idade_total = round(df['Idade'].mean(),0)
media_idade_amostra = round(amostra_aas['Idade'].mean(), 0)

print("Média de idade da amostra aleatória simples:")
print(media_idade_amostra)
print("Média de idade da base de dados completa:")
print(media_idade_total)

# Nome do arquivo de saída
output_file = "amostra_aleatoria_simples.csv"

# Salvar a amostra no arquivo CSV, substituindo se existir
amostra_aas.to_csv(output_file, index=False)

print("Amostra Aleatória Simples (20% da base) salva em", output_file)
print("\nTotal de dados selecionados:", len(amostra_aas))

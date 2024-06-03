import pandas as pd
import random

# Carregar o arquivo CSV
file_path = "base_dados_idades.csv"
df = pd.read_csv(file_path)

# Definir faixas etárias
faixas_etarias = ["0-14 anos", "15-24 anos", "25-34 anos", "35-44 anos", "45-54 anos", "55-64 anos", "65+ anos"]
bins = [0, 14, 24, 34, 44, 54, 64, 100]

# Criar nova coluna de faixas etárias
df['Faixa_Etaria'] = pd.cut(df['Idade'], bins, labels=faixas_etarias, right=True)

# Função para fazer a amostragem estratificada por faixa etária
def amostragem_estratificada_faixa_etaria(df, frac):
    amostra_estratificada = pd.DataFrame()
    medias_idades_faixa_etaria = {}  # Dicionário para armazenar as médias de idade por faixa etária
    for faixa in faixas_etarias:
        # Selecionar os dados para a faixa etária atual
        dados_faixa_etaria = df[df['Faixa_Etaria'] == faixa]
        # Calcular o tamanho da amostra para esta faixa etária
        n_faixa_etaria = int(len(dados_faixa_etaria) * frac)
        # Se o tamanho da amostra for 0, pular para a próxima faixa etária
        if n_faixa_etaria == 0:
            continue
        # Gerar um número aleatório entre 1 e 10
        numero_aleatorio = random.randint(1, 10)
        # Inicializar uma lista para armazenar os IDs selecionados
        ids_selecionados = []
        # Loop para selecionar os IDs adicionando 5 a cada iteração
        i = numero_aleatorio
        while len(ids_selecionados) < n_faixa_etaria:
            if i < len(dados_faixa_etaria):  # Verificar se o índice está dentro do intervalo válido
                ids_selecionados.append(i)
            i += 5
            i %= len(dados_faixa_etaria)  # Garantir que o índice fique dentro do intervalo válido usando o operador módulo
        # Selecionar os dados com base nos IDs selecionados
        amostra_faixa_etaria = dados_faixa_etaria.iloc[ids_selecionados]
        # Adicionar a amostra ao DataFrame final
        amostra_estratificada = pd.concat([amostra_estratificada, amostra_faixa_etaria])
        # Calcular a média de idade para esta faixa etária
        medias_idades_faixa_etaria[faixa] = amostra_faixa_etaria['Idade'].mean()
    return amostra_estratificada, medias_idades_faixa_etaria

# Aplicar a amostragem estratificada por faixa etária
amostra_estratificada_faixa_etaria, medias_idades_por_faixa = amostragem_estratificada_faixa_etaria(df, 0.2)

# Exibir as médias de idade por faixa etária
print("Médias de idade por faixa etária:")
for faixa_etaria, media_idade in medias_idades_por_faixa.items():
    print(f"Faixa etária: {faixa_etaria}, Média de idade: {int(media_idade)}")

# Exibir as porcentagens e quantidades de cada faixa de idade
porcentagens = (amostra_estratificada_faixa_etaria['Faixa_Etaria'].value_counts(normalize=True) * 100).round(2)
quantidades = amostra_estratificada_faixa_etaria['Faixa_Etaria'].value_counts()
print("\nPorcentagem de cada faixa etária:")
print(porcentagens)
print("\nQuantidade de cada faixa etária:")
print(quantidades)

# Exibir a amostra estratificada no prompt
print("\nAmostra Estratificada por Faixa Etária (20% da base):")
print(amostra_estratificada_faixa_etaria)

# Nome do arquivo de saída
output_file = "amostra_aleatoria_estratificada.csv"

# Salvar a amostra estratificada por faixa etária no arquivo CSV
amostra_estratificada_faixa_etaria.to_csv(output_file, index=False)

print("\nAmostra estratificada por faixa etária salva em", output_file)
print("\nTotal de dados selecionados:", len(amostra_estratificada_faixa_etaria))

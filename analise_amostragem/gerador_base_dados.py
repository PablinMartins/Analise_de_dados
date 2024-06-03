import pandas as pd
import numpy as np

# Definir os parâmetros para gerar idades em diferentes faixas etárias
faixas_etarias = {
    "0-14 anos": (0, 14),
    "15-24 anos": (15, 24),
    "25-34 anos": (25, 34),
    "35-44 anos": (35, 44),
    "45-54 anos": (45, 54),
    "55-64 anos": (55, 64),
    "65+ anos": (65, 100)
}

# Proporções para cada faixa etária
proporcoes = [0.2, 0.18, 0.22, 0.16, 0.1, 0.08, 0.06]

# Gerar idades baseadas nas proporções e faixas etárias
idades = []
for (faixa, (inicio, fim)), proporcao in zip(faixas_etarias.items(), proporcoes):
    numero_de_pessoas = int(proporcao * 500)
    idades.extend(np.random.randint(inicio, fim + 1, numero_de_pessoas))

# Caso faltem alguns registros para completar 500 (devido a arredondamentos), completar com idades aleatórias
while len(idades) < 500:
    idades.append(np.random.randint(0, 101))

# Criar o DataFrame
df_idades = pd.DataFrame({
    "ID": range(1, 501),
    "Idade": idades
})

# Salvar o DataFrame em um arquivo CSV
file_path = "base_dados_idades.csv"
df_idades.to_csv(file_path, index=False)
print(f"Arquivo salvo como {file_path}")


import pandas as pd
import xlrd
import os
from extract import carregar_projecoes, carregar_etario, processar_subconjuntos_etario, carregar_instrucao, processar_subconjuntos_instrucao, carregar_socio

csv_path = os.path.join(os.path.dirname(__file__),"csv_temp")

# Tabela 1: Projeções
projecoes_df = carregar_projecoes()

projecoes2_df_filtrado = projecoes_df[
    (projecoes_df["LOCAL"].str.strip() == "Brasil") & 
    (projecoes_df["ANO"].astype(float).between(2018, 2024) | (projecoes_df["ANO"].astype(float) == 2045))
]

colunas_desejadas = ["ANO", "LOCAL", "POP_H", "POP_M", "e0_T", "e60_T"]
projecoes2_df_filtrado = projecoes2_df_filtrado[colunas_desejadas].rename(columns={
    "ANO": "year",
    "LOCAL": "local",
    "POP_H": "pop_h",
    "POP_M": "pop_m",
    "e0_T": "e0_t",
    "e60_T": "e60_t"
})

# Salvar CSV
projecoes2_df_filtrado.to_csv(os.path.join(csv_path,"projecoes.csv"), index=False)

# Tabela 2: Faixa Etária

# Lista com os anos disponíveis
anos = ["2018", "2019", "2020", "2021", "2022", "2023"]

# Carregar os dados e processar os subconjuntos (homens/mulheres) para todos os anos
etario_filtrado = pd.concat(
    [
        pd.concat(processar_subconjuntos_etario(carregar_etario(ano)).values(), axis=0, ignore_index=True)
        for ano in anos
    ], 
    axis=0, ignore_index=True
)

# Ajustes finais no DataFrame
etario_filtrado = etario_filtrado[["year", "sex", "features", "work_pop"]]
etario_filtrado["work_pop"] *= 1000

# Remover as linhas indesejadas
etario_filtrado = etario_filtrado[~etario_filtrado["features"].isin(["14 a 17 anos", "18 a 24 anos", "25 a 29 anos"])]

# Resetar os índices
etario_filtrado = etario_filtrado.reset_index(drop=True)

etario_filtrado.to_csv(os.path.join(csv_path, "faixa_etario.csv"), index=False)


# Tabela 3: Instrução
# Carregar os dados e processar os subconjuntos (homens/mulheres) para todos os anos
socio_filtrado = pd.concat(
    [
        pd.concat(processar_subconjuntos_instrucao(carregar_instrucao(ano)).values(), axis=0, ignore_index=True)
        for ano in anos
    ], 
    axis=0, ignore_index=True
)

# Ajustes finais no DataFrame
socio_filtrado = socio_filtrado[["year", "sex", "degree", "work_pop"]]
socio_filtrado["work_pop"] *= 1000

socio_filtrado.to_csv(os.path.join(csv_path, "faixa_socio.csv"), index=False)

# Tabela 4 e 5: Socioeconômico (Merge entre escolaridade e idade)
idade_inst_sal = carregar_socio()

idade_inst_sal.to_csv(os.path.join(csv_path, "idade_inst_sal.csv"), index=False)

# Exibir os DataFrames processados (opcional, para validação)
print("Projeções filtradas:")
print(projecoes2_df_filtrado.head())

print("\nFaixa Etária filtrada:")
print(etario_filtrado.head())

print("\nInstrução filtrada:")
print(socio_filtrado.head())

print("\nDados Socioeconômicos (idade + escolaridade):")
print(idade_inst_sal.head())

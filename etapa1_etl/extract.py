# Extrair os dados dos arquivos
import pandas as pd
import xlrd

# Tabela 1: Projeções

def carregar_projecoes():
    return pd.read_excel("Tabelas/projecoes_2024_tab4_indicadores.xlsx", skiprows=6)


# Tabela 2: Faixa etária

# Definição das colunas e faixas etárias
colunas_desejadas_etario = {
    "Características selecionadas": "features",
    "População na força de trabalho\n(1 000 pessoas)": "work_pop"
}
faixas_etario = {
    "homens": (15, 22),  # Homens: linhas 18 a 25
    "mulheres": (24, 31) # Mulheres: linhas 27 a 34
}

# Lista com os anos disponíveis
anos = ["2018", "2019", "2020", "2021", "2022", "2023"]

# Função para carregar os dados
def carregar_etario(ano):

    df = pd.read_excel(
        "Tabelas/tabela_1_1_Indic_BR.xls",
        sheet_name=ano,
        skiprows=2,
        usecols=list(colunas_desejadas_etario.keys())
    ).rename(columns=colunas_desejadas_etario)
    
    df['year'] = ano
    return df

# Função para processar os subconjuntos (homens e mulheres)
def processar_subconjuntos_etario(df):
    return {
        faixa: df.iloc[inicio:fim].assign(sex=sexo)
        for faixa, (inicio, fim), sexo in zip(faixas_etario.keys(), faixas_etario.values(), ['H', 'M'])
    }


# Tabela 3: Instrução

# Definição das colunas e faixas etárias
colunas_desejadas_instrucao = {
    "Características selecionadas": "degree",
    "População na força de trabalho\n(1 000 pessoas)": "work_pop"
}

faixas_instrucao = {
    "homens": (58, 62),  # Homens: linhas 58 a 62
    "mulheres": (64, 68) # Mulheres: linhas 64 a 68
}

# Lista com os anos disponíveis
anos = ["2018", "2019", "2020", "2021", "2022", "2023"]

# Função para carregar os dados de instrução
def carregar_instrucao(ano):

    df = pd.read_excel(
        "Tabelas/tabela_1_1_Indic_BR.xls",
        sheet_name=ano,
        skiprows=2,
        usecols=list(colunas_desejadas_instrucao.keys())
    ).rename(columns=colunas_desejadas_instrucao)
    
    df['year'] = ano
    return df

# Função para processar os subconjuntos (homens e mulheres)
def processar_subconjuntos_instrucao(df):
    return {
        faixa: df.iloc[inicio:fim].assign(sex=sexo)
        for faixa, (inicio, fim), sexo in zip(faixas_instrucao.keys(), faixas_instrucao.values(), ['H', 'M'])
    }


# Tabela 4 e 5: Salário

def carregar_socio():
    colunas_desejadas_BR = {"Grandes Regiões, sexo e cor ou raça": "BR"}

    colunas_desejadas_INST = {
        "Sem instrução ou fundamental incompleto": "incomplete",
        "Ensino fundamental completo ou médio incompleto": "elementary",
        "Ensino médio completo ou superior incompleto": "high",
        "Ensino superior completo": "college"
    }

    colunas_desejadas_IDADE_BR = {"Grandes Regiões, Unidades da Federação e Municípios das Capitais": "BR"}
    colunas_desejadas_IDADE = ["14 a 29 anos", "30 a 49 anos", "50 a 59 anos", "60 anos ou mais"]

    anos = ["2018", "2019", "2020", "2021", "2022", "2023"]

    # Criando o DataFrame inst_sal
    inst_sal = pd.concat(
        [
            pd.read_excel(
                "Tabelas/tabela_1_17_InstrCaract_Rend.xls",
                sheet_name=ano,
                skiprows=3,
                usecols=colunas_desejadas_BR
            ).rename(columns=colunas_desejadas_BR)
            .iloc[[4]]
            .reset_index(drop=True)
            .assign(year=ano)
            
            .join(
                pd.read_excel(
                    "Tabelas/tabela_1_17_InstrCaract_Rend.xls",
                    sheet_name=ano,
                    skiprows=5,
                ).drop(columns=["Unnamed: 0", "Unnamed: 1"])
                .drop([0,1])
                .iloc[[0]]
                .reset_index(drop=True)
                .rename(columns=colunas_desejadas_INST)
            )
            
            for ano in anos
        ], axis=0
    ).reset_index(drop=True)

    # Criando o DataFrame idade_sal
    idade_sal = pd.concat(
        [
            pd.read_excel(
                "Tabelas/tabela_1_15_OcupCaract_Geo_Rend.xls",
                sheet_name=ano,
                skiprows=2,
                usecols=list(colunas_desejadas_IDADE_BR.keys())
            ).rename(columns=colunas_desejadas_IDADE_BR)
            .iloc[[3]]
            .reset_index(drop=True)
            .assign(year=ano)
            
            .join(
                pd.read_excel(
                    "Tabelas/tabela_1_15_OcupCaract_Geo_Rend.xls",
                    sheet_name=ano,
                    skiprows=4,
                    usecols=colunas_desejadas_IDADE
                ).iloc[[1]]
                .reset_index(drop=True)
            )
            
            for ano in anos
        ], axis=0
    ).reset_index(drop=True)

    # Criando o DataFrame idade_inst_sal (junção de inst_sal e idade_sal)
    idade_inst_sal = pd.merge(inst_sal, idade_sal, on=["BR", "year"], how="inner")

    return idade_inst_sal
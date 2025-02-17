import os
import pandas as pd
from sqlalchemy import create_engine, text, Integer, String, Column
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Defina as credenciais do MySQL
user = "root"
password = "admin"
host = "0.0.0.0"  # ou IP do servidor
database_name = "projecoes2_banco"

# Arquivos CSV para cada tabela
csv_path = "/home/polia/repos/tarefa2/etapa1_etl/csv_temp"
csv_projecoes = csv_path + '/projecoes.csv'
csv_etario = csv_path + '/faixa_etario.csv'
csv_socio = csv_path + '/faixa_socio.csv'
csv_salar = csv_path + '/idade_inst_sal.csv'

# Crie a engine de conexão sem especificar um banco de dados
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database_name}")

# Crie a base para definir as tabelas
Base = declarative_base()

# Criar o banco de dados se não existir
try:
    with engine.connect() as connection:
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {database_name};"))
        print(f"Banco de dados '{database_name}' verificado/criado com sucesso!")
except SQLAlchemyError as e:
    print(f"Erro ao criar o banco de dados: {e}")


# TABELA 1 - PROJECOES

# Definir a tabela `projecoes2_table`
class Projecao(Base):
    __tablename__ = "projecoes2_table"
    __table_args__ = {'extend_existing': True} # re-defina a tabela, caso ela já tenha sido criada anteriormente.

    year = Column(Integer, primary_key=True)  # Definindo a chave primária
    local = Column(String(50))
    pop_h = Column(Integer)
    pop_m = Column(Integer)
    e0_t = Column(Integer)
    e60_t = Column(Integer)

# Atualizar a engine para usar o banco de dados recém-criado
# engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database_name}")

# Criar a nova tabela no banco de dados
try:
    with engine.connect() as connection:
        # Verificar se o banco de dados existe e conectar
        connection.execute(text(f"USE {database_name};"))
        Base.metadata.create_all(engine)  # Criação da tabela
        print("Tabela 'projecoes2_table' criada com sucesso!")
except SQLAlchemyError as e:
    print(f"Erro ao criar a tabela: {e}")

# Ler o arquivo CSV para um DataFrame
try:
    projecoes2_df_filtrado = pd.read_csv(csv_projecoes)
    print(f"Arquivo '{csv_projecoes}' carregado com sucesso!")
except FileNotFoundError:
    print(f"Erro: Arquivo '{csv_projecoes}' não encontrado!")
    exit(1)

# Inserir os dados do DataFrame na tabela MySQL
try:
    projecoes2_df_filtrado.to_sql("projecoes2_table", con=engine, if_exists="replace", index=False)
    print("Dados inseridos com sucesso na tabela 'projecoes2_table'!")
except SQLAlchemyError as e:
    print(f"Erro ao inserir os dados: {e}")
    
    
    
# TABELA 2 - FAIXA DE IDADE
    
# Definir a tabela `etario_table`
class Etario(Base):
    __tablename__ = "etario_table"
    __table_args__ = {'extend_existing': True} # re-defina a tabela, caso ela já tenha sido criada anteriormente.

    id = Column(Integer, primary_key=True, autoincrement=True)  # Chave primária auto-incrementada
    year = Column(Integer)
    sex = Column(String(1))  # 'H' para homens, 'M' para mulheres
    features = Column(String(50))
    work_pop = Column(Integer)

# Atualizar a engine para usar o banco de dados recém-criado
# engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database_name}")

# Criar a nova tabela no banco de dados
try:
    with engine.connect() as connection:
        # Verificar se o banco de dados existe e conectar
        connection.execute(text(f"USE {database_name};"))
        Base.metadata.create_all(engine)  # Criação da tabela
        print("Tabela 'etario_table' criada com sucesso!")
except SQLAlchemyError as e:
    print(f"Erro ao criar a tabela: {e}")

# Ler o arquivo CSV para um DataFrame
try:
    etario_filtrado = pd.read_csv(csv_etario)
    print(f"Arquivo '{csv_etario}' carregado com sucesso!")
except FileNotFoundError:
    print(f"Erro: Arquivo '{csv_etario}' não encontrado!")
    exit(1)

# Inserir os dados do DataFrame na tabela MySQL
try:
    etario_filtrado.to_sql("etario_table", con=engine, if_exists="replace", index=False)
    print("Dados inseridos com sucesso na tabela 'etario_table'!")
except SQLAlchemyError as e:
    print(f"Erro ao inserir os dados: {e}")
    
    
    
# TABELA 3 - FAIXA DE INSTRUÇÃO (SOCIO)

# Definir a tabela `socio_table`
class Socio(Base):
    __tablename__ = "socio_table"
    __table_args__ = {'extend_existing': True} # re-defina a tabela, caso ela já tenha sido criada anteriormente.

    id = Column(Integer, primary_key=True, autoincrement=True)  # Chave primária auto-incrementada
    year = Column(Integer)
    sex = Column(String(1))  # 'H' para homens, 'M' para mulheres
    degree = Column(String(50))
    work_pop = Column(Integer)

# Atualizar a engine para usar o banco de dados recém-criado
# engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database_name}")

# Criar a nova tabela no banco de dados
try:
    with engine.connect() as connection:
        # Verificar se o banco de dados existe e conectar
        connection.execute(text(f"USE {database_name};"))
        Base.metadata.create_all(engine)  # Criação da tabela
        print("Tabela 'socio_table' criada com sucesso!")
except SQLAlchemyError as e:
    print(f"Erro ao criar a tabela: {e}")

# Ler o arquivo CSV para um DataFrame
try:
    socio_filtrado = pd.read_csv(csv_socio)
    print(f"Arquivo '{csv_socio}' carregado com sucesso!")
except FileNotFoundError:
    print(f"Erro: Arquivo '{csv_socio}' não encontrado!")
    exit(1)

# Inserir os dados do DataFrame na tabela MySQL
try:
    socio_filtrado.to_sql("socio_table", con=engine, if_exists="replace", index=False)
    print("Dados inseridos com sucesso na tabela 'socio_table'!")
except SQLAlchemyError as e:
    print(f"Erro ao inserir os dados: {e}")
    
    
    
# TABELA 4 - SALARIO (INSTRUÇÃO X IDADE)
    
# Definir a tabela `salario_table`
class Salario(Base):
    __tablename__ = "salario_table"
    __table_args__ = {'extend_existing': True} # re-defina a tabela, caso ela já tenha sido criada anteriormente.

    id = Column(Integer, primary_key=True, autoincrement=True)  # Chave primária auto-incrementada
    BR = Column(String(10))
    year = Column(Integer)
    incomplete = Column(Integer)
    elementary = Column(Integer)
    high = Column(Integer)
    college = Column(Integer)
    age_14_29 = Column(Integer)  # Faixa etária 14 a 29 anos
    age_30_49 = Column(Integer)  # Faixa etária 30 a 49 anos
    age_50_59 = Column(Integer)  # Faixa etária 50 a 59 anos
    age_60_plus = Column(Integer)  # Faixa etária 60 anos ou mais


# Atualizar a engine para usar o banco de dados recém-criado
# engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database_name}")

# Criar a nova tabela no banco de dados
try:
    with engine.connect() as connection:
        # Verificar se o banco de dados existe e conectar
        connection.execute(text(f"USE {database_name};"))
        Base.metadata.create_all(engine)  # Criação da tabela
        print("Tabela 'salario_table' criada com sucesso!")
except SQLAlchemyError as e:
    print(f"Erro ao criar a tabela: {e}")

# Ler o arquivo CSV para um DataFrame
try:
    idade_inst_sal = pd.read_csv(csv_salar)
    print(f"Arquivo '{csv_salar}' carregado com sucesso!")
except FileNotFoundError:
    print(f"Erro: Arquivo '{csv_salar}' não encontrado!")
    exit(1)

# Renomear as colunas do DataFrame para corresponder aos nomes esperados na tabela
idade_inst_sal_renomeado = idade_inst_sal.rename(columns={
    "14 a 29 anos": "age_14_29",
    "30 a 49 anos": "age_30_49",
    "50 a 59 anos": "age_50_59",
    "60 anos ou mais": "age_60_plus"
})

# Inserir os dados do DataFrame na tabela MySQL
try:
    idade_inst_sal_renomeado.to_sql("salario_table", con=engine, if_exists="replace", index=False)
    print("Dados inseridos com sucesso na tabela 'salario_table'!")
except SQLAlchemyError as e:
    print(f"Erro ao inserir os dados: {e}")
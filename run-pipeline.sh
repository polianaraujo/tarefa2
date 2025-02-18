#!/bin/bash

python3 ./etapa1_etl/transform.py

python3 ./etapa1_etl/load.py 

# Caminho do diretório onde o script está
PROJECT_DIR="$(dirname "$(realpath "$0")")/project2_dbt/"

echo "Iniciando DBT Debug..."
dbt debug --project-dir "$PROJECT_DIR"

if [ $? -ne 0 ]; then
    echo "Erro ao rodar 'dbt debug'. Saindo..."
    exit 1
fi

echo "DBT Debug finalizado com sucesso!"

echo "Compilando os modelos..."
dbt compile --project-dir "$PROJECT_DIR"

if [ $? -ne 0 ]; then
    echo "Erro ao rodar 'dbt compile'. Saindo..."
    exit 1
fi

echo "DBT Compile finalizado com sucesso!"

echo "Executando os modelos..."
dbt run --project-dir "$PROJECT_DIR"

if [ $? -ne 0 ]; then
    echo "Erro ao rodar 'dbt run'. Saindo..."
    exit 1
fi

echo "DBT Run finalizado com sucesso!"
echo "Processo concluído!"

# Tarefa: Análise Salarial e Socioeconômica para Projeção de Alvos para Empresas

## Etapa 1 - Extração e Carregamento dos Dados

- **Escolha dos Dados**: Escolher um conjunto de dados que seja relevante para o candidato e que permita a aplicação de técnicas de análise de dados.
- **Extração**: Utilizar a linguagem de programação Python e bibliotecas como requests, pandas, sqlalchemy para extrair os dados da fonte escolhida.
- **Transformação**: Limpar e transformar os dados para garantir a qualidade e consistência.
- **Carregamento**: Carregar os dados transformados em um banco de dados relacional (PostgreSQL, MySQL, etc.), utilizando o SQLAlchemy para a conexão e inserção dos dados.

projecoes2_df_filtrado

etario_filtrado

socio_filtrado

idade_inst_sal = merge(inst_sal,idade_sal)

Docker, MySQL, SQLAlchemy.

- Docker:
docker run --name db-lodaq -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:8.3

DBeaver para visualização do banco de dados, tabelas e views.

### Carregamento do banco de dados 
Definido como  ```projecoes2_banco```

``` python
# Defina as credenciais do MySQL
user = "root"                       # Usuário
password = "admin"                  # Senha
host = "0.0.0.0"                    # Número de host
database_name = "projecoes2_banco"  # Nome do banco de dados
```
Tabela criadas:

"projecoes2_table", "etario_table", "socio_table", "salario_table"



## Etapa 2 - Modelagem dos Dados com DBT
- **Criação do Projeto**: Criar um projeto DBT e conectar ao banco de dados criado na etapa anterior.
- **Modelagem**: Criar modelos DBT para transformar os dados brutos em um modelo dimensional, com tabelas ou views.
- **Cálculos**: Realizar cálculos de agregação, criar views e tabelas intermediárias para preparar os dados para a geração de relatórios.
- **Documentação**: Documentar os modelos DBT utilizando a linguagem YAML, explicando a lógica de cada modelo.

Nesta etapa, foi utilizado o DBT para criar um projeto e conectá-lo ao banco de dados gerado na etapa anterior (```projecoes2_banco```). Foram então criados **quatro modelos** para transformar os dados em um modelo dimensional, portanto, quatro tabelas e quatro views, que puderam ser acompanhadas através do DBeaver.

![DBeaver](/home/polia/repos/tarefa2/images/dbeaver_png.png)



## Etapa 3: Criação de um Relatório ou Dashboard (Opcional)

- **Escolha da Ferramenta**: Utilizar uma ferramenta de BI (Business Intelligence) como Tableau, Power BI ou uma biblioteca de visualização em Python (matplotlib, seaborn) para criar um relatório ou dashboard.
- **Visualização**: Criar visualizações que respondam a perguntas de negócio relevantes e que permitam uma fácil interpretação dos dados.

Esta etapa foi realizada no notebook Jupyter denominado ```notebook.ipynb```.

...

### GRÁFICO 1: Projeção da População até 2045

![Projeções](/home/polia/repos/tarefa2/images/projecoes.png)

Por quê até 2045? Dar o exemplo de quem tem 60 anos em 2024...


### GRÁFICOS 2: Força de Trabalho por Perfil Etário e Grau de Instrução

![Força de Trabalho](/home/polia/repos/tarefa2/images/forca_trab.png)


### GRÁFICOS 3: Força de Trabalho por Perfil Etário e Grau de Instrução

![Salário (Idade x Instrução)](/home/polia/repos/tarefa2/images/salario.png)
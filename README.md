# Tarefa: Análise Socioeconômica para Projeção de Alvos para Empresas

Para que as empresas possam direcionar seus investimentos e estratégias de mercado com maior precisão, é essencial entender qual público possui maior poder aquisitivo e seu nível de instrução. Para responder a essa questão, utilizamos dados disponibilizados pelo IBGE, organizados em quatro tabelas principais.


## Etapa 1 - Extração e Carregamento dos Dados

A primeira coisa a ser feita é o processo de coleta e extração, transformação e armazenamento dos dados necessários em um banco de dados relacional, tudo isso presente nos arquivos ```extract.py``` e ```transform.py``` presentes na pasta ```etapa1_etl``` e são executadas no script `run-pipeline.sh` no diretório raiz.

- `extract.py`: Responsável por extrair os dados dos arquivos `.xls`.
- `transform.py`: Processa e organiza os dados em dataframes.
- `run-pipeline.sh`: Executa a pipeline de ETL.

Utilizando Python, foi feita a leitura dos arquivos em tabelas no formato ```.xls```, foram organizados e transformados em dataframes.

Os dados utilizados são provenientes de quatro tabelas do IBGE, essenciais para a análise:

- ```projecoes2_df_filtrado```: Contém projeções populacionais ao longo dos anos.
- ```etario_filtrado```: Apresenta a quantidade de pessoas aptas a trabalhar pela distribuição etária da população.
- ```socio_filtrado```: quantidade de pessoas aptas a trabalhar por grau de instrução da população.
- ```idade_inst_sal```: Merge entre dados de nível de instrução e salários, permitindo análises cruzadas entre idade, educação e rendimento.

O próximo passo foi carregar esses dados em um banco de dados relacional, facilitando consultas eficientes. Utilizado o MySQL, rodando em um container Docker, garantindo um ambiente controlado e escalável.

O banco de dados foi definido como ```projecoes2_banco```, e a conexão foi configurada com os seguintes parâmetros:

Definido como  ```projecoes2_banco```

``` python
# Defina as credenciais do MySQL
user = "root"                       # Usuário
password = "admin"                  # Senha
host = "0.0.0.0"                    # Número de host
database_name = "projecoes2_banco"  # Nome do banco de dados
```
As tabelas criadas dentro do banco incluem:

- ```projecoes2_table``` – Para as projeções populacionais.
- ```etario_table``` – Dados da população apta a trabalhar sobre faixas etárias.
- ```socio_table``` – Dados da população apta a trabalhar sobre grau de instrução.
- ```salario_table``` – Armazena dados de rendimento por faixa etária e grau de instrução.

Para garantir um ambiente seguro e eficiente, além de permitir que o banco de dados seja facilmente gerenciado e acessado de qualquer máquina configurada para utilizar Docker, o MySQL foi executado dentro de um container Docker com o seguinte comando:
```docker run --name db-lodaq -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:8.3```




## Etapa 2 - Modelagem dos Dados com DBT

Nesta etapa, foi utilizado o DBT para criar um projeto e conectá-lo ao banco de dados gerado na etapa anterior (`projecoes2_banco`). Foram então criados **quatro modelos** para transformar os dados em um modelo dimensional, portanto, quatro tabelas e quatro views, que puderam ser acompanhadas através do DBeaver.

![DBeaver](https://github.com/polianaraujo/tarefa2/blob/main/images/dbeaver_png.png)

Além disso, para facilitar a visualização dos dados e a criação de consultas SQL, foi utilizado o DBeaver, uma ferramenta gráfica que possibilita a inspeção e manipulação das tabelas e views armazenadas no banco de dados.

Com os quatro modelos prontos, foram realizados cálculos essenciais para análises estatísticas e projeções que garantem que os dados estejam preparados para a geração de relatórios estratégicos, como:

- Soma da população de homens e mulheres para visualizar a quantidade total.
- Soma da população apta a trabalhar por ano em diferentes faixas etárias e de grau de instrução.

Os comandos necessários para rodar os modelos DBT estão presentes no script `run-pipeline.sh` no diretório raiz. Os seguintes:

```python
dbt debug   # Verifica se o banco de dados está acessível, as credenciais de autenticação e se o ambiente está configurado corretamente.
dbt compile # Converte os arquivos .sql que contêm código dbt (com macros, variáveis e Jinja) em SQL puro, pronto para ser executado no banco de dados.
dbt run     # Roda os arquivos .sql transformados dentro do banco, cria ou atualiza tabelas e views e aplica as transformações.
```

Ao fim desta etapa, toda a modelagem foi documentada presente em `schema.yml`, no diretório `project2_dbt/models`. Cada modelo foi descrito com informações sobre sua lógica de transformação e origem dos dados.



## Etapa 3: Criação de um Relatório ou Dashboard (Opcional)

Esta etapa foi realizada no notebook Jupyter denominado ```graphics.ipynb``` e as bibliotecas `sqlalchemy` para fazer a conexão com o banco de dados e a matplotilib.pyplot para plotar os gráficos para visualização das análises.

Com isso podemos tirar algumas conclusões analisando os gráficos gerados.

### GRÁFICO 1: Projeção da População até 2045

![Projeções](https://github.com/polianaraujo/tarefa2/blob/main/images/projecoes.png)

A primeira tabela analisada foi a da quantidade da população brasileira ao longo dos anos, com um projeção até 2045. Com o gráfico gerado através dela é possível observar que em 2024 a expectativa média de vida é de até aproximadamente 77 anos, enquanto quem tem mais de 60 anos em 2024 possuem uma expectativa adicional de 23 anos.

Então, quem tem mais de 60 anos em 2024, tem grandes chances de viver até 2048. Quem tem 40 anos hoje, terá 60 anos em 2045 possuindo uma expectativa de vida perto dos 81, mas em 2045, quem tem +60 anos tem grandes chances de viver +25, ou seja, até os 85 anos.

Com isso, é possível perceber que a expectativa de vida só tende a aumentar, devido aos grandes avanços da tecnologia e medicina. Com isso, a população tende a se tornar cada vez mais velha, e com isso mais a necessidade da população irá mudar, e o mercado precisará está atento em atendê-las.


A primeira análise focou na evolução da população brasileira ao longo dos anos, com projeções até 2045.

Os dados mostram que:

- Em 2024, a **expectativa média de vida** é de aproximadamente **77 anos**.
- Para indivíduos com **mais de 60 anos em 2024**, a **expectativa de vida adicional é de +23 anos**, indicando grandes chances de **viver até 2048**.
- Quem tem **40 anos hoje** (2024) chegará aos 60 anos **em 2045, com uma expectativa de vida de 81 anos.** Além, de uma expectativa adicional (para os que possuem +60 em 2045) de **+25 anos**, ou seja, podem viver até 85 anos.

🔍 Conclusão: A expectativa de vida vem aumentando continuamente devido aos avanços da tecnologia e da medicina. Isso indica uma mudança no perfil demográfico da população, que tende a envelhecer cada vez mais. Como consequência, as demandas e necessidades da sociedade se transformarão, impactando o mercado e criando novas oportunidades de negócios.



### GRÁFICOS 2: Força de Trabalho por Perfil Etário e Grau de Instrução

![Força de Trabalho](https://github.com/polianaraujo/tarefa2/blob/main/images/forca_trab.png)

Embora não existam projeções específicas sobre a população economicamente ativa no futuro, analisamos os dados da força de trabalho entre 2018 e 2024.

Os principais pontos observados:

- Nos últimos seis anos, a **maior parte** das pessoas **aptas a trabalhar** está na faixa etária de **30 a 49 anos**.
- Quanto ao grau de instrução, a maior parte da força de trabalho tem **ensino médio completo ou superior incompleto**.
- O número de pessoas com **ensino superior completo vem crescendo** gradativamente, enquanto a população **sem instrução formal está diminuindo**.

🔍 Conclusão: A tendência de aumento da escolaridade reforça a necessidade de investimentos em qualificação profissional e inovação no mercado de trabalho. Empresas que oferecem soluções voltadas para educação continuada, cursos técnicos e qualificação de mão de obra podem se beneficiar desse cenário.


### GRÁFICOS 3: Força de Trabalho por Perfil Etário e Grau de Instrução

![Salário (Idade x Instrução)](https://github.com/polianaraujo/tarefa2/blob/main/images/salario.png)

Quanto aos rendimentos, observa-se valores maiores relacionados às faixas etárias de 50 anos + e para as pessoas que completaram o ensino superior.

### Conclusões Gerais

Assim, diante do aumento da idade média dos brasileiros e do percentual destes com qualificação, podemos inferir que na janela de crescimento demográfico, i.e., nos próximos 20 anos, até 2045,  teremos um aumento deste público que demandará cada vez mais produtos e serviços especializados para este público, que é naturalmente mais exigente e financeiramente mais abastado.
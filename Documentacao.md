# Documentação da API Random

## Introdução

A API Random é um projeto que extrai dados aleatórios da API Random User e os insere em um banco de dados SQL Server. Esta documentação fornece informações detalhadas sobre o funcionamento da API Random, incluindo requisitos, instalação, configuração e uso.

## Requisitos

Para executar a API Random, você precisará dos seguintes requisitos:

- Python 3.x
- Bibliotecas: Pandas, Requests, PyODBC
- SQL Server

## Instalação

1. Clone o repositório da API Random:

```shell
git clone https://github.com/SR-Dionizio/API_Random.git
```

2. Instale as bibliotecas necessárias:

```shell
pip install pandas requests pyodbc
```

## Configuração

1. Abra o arquivo `api_random.py` no diretório do projeto.
2. Na seção de configuração, você encontrará o código para a conexão com o banco de dados SQL Server.
3. Verifique o driver do ODBC adequado para a sua instalação do SQL Server.
4. Edite a linha `conn = pyodbc.connect('Driver={SQL Server};Server=SEU_SERVER;Database=Clientes;Trusted_Connection=yes;')` com as informações corretas do seu servidor SQL.

## Uso

1. Execute o arquivo `api_random.py` para iniciar o processo de extração e inserção dos dados na API Random.
2. O script extrairá dados aleatórios da API Random User e os armazenará em um DataFrame do Pandas.
3. Em seguida, o script se conectará ao banco de dados SQL Server usando a biblioteca PyODBC.
4. Para cada linha do DataFrame, o script verificará se o CPF já existe no banco de dados.
5. Se o CPF já existir, os dados serão atualizados no banco de dados.
6. Caso contrário, uma nova linha será inserida com os dados da API.
7. Ao finalizar a inserção/atualização dos dados, a conexão com o banco de dados será fechada.

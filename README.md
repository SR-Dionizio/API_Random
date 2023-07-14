```markdown
# API Random

Este é um projeto que extrai dados aleatórios de uma API e os insere em um banco de dados SQL Server.

## Pré-requisitos

- Python 3.x
- Pandas
- Requests
- PyODBC
- SQL Server

## Instalação

1. Clone o repositório:

```shell
git clone https://github.com/SR-Dionizio/api-random.git
```

2. Instale as dependências:

```shell
pip install pandas requests pyodbc
```

## Uso

1. Configure a conexão com o banco de dados SQL Server no arquivo `api_random.py`:
   - Verifique o driver do ODBC adequado para a sua instalação do SQL Server.
   - Edite a linha `conn = pyodbc.connect('Driver={SQL Server};Server=SEU_SERVER;Database=Clientes;Trusted_Connection=yes;')` com as informações corretas.

2. Execute o arquivo `api_random.py`:

```shell
python api_random.py
```

Isso irá extrair os dados aleatórios da API e inseri-los/atualizá-los no banco de dados.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request

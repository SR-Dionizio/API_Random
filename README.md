# Random User API - Extração e Inserção de Dados em Banco de Dados

Este é um projeto simples que utiliza a API Random User para extrair dados de usuários aleatórios e inseri-los em um banco de dados SQL Server.

## Descrição

O objetivo deste projeto é demonstrar como extrair dados da API Random User e inseri-los em um banco de dados utilizando a biblioteca pandas para manipulação de dados e a biblioteca pyodbc para a conexão com o banco de dados SQL Server.

O projeto é dividido em duas funções principais:

1. **api_random():** Esta função faz uma requisição para a API Random User e extrai os dados necessários. Em seguida, os dados são armazenados em um DataFrame do pandas.

2. **insert_db():** Esta função estabelece uma conexão com o banco de dados SQL Server e insere os dados do DataFrame na tabela "Clientes". É utilizado um cursor para executar as consultas SQL.

## Requisitos

Antes de executar o código, certifique-se de ter as seguintes bibliotecas instaladas:

- pandas
- requests
- pyodbc

Além disso, é necessário ter um servidor SQL Server disponível e criar um banco de dados chamado "Clientes" com uma tabela vazia chamada "Clientes". Certifique-se de configurar corretamente a conexão com o banco de dados no código.

## Como executar

1. Clone o repositório para o seu ambiente local.

2. Certifique-se de ter os requisitos mencionados acima instalados.

3. Execute o arquivo "api_random.py" em um ambiente Python.

4. Os dados serão extraídos da API Random User e inseridos no banco de dados.

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma sugestão ou melhoria para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

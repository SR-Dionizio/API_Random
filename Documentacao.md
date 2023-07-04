# Documentação para o Código

O código fornecido é um script Python que extrai dados da API Random User e os insere em um banco de dados SQL Server usando pyodbc.

## Explicação do Código

O código consiste em duas funções: `api_random()` e `insert_db()`. Aqui está uma explicação de cada função:

### `api_random()`

Esta função realiza as seguintes etapas:

1. Importa as bibliotecas necessárias: `pandas`, `requests` e `pyodbc`.
2. Define um DataFrame vazio chamado `dados` para armazenar os dados extraídos.
3. Define uma variável `contador` para acompanhar o número da linha no DataFrame.
4. Constrói a URL da API para solicitar dados de 500 usuários brasileiros.
5. Envia uma solicitação GET para a URL da API e recupera a resposta.
6. Analisa os dados JSON da resposta.
7. Itera sobre cada usuário na resposta e extrai informações relevantes, como CPF, gênero, nome, endereço, e-mail, etc.
8. Adiciona os dados extraídos ao DataFrame `dados`.
9. Imprime uma mensagem de sucesso após extrair os dados.

### `insert_db()`

Esta função realiza as seguintes etapas:

1. Importa as bibliotecas necessárias: `pandas` e `pyodbc`.
2. Estabelece uma conexão com o banco de dados SQL Server usando a biblioteca `pyodbc`.
3. Cria um objeto de cursor para executar consultas SQL.
4. Itera sobre cada linha do DataFrame `dados`.
5. Constrói uma consulta SQL de inserção para cada linha de dados e a executa usando o cursor.
6. Confirma as alterações no banco de dados.
7. Fecha a conexão com o banco de dados.
8. Imprime uma mensagem de sucesso após inserir os dados.

### Execução Principal

A seção de execução principal do código chama a função `api_random()` para extrair dados da API e armazená-los no DataFrame `dados`. Em seguida, chama a função `insert_db()` para inserir os dados extraídos no banco de dados SQL Server.

## Dependências

O código requer as seguintes dependências:

- pandas: Usado para criar e manipular DataFrames.
- requests: Usado para enviar solicitações HTTP para a API e recuperar a resposta.
- pyodbc: Usado para estabelecer uma conexão com o banco de dados SQL Server e executar consultas SQL.

Certifique-se de que essas bibliotecas estejam instaladas antes de executar o código.

## Uso

Para usar o código:

1. Certifique-se de que as dependências necessárias estejam instaladas.
2. Configure um banco de dados SQL Server com uma tabela chamada `Clientes` que corresponda às colunas especificadas no código.
3. Modifique a string de conexão na função `insert_db()` para corresponder à configuração do seu banco de dados.
4. Execute o código e ele extrairá dados da API e os inserirá no banco de dados.
5. O código imprimirá mensagens indicando o progresso e o sucesso dos processos de extração e inserção.

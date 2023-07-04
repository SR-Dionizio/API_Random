import pandas as pd
import requests
import pyodbc

#Função que extrai os dados necessários da API
def api_random():

    print('Iniciando a extração de dados')
    #Definindo o dataframe como global para usar em outras funções
    global dados
    #Criando as colunas do dataframe
    dados = pd.DataFrame(columns=["CPF",
                                "Genero",
                                "Nome",
                                "Endereço",
                                "Numero_casa",
                                "Cidade",
                                "Estado",
                                "País",
                                "Cep",
                                "email",
                                "Nascimento",
                                "Idade",
                                "Telefone"])

    #Variável para pegar o número da linha do dataframe
    contador = 0

    #End point da API
    url = f"https://randomuser.me/api/1.4/?nat=br&results=500"
    #Fazendo a requisição da API
    response = requests.get(url)
    #Definindo o arquivo de resposta da API
    data = response.json()

    #Looping Para escrever os dados no dataframe
    for result in data["results"]:
        contador += 1
        Cpf = result["id"]["value"]
        Genero = result["gender"]
        Nome = result["name"]["first"]
        Endereco = result["location"]["street"]["name"]
        Numero_endereco = result["location"]["street"]["number"]
        Cidade = result["location"]["city"]
        Estado = result["location"]["state"]
        Pais = result["location"]["country"]
        Cep = result["location"]["postcode"]
        Email = result["email"]
        Nascimento = result["dob"]["date"]
        Idade = result["dob"]["age"]
        Telefone = result["phone"]

        dados.loc[contador] = [Cpf,
                                Genero,
                                Nome, 
                                Endereco, 
                                Numero_endereco, 
                                Cidade.replace("'",""),
                                Estado,
                                Pais,
                                Cep,
                                Email,
                                Nascimento,
                                Idade,
                                Telefone]

    print('Dados extraídos com sucesso')

#Função que insere os dados da API em um banco de dados
def insert_db():

    print("Iniciando a inserção dos dados no banco")
    # Estabelecendo a conexão com o banco de dados
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DANIEL;'
                        'Database=Clientes;'
                        'Trusted_Connection=yes;')

    # Criando um cursor para executar consultas SQL
    cursor = conn.cursor()

    # Inserindo os dados do DataFrame na tabela do banco de dados
    for row in dados.itertuples(index=False):
        values = ','.join([f"'{str(value)}'" for value in row])
        insert_query = f"INSERT INTO Clientes VALUES ({values});"
        cursor.execute(insert_query)
        conn.commit()
        
    # Fechando a conexão com o banco de dados
    conn.close()
    print("Dados inseridos no banco com sucesso")


api_random()
insert_db()
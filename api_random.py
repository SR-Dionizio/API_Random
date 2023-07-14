import pandas as pd
import requests
import pyodbc

class RandomAPIData:
    def __init__(self):
        self.dados = pd.DataFrame(columns=["CPF", "Genero", "Nome", "Endereço", "Numero_casa", "Cidade", "Estado", "País", "Cep", "email", "Nascimento", "Idade", "Telefone"])

    def extract_data(self):
        print('Iniciando a extração de dados')
        url = "https://randomuser.me/api/1.4/?nat=br&results=500"
        response = requests.get(url)
        data = response.json()
        contador = 0

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

            self.dados.loc[contador] = [Cpf, Genero, Nome, Endereco, Numero_endereco, Cidade.replace("'", ""), Estado, Pais, Cep, Email, Nascimento, Idade, Telefone]

        print('Dados extraídos com sucesso')

    def insert_db(self):
        print("Iniciando a inserção/atualização dos dados no banco")
        conn = pyodbc.connect('Driver={SQL Server};Server=DANIEL;Database=Clientes;Trusted_Connection=yes;')
        cursor = conn.cursor()

        for row in self.dados.itertuples(index=False):
            cpf = row[0]
            select_query = f"SELECT COUNT(*) FROM Clientes WHERE CPF='{cpf}'"
            cursor.execute(select_query)
            row_count = cursor.fetchone()[0]

            if row_count > 0:
                update_query = f"UPDATE Clientes SET Genero='{row[1]}', Nome='{row[2]}', Endereço='{row[3]}', Numero_casa='{row[4]}', Cidade='{row[5]}', Estado='{row[6]}', País='{row[7]}', Cep='{row[8]}', email='{row[9]}', Nascimento='{row[10]}', Idade='{row[11]}', Telefone='{row[12]}' WHERE CPF='{cpf}'"
                cursor.execute(update_query)
            else:
                values = ','.join([f"'{str(value)}'" for value in row])
                insert_query = f"INSERT INTO Clientes VALUES ({values});"
                cursor.execute(insert_query)

            conn.commit()

        conn.close()
        print("Dados inseridos/atualizados no banco com sucesso")

# Utilizando a classe RandomAPIData
api_data = RandomAPIData()
api_data.extract_data()
api_data.insert_db()

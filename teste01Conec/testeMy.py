#Importação de bibliotecas
import mysql.connector
from mysql.connector import Error
######################################################

# Função para a criação de conexão com o MySql
def criacao_conexao_banco(host, nome_usuario, senha):
    conexao= None
    try:
        conexao = mysql.connector.connect(
            host=host,
            user=nome_usuario,
            passwd=senha
        )
        print("MySQL Banco de dados conectado/selecionado com sucesso!\n")
    except Error as err:
        print(f"Error: Falha ao conectar/Selecionar com o banco de dados '{err}'\n")

    return conexao
########################################################
# Declarar o banco desejável
conexao = criacao_conexao_banco("localhost", "aluno", "sptech")
########################################################

########################################################

# Função que cria o banco de dados [Database]
def create_database(conexao, comando):
    cursor = conexao.cursor()
    try:
        cursor.execute(comando)
        print("Banco de dados criado com sucesso!\n")
    except Error as err:
        print(f"Erro: Falha ao criar o banco de dados [database] '{err}'\n")
########################################################

# Criação do seu Banco de dados
create_database_comando= "CREATE DATABASE nomeBanco"
create_database (conexao, create_database_comando)

########################################################

########################################################
# Para a conexão direta do programa
def conexao_direta(host, nomeUsuario, senha, nomeBanco):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=nomeUsuario,
            passwd=senha,
            database=nomeBanco
        )
        print("Conexão com banco funcionando de acordo!\n")
    except Error as err:
        print(f"Error: '{err}'\n")

    return connection
########################################################

########################################################
# Criação da conexão com banco direto [Database]
criacao_conexao_direta = conexao_direta("localhost", "aluno", "sptech", "school")
########################################################

########################################################
# Para a realização de comandos SQL
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Comando executado com sucesso!\n")
    except Error as err:
        print(f"Error: '{err}'")

########################################################
#                   EXEMPLO DE APLICAÇÃO
# Comandos do banco de dados para a criação das tabela exemplo

create_teacher_table = """
CREATE TABLE teacher (
  teacher_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  language_1 VARCHAR(3) NOT NULL,
  language_2 VARCHAR(3),
  dob DATE,
  tax_id INT UNIQUE,
  phone_no VARCHAR(20)
  );
 """
pop_teacher = """
INSERT INTO teacher VALUES
(1,  'James', 'Smith', 'ENG', NULL, '1985-04-20', 12345, '+491774553676'),
(2, 'Stefanie',  'Martin',  'FRA', NULL,  '1970-02-17', 23456, '+491234567890'), 
(3, 'Steve', 'Wang',  'MAN', 'ENG', '1990-11-12', 34567, '+447840921333'),
(4, 'Friederike',  'Müller-Rossi', 'DEU', 'ITA', '1987-07-07',  45678, '+492345678901'),
(5, 'Isobel', 'Ivanova', 'RUS', 'ENG', '1963-05-30',  56789, '+491772635467'),
(6, 'Niamh', 'Murphy', 'ENG', 'IRI', '1995-09-08',  67890, '+491231231232');
"""
 #                  PARA ADICIONAR A TABELA NO BANCO

conexao = conexao_direta("localhost", "aluno", "sptech", "school") # Para selecionar o banco de dados
execute_query(conexao, create_teacher_table) # executar o comando em SQL 
execute_query(conexao, pop_teacher)
########################################################

########################################################
#               PARA SELECT [VISUALIZAR]

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

########################################################
#                   EXEMPLO DE APLICAÇÃO
q1 = """
SELECT *
FROM teacher;
"""

conexao = conexao_direta("localhost", "aluno", "sptech", "school") # Para selecionar o banco de dados
results = read_query(conexao, q1)

for result in results: # Apesar que o results aparenda dar erro, ela funciona. CONFIA!
  print(result)
########################################################

########################################################
#                   PARA ATUALIZAR
update = """
UPDATE teacher
SET first_name = 'Julia' 
WHERE teacher_id = 1;
"""
conexao = conexao_direta("localhost", "aluno", "sptech", "school") # Para selecionar o banco de dados
execute_query(conexao, update)

########################################################

########################################################
#               PARA DELETAR
delete = """
DELETE FROM teacher WHERE teacher_id = 2
"""

########################################################

########################################################

for result in results: # Apesar que o results aparenda dar erro, ela funciona. CONFIA!
  print(result)
#Importação de bibliotecas
import mysql.connector
from mysql.connector import Error
import pandas as pd
######################################################

# Função para a criação de conexão com o MySql
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Banco de dados conectado/selecionado com sucesso!\n")
    except Error as err:
        print(f"Error: Falha ao conectar/Selecionar com o banco de dados '{err}'\n")

    return connection
########################################################

# Conexão do banco de dados [MySql]
connection = create_server_connection("localhost", "aluno", "sptech")

########################################################

# Função que cria o banco de dados [Database]
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Banco de dados criado com sucesso!\n")
    except Error as err:
        print(f"Erro: Falha ao criar o banco de dados [database] '{err}'\n")
########################################################

# Criação do seu Banco de dados
create_database_query = "CREATE DATABASE school"
create_database (connection, create_database_query)

########################################################
# Para a conexão direta do programa
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Conexão com banco funcionando de acordo!\n")
    except Error as err:
        print(f"Error: '{err}'\n")

    return connection
########################################################

# Criação da conexão com banco direto [Database]
create_connection_bd = create_db_connection("localhost", "aluno", "sptech", "school")

# Para a realização de consultadas e comandos
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Comando executado com sucesso!\n")
    except Error as err:
        print(f"Error: '{err}'")

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

create_client_table = """
CREATE TABLE client (
  client_id INT PRIMARY KEY,
  client_name VARCHAR(40) NOT NULL,
  address VARCHAR(60) NOT NULL,
  industry VARCHAR(20)
);
 """

create_participant_table = """
CREATE TABLE participant (
  participant_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  phone_no VARCHAR(20),
  client INT
);
"""

create_course_table = """
CREATE TABLE course (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(40) NOT NULL,
  language VARCHAR(3) NOT NULL,
  level VARCHAR(2),
  course_length_weeks INT,
  start_date DATE,
  in_school BOOLEAN,
  teacher INT,
  client INT
);
"""
alter_participant = """
ALTER TABLE participant
ADD FOREIGN KEY(client)
REFERENCES client(client_id)
ON DELETE SET NULL;
"""

alter_course = """
ALTER TABLE course
ADD FOREIGN KEY(teacher)
REFERENCES teacher(teacher_id)
ON DELETE SET NULL;
"""

alter_course_again = """
ALTER TABLE course
ADD FOREIGN KEY(client)
REFERENCES client(client_id)
ON DELETE SET NULL;
"""

create_takescourse_table = """
CREATE TABLE takes_course (
  participant_id INT,
  course_id INT,
  PRIMARY KEY(participant_id, course_id),
  FOREIGN KEY(participant_id) REFERENCES participant(participant_id) ON DELETE CASCADE,
  FOREIGN KEY(course_id) REFERENCES course(course_id) ON DELETE CASCADE
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
pop_client = """
INSERT INTO client VALUES
(101, 'Big Business Federation', '123 Falschungstraße, 10999 Berlin', 'NGO'),
(102, 'eCommerce GmbH', '27 Ersatz Allee, 10317 Berlin', 'Retail'),
(103, 'AutoMaker AG',  '20 Künstlichstraße, 10023 Berlin', 'Auto'),
(104, 'Banko Bank',  '12 Betrugstraße, 12345 Berlin', 'Banking'),
(105, 'WeMoveIt GmbH', '138 Arglistweg, 10065 Berlin', 'Logistics');
"""

pop_participant = """
INSERT INTO participant VALUES
(101, 'Marina', 'Berg','491635558182', 101),
(102, 'Andrea', 'Duerr', '49159555740', 101),
(103, 'Philipp', 'Probst',  '49155555692', 102),
(104, 'René',  'Brandt',  '4916355546',  102),
(105, 'Susanne', 'Shuster', '49155555779', 102),
(106, 'Christian', 'Schreiner', '49162555375', 101),
(107, 'Harry', 'Kim', '49177555633', 101),
(108, 'Jan', 'Nowak', '49151555824', 101),
(109, 'Pablo', 'Garcia',  '49162555176', 101),
(110, 'Melanie', 'Dreschler', '49151555527', 103),
(111, 'Dieter', 'Durr',  '49178555311', 103),
(112, 'Max', 'Mustermann', '49152555195', 104),
(113, 'Maxine', 'Mustermann', '49177555355', 104),
(114, 'Heiko', 'Fleischer', '49155555581', 105);
"""

pop_course = """
INSERT INTO course VALUES
(12, 'English for Logistics', 'ENG', 'A1', 10, '2020-02-01', TRUE,  1, 105),
(13, 'Beginner English', 'ENG', 'A2', 40, '2019-11-12',  FALSE, 6, 101),
(14, 'Intermediate English', 'ENG', 'B2', 40, '2019-11-12', FALSE, 6, 101),
(15, 'Advanced English', 'ENG', 'C1', 40, '2019-11-12', FALSE, 6, 101),
(16, 'Mandarin für Autoindustrie', 'MAN', 'B1', 15, '2020-01-15', TRUE, 3, 103),
(17, 'Français intermédiaire', 'FRA', 'B1',  18, '2020-04-03', FALSE, 2, 101),
(18, 'Deutsch für Anfänger', 'DEU', 'A2', 8, '2020-02-14', TRUE, 4, 102),
(19, 'Intermediate English', 'ENG', 'B2', 10, '2020-03-29', FALSE, 1, 104),
(20, 'Fortgeschrittenes Russisch', 'RUS', 'C1',  4, '2020-04-08',  FALSE, 5, 103);
"""

pop_takescourse = """
INSERT INTO takes_course VALUES
(101, 15),
(101, 17),
(102, 17),
(103, 18),
(104, 18),
(105, 18),
(106, 13),
(107, 13),
(108, 13),
(109, 14),
(109, 15),
(110, 16),
(110, 20),
(111, 16),
(114, 12),
(112, 19),
(113, 19);
"""
########################################################
# Para a execução dos dados acima
connection = create_db_connection("localhost", "aluno", "sptech", "school") # Para selecionar o banco de dados
execute_query(connection, create_teacher_table) # executar o comando em SQL 
execute_query(connection, create_client_table) # executar o comando em SQL
execute_query(connection, create_participant_table) # executar o comando em SQL
execute_query(connection, create_course_table) # executar o comando em SQL

execute_query(connection, alter_participant)
execute_query(connection, alter_course)
execute_query(connection, alter_course_again)

execute_query(connection, create_takescourse_table)

execute_query(connection, pop_teacher)
execute_query(connection, pop_client)
execute_query(connection, pop_participant)
execute_query(connection, pop_course)
execute_query(connection, pop_takescourse)
########################################################
# Para a visualização do banco 
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

q1 = """
SELECT *
FROM teacher;
"""

connection = create_db_connection("localhost", "aluno", "sptech", "school") # Para selecionar o banco de dados
results = read_query(connection, q1)

for result in results: # Apesar que o results aparenda dar erro, ela funciona. CONFIA!
  print(result)


q5 = """
SELECT course.course_id, course.course_name, course.language, client.client_name, client.address
FROM course
JOIN client
ON course.client = client.client_id
WHERE course.in_school = FALSE;
"""

connection = create_db_connection("localhost", "aluno", "sptech", "school") # Para selecionar o banco de dados
results = read_query(connection, q5)
from_db = []#Inicializa uma lista vazia 
# Percorrer os resultados e inseri-los à lista

for result in results: # Apesar que o results aparenda dar erro, ela funciona. CONFIA!
  # Retorna uma lista de tuplas
  result = list(result)
  from_db.append(result)

  #Adicionar essa lista ao pandas -  para visualização das tabelas
columns = ["course_id", "course_name", "language", "client_name", "address"]
df = pd.DataFrame(from_db, columns=columns)

display(df)

update = """
UPDATE client 
SET address = '23 Fingiertweg, 14534 Berlin' 
WHERE client_id = 101;
"""

connection = create_db_connection("localhost", "aluno", "sptech", "school") # Para selecionar o banco de dados
execute_query(connection, update)

delete_course = """
DELETE FROM course 
WHERE course_id = 20;
"""


connection = create_db_connection("localhost", "aluno", "sptech", "school") # Para selecionar o banco de dados
execute_query(connection, delete_course)

def execute_list_query(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

sql = '''
    INSERT INTO teacher (teacher_id, first_name, last_name, language_1, language_2, dob, tax_id, phone_no) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    
val = [
    (7, 'Hank', 'Dodson', 'ENG', None, '1991-12-23', 11111, '+491772345678'), 
    (8, 'Sue', 'Perkins', 'MAN', 'ENG', '1976-02-02', 22222, '+491443456432')
]

connection = create_db_connection("localhost", "aluno", "sptech", "school") # Para selecionar o banco de dados
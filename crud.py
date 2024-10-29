import mysql.connector


conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'locadora',
)


cursor = conexao.cursor()
cursor.close()
conexao.close()
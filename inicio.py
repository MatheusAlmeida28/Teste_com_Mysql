from pymysql import connect, cursors

connection = connect(
    host = "localhost",
    user = "root",
    password = "",
    port = 3306,
    db = "testedb",
    charset = "utf8mb4",
    cursorclass = cursors.DictCursor)

def criar_tabela():
    try:
        with connection.cursor() as cursor:
            cursor.execute("create table teste (nome varchar(50))")
        print("Tudo ok")
    except Exception as erro:
        print(f"Ocorreu um erro {erro}")

def adicionar_valores_tabela():
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO teste values ('Matheus')")
            print("Valor inserido com sucesso!")
    except Exception as erro:
        print(f"Ocorreu um erro {erro}")

def mostrar_valor_tabela():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM teste")
            resultado = cursor.fetchall()
            for lista in resultado:
                print(lista)
    except Exception as erro:
        print(f"Ocorreu um erro {erro}")

def atualizar_valor_tabela():
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE teste SET nome = 'Souza' WHERE nome = 'Matheus'")
            print("Atualização feita com sucesso!")
    except Exception as erro:
        print(f"Ocorreu um erro {erro}")

def remover_valor_tabela():
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM teste WHERE nome = 'Souza'")
            print("Remoção feita com sucesso!")
    except Exception as erro:
        print(f"Ocorreu um erro {erro}")

remover_valor_tabela()
connection.close()

import sqlite3

connection = sqlite3.connect('banco.db')

cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY,\
    nome text, estrelas real, diaria real, cidade text)"

insert_hoteis_default = "INSERT INTO hoteis VALUES ('copacabana', 'Copacabana Palace', 5.0, 1000.0, 'Rio de Janeio'),\
    ('gravata', 'Hotel Gravatá', 3.8, 400.0, 'Gravatá'),\
    ('noronha', 'Hotel de Noronha', 4.5, 300.25, 'Fernando de Noronha')"

cursor.execute(cria_tabela)
cursor.execute(insert_hoteis_default)

connection.commit()
connection.close()
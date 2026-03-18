import sqlite3

def criar_banco():
    conn = sqlite3.connect('consumo.db')
    cursor = conn.cursor()
    # Criando a tabela de histórico
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historico (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            distancia REAL, 
            consumo REAL,
            preco REAL,
            resultado REAL,
            data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def salvar_consulta(dist, cons, prec, res):
    conn = sqlite3.connect('consumo.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO historico (distancia, consumo, preco, resultado) VALUES (?, ?, ?, ?)', 
                   (dist, cons, prec, res))
    conn.commit()
    conn.close()

def listar_historico():
    conn = sqlite3.connect('consumo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT distancia, consumo, preco, resultado, data FROM historico ORDER BY data DESC LIMIT 10')
    dados = cursor.fetchall()
    conn.close()
    return dados
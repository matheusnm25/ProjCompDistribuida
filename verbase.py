import sqlite3

# Conecta ao banco
conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

# Executa a consulta
cursor.execute("SELECT * FROM produtos")
dados = cursor.fetchall()
# Exibe os dados
print("[Conteúdo da Tabela 'produtos']")
for linha in dados:
    print(linha)

conn.close()

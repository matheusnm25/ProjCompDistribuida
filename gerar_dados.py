import sqlite3
import random
from faker import Faker
from datetime import datetime
import os

fake = Faker('pt_BR')

# Função para criar conexão com o banco de dados
def criar_conexao(db_file):
    """Cria uma conexão com o banco de dados SQLite especificado por db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Conectado ao SQLite versão {sqlite3.sqlite_version}")
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conn

# Função para criar tabelas
def criar_tabela(conn, create_table_sql):
    """Cria uma tabela a partir da instrução SQL create_table_sql."""
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela: {e}")

# Definição das tabelas
sql_create_produtos_table = """
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    quantidade_estoque INTEGER NOT NULL
);
"""

sql_create_clientes_table = """
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);
"""

sql_create_pedidos_table = """
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    data_criacao TEXT NOT NULL,
    status TEXT NOT NULL,  -- Ex: 'pendente', 'pagamento_aprovado', 'em_separacao', 'nf_emitida', 'enviado', 'cancelado'
    valor_total REAL,
    FOREIGN KEY (cliente_id) REFERENCES clientes (id)
);
"""

sql_create_itens_pedido_table = """
CREATE TABLE IF NOT EXISTS itens_pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    preco_unitario REAL NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos (id),
    FOREIGN KEY (produto_id) REFERENCES produtos (id)
);
"""

sql_create_pagamentos_table = """
CREATE TABLE IF NOT EXISTS pagamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL UNIQUE,  -- Geralmente 1 pagamento por pedido
    data_processamento TEXT NOT NULL,
    status TEXT NOT NULL,  -- Ex: 'aprovado', 'rejeitado', 'pendente'
    metodo TEXT,
    FOREIGN KEY (pedido_id) REFERENCES pedidos (id)
);
"""

sql_create_notas_fiscais_table = """
CREATE TABLE IF NOT EXISTS notas_fiscais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL UNIQUE,
    numero TEXT NOT NULL UNIQUE,
    data_emissao TEXT NOT NULL,
    chave_acesso TEXT,
    FOREIGN KEY (pedido_id) REFERENCES pedidos (id)
);
"""

sql_create_envios_table = """
CREATE TABLE IF NOT EXISTS envios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL UNIQUE,
    nota_fiscal_id INTEGER NOT NULL UNIQUE,
    data_despacho TEXT,
    codigo_rastreamento TEXT,
    status TEXT NOT NULL,  -- Ex: 'aguardando_envio', 'enviado', 'entregue'
    FOREIGN KEY (pedido_id) REFERENCES pedidos (id),
    FOREIGN KEY (nota_fiscal_id) REFERENCES notas_fiscais (id)
);
"""

# Função para popular dados
def popular_dados(conn, num_clientes=100, num_produtos=50, num_pedidos=200):
    """Popula o banco de dados com dados sintéticos."""
    cursor = conn.cursor()

    print("Populando tabela clientes...")
    clientes_ids = []
    for i in range(num_clientes):
        nome = fake.name()
        email = f"cliente_{i}_{fake.user_name()}@exemplo.com"  # Garante unicidade
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
        clientes_ids.append(cursor.lastrowid)

    print("Populando tabela produtos...")
    produtos_ids = []
    for i in range(num_produtos):
        nome = f"Produto {fake.word().capitalize()} {random.choice(['Eletrônico', 'Vestuário', 'Livro', 'Alimento'])}"
        preco = round(random.uniform(10.5, 500.99), 2)
        estoque = random.randint(0, 100)
        cursor.execute("INSERT INTO produtos (id, nome, preco, quantidade_estoque) VALUES (?, ?, ?, ?)", (i + 1, nome, preco, estoque))
        produtos_ids.append(i + 1)

    print("Populando tabelas pedidos e itens_pedido...")
    pedido_ids_criados = []
    for i in range(num_pedidos):
        cliente_id = random.choice(clientes_ids)
        data_criacao = fake.date_time_between(start_date="-90d", end_date="now").isoformat()
        status_inicial = 'pendente'
        cursor.execute("INSERT INTO pedidos (cliente_id, data_criacao, status) VALUES (?, ?, ?)", (cliente_id, data_criacao, status_inicial))
        pedido_id = cursor.lastrowid
        pedido_ids_criados.append(pedido_id)

    conn.commit()
    print("População de dados concluída.")

# Função Principal
def main():
    database = "ecommerce.db"

    if os.path.exists(database):
        os.remove(database)
        print(f"Banco de dados '{database}' existente removido.")

    conn = criar_conexao(database)

    if conn is not None:
        print("Criando tabelas...")
        criar_tabela(conn, sql_create_clientes_table)
        criar_tabela(conn, sql_create_produtos_table)
        criar_tabela(conn, sql_create_pedidos_table)
        criar_tabela(conn, sql_create_itens_pedido_table)
        criar_tabela(conn, sql_create_pagamentos_table)
        criar_tabela(conn, sql_create_notas_fiscais_table)
        criar_tabela(conn, sql_create_envios_table)
        print("Tabelas criadas com sucesso.")

        popular_dados(conn, num_clientes=50, num_produtos=30, num_pedidos=100)

        conn.close()
        print(f"Conexão com '{database}' fechada.")
    else:
        print("Erro! Não foi possível criar a conexão com o banco de dados.")

if __name__ == '__main__':
    main()
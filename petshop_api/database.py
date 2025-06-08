import sqlite3
import os

# Caminho absoluto do banco de dados

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "../petshop.db")

# Conexão com o banco

db = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = db.cursor()

# Tabela de usuários

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)
""")

# Tabela de produtos

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    preco REAL NOT NULL,
    categoria TEXT
)
""")

# Tabela de pedidos

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    data TEXT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
)
""")

# Tabela de consultas veterinárias

cursor.execute("""
CREATE TABLE IF NOT EXISTS consultas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    data TEXT NOT NULL,
    horario TEXT NOT NULL,
    tipo TEXT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)
""")

# Tabela de banho e tosa

cursor.execute("""
CREATE TABLE IF NOT EXISTS banho_tosa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    data TEXT NOT NULL,
    horario TEXT NOT NULL,
    servico TEXT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)
""")

# Aplicar mudanças no banco

db.commit()
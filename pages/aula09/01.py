# --- Importar as bibliotecas necessárias ---
import streamlit as st
import sqlite3
import pandas as pd
import requests

# --- Titulo do site
st.title('Integração com banco de dados e APIs')

# --- Conexão com o banco de dados SQLite
conn = sqlite3.connect(':memory:')  # Usando um banco de dados em memória para testes
cursor = conn.cursor()

# --- Criar uma tabela e inserir dados de exemplo
cursor.execute(''' CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)''')

# --- Inserir dados de exemplo
cursor.execute("INSERT OR REPLACE INTO produtos (id, nome, preco) VALUES (1, 'Computador', 3500.0)")
cursor.execute("INSERT OR REPLACE INTO produtos (id, nome, preco) VALUES (2, 'Notebook', 5000.0)")
cursor.execute("INSERT OR REPLACE INTO produtos (id, nome, preco) VALUES (3, 'Tablet', 1500.0)")

# --- Commit das alterações
conn.commit()

# --- Consultar os dados da tabela
st.header('Produtos disponíveis')
cursor.execute("SELECT * FROM produtos")
produtos = cursor.fetchall()
st.dataframe(pd.DataFrame(produtos, columns=['ID', 'Nome', 'Preço']))

# --- Fechar a conexão com o banco de dados
conn.close()

# --- Exemplo de API (simulada)
st.header('Dados de API externa')

try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts?_limit=5')  # Requisição para uma API de exemplo
    response.raise_for_status()  # Verificar se a requisição foi bem-sucedida
    posts = response.json()
    st.dataframe(pd.DataFrame(posts))
except requests.exceptions.RequestException as e:
    st.error(f'Erro ao acessar a API: {e}')


from app import app, db
import sqlite3

def add_column():
    # Conectar ao banco de dados diretamente
    conn = sqlite3.connect('instance/site.db')
    cursor = conn.cursor()

    # Verificar se a tabela 'present' existe
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='present'")
    table_exists = cursor.fetchone()

    if table_exists:
        # Verificar se a coluna 'image_file' já existe
        cursor.execute("PRAGMA table_info(present)")
        columns = [column[1] for column in cursor.fetchall()]

        if 'image_file' not in columns:
            # Adicionar a nova coluna
            cursor.execute('ALTER TABLE present ADD COLUMN image_file VARCHAR(200) NOT NULL DEFAULT ""')

    # Salvar as alterações e fechar a conexão
    conn.commit()
    conn.close()

with app.app_context():
    add_column()

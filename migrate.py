from app import app, db
from flask_sqlalchemy import SQLAlchemy

def add_column():
    db = SQLAlchemy(app)

    # Verificar se a coluna 'image_file' já existe
    columns = db.engine.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'present' AND column_name = 'image_file'")
    column_exists = columns.fetchone()

    if not column_exists:
        # Adicionar a nova coluna
        db.engine.execute('ALTER TABLE present ADD COLUMN image_file VARCHAR(200) NOT NULL DEFAULT ""')

with app.app_context():
    add_column()
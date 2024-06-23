import os

class Config:
    # Use a variável de ambiente DATABASE_URL se estiver definida, caso contrário use o SQLite para desenvolvimento
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'app/static/uploads')
    MAX_CONTENT_PATH = 16 * 1024 * 1024  # 16 MB

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

# Adicione a URL do PostgreSQL diretamente aqui para garantir que está sendo usada
os.environ['DATABASE_URL'] = 'postgres://ubksl4tqlamln4:p1c21324f05453e39b2141da690c0b6b22f4d87c6f6e3af6a5c16f4fcb87bc1f1@cd5gks8n4kb20g.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d5qaspp2blgbc0'

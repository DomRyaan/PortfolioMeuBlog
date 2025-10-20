import sys
from flask_frozen import Freezer
from app import app
from database.post import Post
import os
import shutil

freezer = Freezer(app)

BUILD_DIR = 'build'
if os.path.exists(BUILD_DIR):
    print(f"Limpando a pasta '{BUILD_DIR}' antiga...")
    shutil.rmtree(BUILD_DIR)

# É aqui que a mágica acontece!
# Este gerador encontra todos os seus posts e cria as URLs para eles.
@freezer.register_generator
def post_mostrar():
    # Usamos um contexto do app para poder acessar o banco de dados
    with app.app_context():
        # Pega todos os posts do seu banco SQLite
        posts = Post.query.all()
        for post in posts:
            # Para cada post, informamos a URL que deve ser gerada.
            # O nome 'post_id' DEVE ser o mesmo da sua rota @app.route('/blog/artigo/<int:post_id>')
            yield {'post_id': post.id}

if __name__ == '__main__':
    freezer.freeze()
    print("Copiando arquivos de configuração...")
    source_redirects_file = '_redirects'
    destination_folder = 'build'
    
    if os.path.exists(source_redirects_file):
        shutil.copy(source_redirects_file, destination_folder)
        print(" -> Arquivo '_redirects' copiado para a pasta 'build'.")
    else:
        print(f" -> AVISO: Arquivo '{source_redirects_file}' não encontrado na raiz.")

    print("\nProcesso finalizado!")
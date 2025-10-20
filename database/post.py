from .dbconfig import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = 'Post'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    trecho = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    @staticmethod
    def adicionar_post(post):
        try:
            db.session.add(post)
            db.session.commit()
        except Exception as ex:
            db.session.rollback()
            print("Ocorreu um erro: " + str(ex))
        finally:
            db.session.close()
    
    @staticmethod
    def deletar_post(livro):
        try:
            db.session.delete(livro)
            db.session.commit()
            print("Post Excluido")
        except Exception as ex:
            db.session.rollback()
            print("Erro ao deletar: " + ex)
        finally:
            db.session.close()
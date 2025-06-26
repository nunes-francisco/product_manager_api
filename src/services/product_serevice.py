from src.models.produto import Produto
from app import db
from sqlalchemy.exc import SQLAlchemyError

class ProdutoService:
    """Serviço para gerenciar operações relacionadas a produtos."""
    @staticmethod
    def listar():
        """Lista todos os produtos."""
        return [p.to_dict() for p in Produto.query.all()]

    @staticmethod
    def obter(produto_id):
        """Obtém um produto pelo ID."""
        return Produto.query.get_or_404(produto_id).to_dict()

    @staticmethod
    def criar(dados):
        """Cria um novo produto."""
        novo = Produto(**dados)
        db.session.add(novo)
        db.session.commit()
        return novo.to_dict()

    @staticmethod
    def atualizar(produto_id, dados):
        """Atualiza um produto existente."""
        produto = Produto.query.get_or_404(produto_id)
        for campo in ['nome', 'preco', 'estoque']:
            if campo in dados:
                setattr(produto, campo, dados[campo])
        db.session.commit()
        return produto.to_dict()

    @staticmethod
    def deletar(produto_id):
        
        produto = Produto.query.get_or_404(produto_id)
        db.session.delete(produto)
        db.session.commit()
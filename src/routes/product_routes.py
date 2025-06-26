from flask import Blueprint, jsonify, request
from http import HTTPStatus
from sqlalchemy.exc import SQLAlchemyError
from src.services.produto_service import ProdutoService

produto_bp = Blueprint('produto', __name__)

@produto_bp.route('/produtos', methods=['GET'])
def listar_produtos():
    """Lista todos os produtos
    ---
    responses:
      200:
        description: Lista de produtos
    """
    return jsonify(ProdutoService.listar()), HTTPStatus.OK

@produto_bp.route('/produtos/<int:produto_id>', methods=['GET'])
def obter_produto(produto_id):
    """Obtém um produto por ID
    ---
    parameters:
      - in: path
        name: produto_id
        required: true
        type: integer
    responses:
      200:
        description: Produto encontrado
    """
    return jsonify(ProdutoService.obter(produto_id)), HTTPStatus.OK

@produto_bp.route('/produtos', methods=['POST'])
def criar_produto():
    """Cria um novo produto
    ---
    parameters:
      - in: body
        name: body
        schema:
          required:
            - nome
            - preco
            - estoque
          properties:
            nome:
              type: string
            preco:
              type: number
            estoque:
              type: integer
    responses:
      201:
        description: Produto criado com sucesso
    """
    try:
        dados = request.get_json()
        produto = ProdutoService.criar(dados)
        return jsonify(produto), HTTPStatus.CREATED
    except (KeyError, SQLAlchemyError) as erro:
        return jsonify({'erro': str(erro)}), HTTPStatus.BAD_REQUEST

@produto_bp.route('/produtos/<int:produto_id>', methods=['PUT'])
def atualizar_produto(produto_id):
    """Atualiza um produto existente
    ---
    parameters:
      - in: path
        name: produto_id
        required: true
        type: integer
      - in: body
        name: body
        schema:
          properties:
            nome:
              type: string
            preco:
              type: number
            estoque:
              type: integer
    responses:
      200:
        description: Produto atualizado com sucesso
    """
    try:
        dados = request.get_json()
        produto = ProdutoService.atualizar(produto_id, dados)
        return jsonify(produto), HTTPStatus.OK
    except SQLAlchemyError as erro:
        return jsonify({'erro': str(erro)}), HTTPStatus.BAD_REQUEST

@produto_bp.route('/produtos/<int:produto_id>', methods=['DELETE'])
def deletar_produto(produto_id):
    """Remove um produto
    ---
    parameters:
      - in: path
        name: produto_id
        required: true
        type: integer
    responses:
      204:
        description: Produto removido com sucesso
    """
    try:
        ProdutoService.deletar(produto_id)
        return '', HTTPStatus.NO_CONTENT
    except SQLAlchemyError as erro:
        return jsonify({'erro': str(erro)}), HTTPStatus.BAD_REQUEST

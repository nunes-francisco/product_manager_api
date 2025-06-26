import pytest
from app import app, db
from src.models.produto import Produto

@pytest.fixture
def client():
    """Fixture para criar um cliente de teste Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_criar_listar_produto(client):
    # Testando a criação de um produto
    response = client.post('/produtos', json={
        'nome': 'Mouse',
        'preco': 49.99,
        'estoque': 100
    })
    assert response.status_code == 201

    response = client.get('/produtos')
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['nome'] == 'Mouse'
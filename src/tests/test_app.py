import pytest 
from src.model.colaborador_model import Colaborador
from src.app import create_app
import time

 
@pytest.fixture
def app():
    app = create_app()
    yield app
    
@pytest.fixture
def client(app):
    return app.test_client()


def test_pegar_todos_colaboradores(client):
    resposta = client.get('/colaborador/todos-colaboradores')
    assert resposta.status_code == 200
    

def test_desempenho_requisicao_get(client):
    comeco = time.time() 
    
    for _ in range(100):
        resposta = client.get('/colaborador/todos-colaboradores')
    
    fim = time.time() - comeco 
    
    assert fim < 1.0 
    
def test_desempenho_requisicao_post(client):
    comeco = time.time() 
    
    colaborador = {
        'nome': 'teste da silva',
        'email': 'testando@teste.com',
        'senha': '654321',
        'cargo': 'tester',
        'salario': 120.99
    }
    
    for _ in range(100):
        resposta = client.post('/colaborador/cadastrar', json=colaborador)
        
    fim = time.time() - comeco 
    assert fim < 20.0
    
def test_soma():
    assert 2 + 2 == 3
    
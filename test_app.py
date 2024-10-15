import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_cotacao_atual(client):
    response = client.get('/cotacao-atual')
    assert response.status_code == 200
    data = response.get_json()
    assert 'data' in data
    assert 'Valor' in data

def test_cotacao_por_data_valida(client):
    params = {'data_inicial': '01/10/2024', 'data_final': '14/10/2024'}
    response = client.get('/cotacao_por_data', query_string=params)
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_cotacao_por_data_invalida(client):
    response = client.get('/cotacao_por_data')
    assert response.status_code == 200
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == "As datas de origem e de destino são obrigatórias."

def test_formatacao_data(client):
    params = {'data_inicial': '01/10/2024', 'data_final': '14/10/2024'}
    response = client.get('/cotacao_por_data', query_string=params)
    data = response.get_json()
    if data:
        for item in data:
            assert 'data' in item
            assert 'bid' in item

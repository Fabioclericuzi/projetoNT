import pytest
from unittest.mock import Mock

def pegar_cotacao_por_data(data_inicial, data_final):
    if not data_inicial or not data_final:
        return {"error": "As datas de origem e de destino são obrigatórias."}
    return [{'data': '2024-10-01', 'bid': 5.25}, {'data': '2024-10-02', 'bid': 5.30}]

def test_pegar_cotacao_por_data_valida():
    data = pegar_cotacao_por_data('01/10/2024', '14/10/2024')
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]['data'] == '2024-10-01'
    assert data[0]['bid'] == 5.25

def test_pegar_cotacao_por_data_invalida():
    data = pegar_cotacao_por_data('', '')
    assert 'error' in data
    assert data['error'] == "As datas de origem e de destino são obrigatórias."

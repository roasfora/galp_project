import sys
import os
import pytest
import pandas as pd
from unittest.mock import patch

# Adiciona o diretório src ao caminho do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from api_extract import fetch_monthly_adjusted_data  # Ajustando para o nome correto do arquivo

@pytest.fixture
def mock_api_response():
    """Simula uma resposta válida da API Alpha Vantage"""
    return {
        "Monthly Adjusted Time Series": {
            "2024-01-31": {
                "1. open": "15.23",
                "2. high": "16.00",
                "3. low": "14.50",
                "4. close": "15.80",
                "5. adjusted close": "15.75",
                "6. volume": "500000",
                "7. dividend amount": "0.05"
            }
        }
    }

@patch("api_extract.requests.get")  # Ajustando o caminho corretamente
def test_fetch_monthly_adjusted_data_success(mock_get, mock_api_response):
    """Teste: Verifica se a função retorna um DataFrame válido ao receber resposta correta da API"""
    
    # Mock da resposta da API
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_api_response

    # Definir API Key temporária para o teste
    os.environ["API_KEY_GALP"] = "fake_api_key"

    df = fetch_monthly_adjusted_data()

    assert isinstance(df, pd.DataFrame), "A função deve retornar um DataFrame"
    assert not df.empty, "O DataFrame não deve estar vazio"
    assert "open" in df.columns, "A coluna 'open' deve estar presente no DataFrame"
    assert "high" in df.columns, "A coluna 'high' deve estar presente no DataFrame"

@patch("api_extract.requests.get")
def test_fetch_monthly_adjusted_data_missing_api_key(mock_get):
    """Teste: Verifica se a função lança erro quando a API Key não está configurada"""
    
    # Remover API Key para simular erro
    if "API_KEY_GALP" in os.environ:
        del os.environ["API_KEY_GALP"]

    with pytest.raises(ValueError, match="A API Key não está definida"):
        fetch_monthly_adjusted_data()

import sys
import os
import pytest
from unittest.mock import patch

# Adiciona o diretório src ao caminho do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from web_scraping_beautifulsoup import fetch_eur_to_usd_rate  # Ajustando para o nome correto do arquivo

@patch("web_scraping_beautifulsoup.requests.get")
def test_fetch_eur_to_usd_rate_success(mock_get):
    """Teste: Verifica se o scraper retorna dados corretamente"""

    # Simulando a resposta do site
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = '<span class="ccOutputRslt">1.10 USD</span>'

    data = fetch_eur_to_usd_rate()

    assert isinstance(data, dict), "A função deve retornar um dicionário"
    assert "timestamp" in data, "O dicionário deve conter 'timestamp'"
    assert "eur_to_usd_rate" in data, "O dicionário deve conter 'eur_to_usd_rate'"
    assert isinstance(data["eur_to_usd_rate"], float), "A taxa de câmbio deve ser um número"

@patch("web_scraping_beautifulsoup.requests.get")
def test_fetch_eur_to_usd_rate_failure(mock_get):
    """Teste: Verifica erro ao não conseguir acessar a página"""
    
    mock_get.return_value.status_code = 500

    with pytest.raises(RuntimeError, match="Error scraping EUR to USD exchange rate"):
        fetch_eur_to_usd_rate()

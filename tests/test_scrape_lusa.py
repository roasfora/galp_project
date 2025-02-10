import sys
import os
import pytest
from unittest.mock import patch

# Adiciona o diretório src ao caminho do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from web_scraping_selenium import scrape_lusa_with_selenium  # Ajustando para a estrutura correta

class MockElement:
    """Mock para simular elementos do Selenium"""
    def __init__(self, text, href):
        self.text = text
        self.href = href

    def get_attribute(self, attr):
        if attr == "href":
            return self.href
        return None

@patch("web_scraping_selenium.webdriver.Chrome")  # Ajuste o caminho corretamente
def test_scrape_lusa_with_news(mock_browser):
    """Teste: Verifica se o scraper retorna notícias corretamente"""
    
    # Simulando o driver e elementos HTML
    mock_driver = mock_browser.return_value
    mock_driver.find_elements.return_value = [
        MockElement("Notícia Teste 1", "https://www.lusa.pt/test1"),
        MockElement("Notícia Teste 2", "https://www.lusa.pt/test2")
    ]

    news_list = scrape_lusa_with_selenium()
    
    assert isinstance(news_list, list), "O retorno deve ser uma lista"
    assert len(news_list) > 0, "Deve haver pelo menos uma notícia"
    assert "title" in news_list[0] and "link" in news_list[0], "Cada item deve conter 'title' e 'link'"

@patch("web_scraping_selenium.webdriver.Chrome")
def test_scrape_lusa_no_news(mock_browser):
    """Teste: Verifica se o scraper retorna lista vazia quando não há notícias"""
    
    mock_driver = mock_browser.return_value
    mock_driver.find_elements.return_value = []  # Simula página sem notícias

    news_list = scrape_lusa_with_selenium()

    assert isinstance(news_list, list), "O retorno deve ser uma lista"
    assert len(news_list) == 0, "Lista deve estar vazia quando não há notícias"

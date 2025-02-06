import requests
from bs4 import BeautifulSoup

# URL do HTML hospedado localmente ou online
url = "http://localhost:8000/index.html"  # Se for um site online, troque pela URL real

# Faz a requisição HTTP para obter o conteúdo do HTML
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parse do HTML usando BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extrair o título do curso
    titulo = soup.find("h1").text
    print(f"Título do Curso: {titulo}")

    # Extrair detalhes do curso
    detalhes = soup.find("div", class_="course-details")
    if detalhes:
        for p in detalhes.find_all("p"):
            print(p.text)

    # Extrair horários
    horarios = soup.find("div", class_="schedule")
    if horarios:
        print("\nHorários:")
        for p in horarios.find_all("p"):
            print(p.text)

    # Extrair preços
    investimento = soup.find("div", class_="pricing")
    if investimento:
        print("\nInvestimento:")
        for p in investimento.find_all("p"):
            print(p.text)

else:
    print("Erro ao acessar a página:", response.status_code)

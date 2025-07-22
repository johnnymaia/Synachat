import requests
from bs4 import BeautifulSoup
import re
import time

def obter_conteudo_jp():
    """Obtém conteúdo relevante do site do Jovem Programador"""
    urls = [
    "https://www.jovemprogramador.com.br/",
    "https://www.jovemprogramador.com.br/sobre.php",
    "https://www.jovemprogramador.com.br/hackathon/",
    "http://jovemprogramador.com.br/duvidas.php",
    ]

    conteudo_completo = ""

    for url in urls:
        print(f"[SISTEMA] Acessando: {url}")
        try:
            # Configurar cabeçalhos para simular navegador
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept-Language': 'pt-BR,pt;q=0.9'
            }

            response = requests.get(url, headers=headers, timeout=15)

            if response.status_code != 200:
                print(f"[ERRO] Status {response.status_code} em {url}")
                continue

            soup = BeautifulSoup(response.text, 'html.parser')

            # Remover elementos irrelevantes
            for elemento in soup(["script", "style", "header", "footer", "nav", "form", "img"]):
                elemento.decompose()

            # Extrair texto principal
            texto = soup.get_text(separator=' ', strip=True)
            texto = re.sub(r'\s+', ' ', texto)  # Normalizar espaços

            # Adicionar contexto de URL
            conteudo_completo += f"\n\n--- CONTEÚDO DE {url} ---\n{texto}"

            # Respeitar o tempo entre requisições
            time.sleep(2)

        except Exception as e:
            print(f"[ERRO] Falha ao acessar {url}: {str(e)}")

    return conteudo_completo
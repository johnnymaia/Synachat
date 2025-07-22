
# 🤖 Syna - Assistente Virtual do Jovem Programador

Syna é um chatbot inteligente desenvolvido em Python com integração à API Gemini (Google Generative AI). Ela responde dúvidas exclusivamente sobre o programa **Jovem Programador**, utilizando informações atualizadas diretamente do site oficial.

## 📌 Funcionalidades

- Raspagem automática de conteúdo do site [jovemprogramador.com.br](https://www.jovemprogramador.com.br)
- Geração de respostas contextualizadas com IA
- Filtro inteligente para garantir que apenas perguntas relacionadas ao programa sejam respondidas
- Execução simples via terminal com histórico de conversa

---

## 🛠️ Tecnologias Utilizadas

- `Python 3.10+`
- [`requests`](https://pypi.org/project/requests/)
- [`BeautifulSoup` (bs4)](https://pypi.org/project/beautifulsoup4/)
- [`re`](https://docs.python.org/3/library/re.html)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)
- [`google.generativeai`](https://pypi.org/project/google-generativeai/) (Gemini API)

---

## 📂 Estrutura do Projeto

```
├── main.py                # Execução principal do chatbot Syna
├── web_scraper.py         # Função para extrair conteúdo do site Jovem Programador
├── .env                   # Chave da API Gemini (não incluída no repositório)
└── README.md              # Documentação do projeto
```

---

## ⚙️ Como Executar

### 1. Clonar o repositório
```bash
git clone https://github.com/seuusuario/syna-chatbot.git
cd syna-chatbot
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

> Crie um arquivo `requirements.txt` com:
```
requests
beautifulsoup4
python-dotenv
google-generativeai
```

### 3. Configurar chave da API Gemini
Crie um arquivo `.env` na raiz do projeto com:

```
GEMINI_API_KEY=sua_chave_api_aqui
```

### 4. Executar
```bash
python main.py
```

---

## 🧠 Como Funciona

1. O `web_scraper.py` coleta o conteúdo das principais páginas do site Jovem Programador.
2. O `main.py` carrega esse conteúdo e usa o modelo **Gemini 1.5 Flash** para responder perguntas.
3. O sistema verifica se a pergunta é sobre o programa; se sim, responde com base no conteúdo.
4. Caso contrário, recusa educadamente e oferece ajuda sobre temas válidos.

---

## 📌 Exemplo de uso

```bash
Você: Quando começam as inscrições do Jovem Programador?
Syna: As inscrições geralmente ocorrem entre fevereiro e março. Para informações atualizadas, acesse www.jovemprogramador.com.br.
```

---

## 📄 Licença

Este projeto é de uso educacional e experimental. Para uso comercial ou redistribuição, entre em contato com os autores.

---

## 👨‍💻 Desenvolvido por

- Ted Silva e equipe

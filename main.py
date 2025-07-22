import google.generativeai as genai
import os
from dotenv import load_dotenv
import time

# Importa a função de scraping do novo arquivo
from web_scraper import obter_conteudo_jp

# =============== CONFIGURAÇÃO INICIAL ===============

# Carrega variáveis de ambiente
load_dotenv()
chave_api = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=chave_api)

# Inicializar o modelo Gemini
modelo = genai.GenerativeModel("gemini-1.5-flash")

# =============== CONTEXTO DO JOVEM PROGRAMADOR ===============

CONTEXTO_JP = """
Jovem Programador é um programa de capacitação tecnológica gratuito oferecido pelo Senac SC em parceria com o Fecomércio e Sesc.
O projeto forma programadores para atuação em empresas de Santa Catarina através de aulas híbridas.

Principais tópicos relacionados:
- Inscrições e processo seletivo
- Conteúdo do curso e módulos
- Duração e formato das aulas
- Oportunidades de emprego
- Hackathons e eventos
- Parceiros e patrocinadores
- Unidades do Senac participantes
- Dúvidas frequentes sobre o programa
"""

# =============== FUNÇÕES DO CHATBOT ===============

def verificar_tema_pergunta(pergunta):
    """Verifica se a pergunta está relacionada ao Jovem Programador"""
    prompt = f"""
    Você é um filtro de conteúdo especializado no curso Jovem Programador.
    Avalie se a pergunta abaixo está diretamente relacionada ao programa Jovem Programador, incluindo tópicos como inscrições, conteúdo do curso, duração, oportunidades de emprego, hackathons, eventos, parceiros, unidades ou dúvidas frequentes.

    Contexto sobre o Jovem Programador:
    {CONTEXTO_JP}

    Pergunta: "{pergunta}"

    Responda APENAS com:
    - "sim" se a pergunta for sobre o Jovem Programador (qualquer um dos tópicos mencionados).
    - "não" se for sobre qualquer outro assunto.

    Não inclua explicações, justificativas ou outros textos.
    """

    try:
        response = modelo.generate_content(prompt)
        resposta = response.text.strip().lower()
        return resposta == "sim"
    except Exception as e:
        print(f"[ERRO] Falha na verificação de tema: {str(e)}")
        return False

def gerar_resposta(pergunta, conteudo_site):
    """Gera resposta baseada no contexto do Jovem Programador"""
    prompt = f"""
    Você é Syna, uma assistente virtual especializada exclusivamente no curso Jovem Programador.
    Sua função é responder perguntas SOBRE ESTE PROGRAMA usando as informações abaixo.

    INSTRUÇÕES CRÍTICAS:
    1. Responda SEMPRE em português brasileiro (pt-BR)
    2. Se a pergunta NÃO for sobre o Jovem Programador, responda:
       "Desculpe, só posso responder perguntas sobre o curso Jovem Programador. Posso te ajudar com alguma dúvida sobre o programa?"

    3. Se não encontrar informação suficiente, responda:
       "Não encontrei informações sobre isso no site do Jovem Programador. Você pode consultar diretamente em www.jovemprogramador.com.br ou perguntar sobre outro tópico relacionado ao programa."


    Informações gerais sobre o programa:
    {CONTEXTO_JP}

    Conteúdo atualizado do site:
    {conteudo_site[:20000]}  Pergunta do usuário:
    "{pergunta}"

    Resposta em português brasileiro:
    """

    try:
        response = modelo.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"[ERRO] Falha ao gerar resposta: {str(e)}")
        return "Desculpe, ocorreu um erro ao processar sua pergunta. Por favor, tente novamente mais tarde."

# =============== PROGRAMA PRINCIPAL ===============

def main():
    # Inicialização
    print("\n" + "="*60)
    print("ASSISTENTE VIRTUAL SYNA - JOVEM PROGRAMADOR")
    print("="*60)
    print("Sou a Syna, sua assistente para o programa Jovem Programador!")
    print("Carregando informações atualizadas... Por favor aguarde.")

    # Carregar conteúdo do site
    conteudo_site = obter_conteudo_jp()

    print("\n" + "-"*60)
    print(f"Conteúdo carregado com sucesso! Estou pronta para ajudar.")
    print("Faça perguntas sobre o curso Jovem Programador (digite 'sair' para encerrar)")
    print("-"*60 + "\n")

    # Histórico de conversa
    historico = []

    # Loop de conversação
    while True:
        try:
            mensagem_usuario = input("Você: ").strip()

            if not mensagem_usuario:
                continue

            if mensagem_usuario.lower() in ["sair", "exit", "bye", "tchau", "encerrar"]:
                print("\nSyna: Até logo! Qualquer dúvida sobre o Jovem Programador, estou à disposição.")
                break

            # Verificar tema antes de processar
            if not verificar_tema_pergunta(mensagem_usuario):
                print("\nSyna: Desculpe, só posso responder perguntas sobre o curso Jovem Programador.")
                print("Syna: Posso te ajudar com informações sobre: inscrições, conteúdo do curso, oportunidades ou hackathons?")
                print("-"*60)
                continue

            # Gerar resposta contextualizada
            print("Syna: Processando sua pergunta...")
            resposta = gerar_resposta(mensagem_usuario, conteudo_site)

            # Registrar no histórico
            historico.append({"usuario": mensagem_usuario, "bot": resposta})

            # Exibir resposta formatada
            print("\nSyna:", resposta)
            print("-"*60)

        except KeyboardInterrupt:
            print("\n\nEncerrando a Syna...")
            break
        except Exception as e:
            print(f"\n[ERRO] Ocorreu um problema: {str(e)}")
            print("Syna: Desculpe, tive um problema. Por favor, reformule sua pergunta.")
            print("-"*60)

if __name__ == "__main__":
    main()
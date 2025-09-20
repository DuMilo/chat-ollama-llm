# app.py
# Este script cria uma aplicação de chat simples que interage com um modelo de linguagem grande (LLM)
# hospedado em um servidor Ollama. O usuário pode digitar mensagens, e o LLM responderá com base nessas mensagens.

import requests
import json

# O endereço completo do servidor Ollama e do endpoint que gera respostas
OLLAMA_ENDPOINT = "http://ollama.eastus.cloudapp.azure.com:11434/api/generate"

print("Aplicação de Chat com LLM iniciada!")
print("Digite 'sair' a qualquer momento para terminar.")

while True:
    # 1. Pede ao usuário a mensagem (prompt)
    prompt_usuario = input("\nVocê: ")
    
    if prompt_usuario.lower() == 'sair':
        print("Até logo!")
        break

    # 2. Monta o "pacote" de dados (payload) em formato de dicionário Python
    data = {
        "model": "phi3:mini",
        "prompt": prompt_usuario,
        "stream": False  
    }

    try:
        # 3. Envia a requisição para o LLM
        print("IA está pensando...")
        response = requests.post(OLLAMA_ENDPOINT, json=data)
        
        response.raise_for_status() 

        # 4. Extrai a resposta e a exibe para o usuário
        # O response.text contém a resposta em string, que convertemos para JSON e guardamos no response_json.json
        response_json = json.loads(response.text)
        resposta_ia = response_json["response"]
        
        print(f"IA: {resposta_ia.strip()}") 

    except requests.exceptions.RequestException as e:
        print(f"\n[Erro de Conexão]: Não foi possível conectar ao servidor Ollama.")
        print(f"Detalhes: {e}")
        break
    except KeyError:
        print("\n[Erro]: A resposta da API não continha a chave 'response'.")
        print("Resposta recebida:", response.text)
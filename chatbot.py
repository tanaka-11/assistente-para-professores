# Importação com apelido
import google.generativeai as genai
import os

# Configurando parâmetros do chatbot
generation_config = {
  "candidate_count": 1,
  "temperature": 0.5,
}

# Configurações de segurança
safety_settings = {
    "HATE": "BLOCK_NONE",
    "HARASSMENT": "BLOCK_NONE",
    "SEXUAL" : "BLOCK_NONE",
    "DANGEROUS" : "BLOCK_NONE",
}

# Acessar a chave API a partir de uma variável de ambiente
api_key = os.getenv("GOOGLE_API_KEY")

# Inicializando o modelo
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings,
                              api_key=api_key)

# Iniciando o chat começando com o historico vazio
chat = model.start_chat(history=[])

# Loop para o chat funcionar ate o usuario encerrar
while True:
    # Criando o prompt para pergunta do usuario
    prompt = input("Esperando sua pergunta: ")

    # Encerra o chat se o usuário digitar "fim"
    if prompt.lower() == "fim":
        break

    # Permite que o usuário altere a temperatura
    if prompt.startswith("/set_temperature "):
        temperature = float(prompt[16:])
        generation_config["temperature"] = temperature
        continue

    try:
        # Guardando mensagem enviada recebendo o valor da prompt
        response = chat.send_message(prompt)
        
        # Verifica a resposta do chatbot para conteúdo inapropriado
        if "palavra_inapropriada" in response.text:
            response.text = "Desculpe, eu não posso dizer isso."

        print("Resposta: ", response.text, '\n')

        # Salva a conversa em um arquivo de log
        with open("chat_log.txt", "a") as file:
            file.write("Usuário: " + prompt + "\n")
            file.write("Chatbot: " + response.text + "\n")
    except Exception as e:
        print("Ocorreu um erro: ", str(e))

# Assistente para professores

**Descrição do Projeto - Amigo do Professor**

Um chatbot criado em Python usando o Studio IA para auxiliar professores mais velhos em suas tarefas diárias e aproxima-los da tecnologia de forma amigável e eficiente.

---

### Passo a passo de como fazer o chatbot como um assistente para professores.

1. Configuração do Ambiente

- Instalar o SDK do Google:

```
!pip install -q -U google-generativeai
```

2. Importar bibliotecas

- Começamos importando as bibliotecas necessárias sendo elas o: **google.generativeai** (com o apelido **_genai_**) que serve para acessar os recursos da API e **google.colab.userdata** para podermos esconder nossa API Key.

```
# Importação com apelido
import google.generativeai as genai
from google.colab import userdata
```

3. Configurando parâmetros do chatbot

- Onde **candidate_count** (número de opções da resposta) e **temperature** (criatividade na resposta do chatbot de 0 a 1, sendo 1 mais criativo e 0 mais preciso).

```
generation_config = {
  "candidate_count": 1,
  "temperature": 0.5,
}
```

4. Configurações de segurança

- Segurança das palavras ditas pelo chatbot (Futuramente implementarei os filtros).

```
safety_settings = {
    "HATE": "BLOCK_NONE",
    "HARASSMENT": "BLOCK_NONE",
    "SEXUAL" : "BLOCK_NONE",
    "DANGEROUS" : "BLOCK_NONE",
}
```

5. Inicializando o modelo

- Utilizando a versão 1.0 pois se tratar de uma versão mais estavel.

```
model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
```

6. Criando o chatbot

```
# Iniciando o chat começando com o historico vazio
chat = model.start_chat(history=[])

# Criando o prompt para pergunta do usuario
prompt = input("Esperando sua pergunta: ")

# Loop para o chat funcionar ate o usuario encerrar
while prompt != "fim":
  # Mensagem enviada recebendo o valor da prompt
  response = chat.send_message(prompt)
  print("Resposta: ", response.text, '\n')
  prompt = input("Esperando sua pergunta: ")
```

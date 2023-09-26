# Funcionamento do Chat como API
Este chat funciona como uma API simulada, onde um usuário pode enviar uma mensagem em formato de prompt e receber uma resposta formatada em JSON, seguindo categorias pré-definidas.

### Categorias
- Saudações (greeting):
    - Prompt: ["oi", "olá", "ola"]
    - Respostas: ["Olá, como vai?", "Oi, tudo bem?", "Olá, tudo bem?"]
    - Ação: ["say"]

- Despedidas (goodbye):
    - Prompt: ["tchau", "xau", "bye", "adeus"]
    - Respostas: ["Tchau, até mais!", "Até mais!", "Tchau, volte sempre!"]
    - Ação: ["say", "stop"]

- Perguntas sobre produtos (product):
    - Prompt: ["produto"]
    - Respostas: [Resposta gerada dinamicamente]
    - Ação: ["see"]

- Outras Perguntas (other):
    - Prompt: ["que horas é?", "qual a distância entre a terra e o sol?"]
    - Respostas: [Resposta gerada dinamicamente]
    - Ação: ["say", "see"]

### Como Usar
O usuário envia um prompt correspondente à categoria desejada. A API então gera uma resposta apropriada baseada na categoria e retorna um objeto JSON contendo a resposta, pronto para ser utilizado.
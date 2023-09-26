# Sem nome
Trabalho Pratico da Disciplina de Inteligência Artificial - GCC128 (UFLA)

## Robô Social com Interação Humana usando Modelo Arquitetônico Sentir-Pensar-Agir

O objetivo deste projeto de Inteligência Artificial (IA) é prototipar um robô social capaz de interagir com seres humanos de forma autônoma e natural. O projeto se baseará no modelo arquitetônico "Sentir-Pensar-Agir", que permite que o robô perceba seu ambiente, processe informações e tome decisões, adaptando seu comportamento de acordo com as interações com os humanos.

O projeto inclui o uso da câmera para a visão do robô, com reconhecimento de objetos utilizando TensorFlow. Para a comunicação com o robô, são utilizados o microfone e autofalantes, junto com as bibliotecas speech_recognition (fala em texto) e gTTS (texto em fala).

### Funcionalidades
- Visão: Utilização de uma câmera para a visão do robô, com reconhecimento de objetos implementado usando TensorFlow.

- Comunicação: O robô utiliza um microfone e alto-falantes para a interação. A comunicação de voz é convertida em texto com a biblioteca speech_recognition, e o texto é convertido em fala usando a gTTS.

- Tomada de Decisões: As decisões do robô são baseadas em categorias predefinidas:

    - greetings: Responde cumprimentos com fala.
    - goodbyes: Responde a despedidas com fala e encerra o programa.
    - products: Reconhece produtos na imagem da câmera e responde com fala.
    - other: Responde a perguntas utilizando a API do Chat GPT.


### Tecnologias Utilizadas
- <a href="https://www.tensorflow.org/?hl=pt-br">TensorFlow</a>: Utilizado para o reconhecimento de objetos a partir da visão do robô pela câmera.

- <a href="https://pypi.org/project/SpeechRecognition/">speech_recognition</a>: Biblioteca para converter fala em texto para comunicação com o robô.

- <a href="https://pypi.org/project/gTTS/">gTTS</a> (Google Text-to-Speech): Utilizado para converter texto em fala para a comunicação do robô com os humanos.

- <a href="https://platform.openai.com/docs/guides/gpt">openai</a>: Categorização e respostas para as falas que o robo escutar com a API do Chat GPT.

### Como Executar

1 . Clone este repositório.
```
git clone git@github.com:anabrtorres/ai-project.git
cd seu-repositorio
```

2. Instale as dependências.
```
pip install -r requirements.txt
```

3. Execute o programa.
```
python3 main.py
```


### Contribuição
Contribuições são bem-vindas! Para qualquer melhoria ou correção de bugs, sinta-se à vontade para abrir uma issue ou enviar um pull request.
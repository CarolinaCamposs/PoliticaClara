# **Política Clara**

**Simplificando Políticas de Privacidade com Inteligência Artificial**

---

## **Descrição**

**Política Clara** é uma extensão de navegador desenvolvida para ajudar os usuários a compreenderem políticas de privacidade de forma mais simples e acessível. Utilizando **IA generativa** e **Modelos de Linguagem de Grande Escala (LLMs)**, como a API da Cohere, a ferramenta transforma trechos complexos de políticas de privacidade em explicações claras e organizadas, permitindo uma experiência mais informada e consciente na interação com serviços digitais.

---

## **Funcionalidades**

- **Análise Automática**: Transforma trechos complexos de políticas de privacidade em explicações acessíveis.
- **Simplificação Baseada em Critérios**: Avalia e organiza o conteúdo com base em sete critérios essenciais, como:
  - O que é coletado?
  - Como os dados são tratados?
  - Como a empresa pode usar os dados coletados? 
  - As informações podem ser compartilhadas ou vendidas para terceiros? 
  - Como os dados são armazenados? 
  - O fornecimento dos dados é voluntário ou obrigatório? Quais as consequências de uma recusa? 
  - Quais são as medidas adotadas para garantir a confidencialidade, integridade e qualidade dos dados?
    
- **Integração Direta no Navegador**: Funciona como uma extensão compatível com navegadores como Mozilla Firefox.
- **Interface Intuitiva**: Apresenta os resultados em um popup direto no navegador.

---

## **Tecnologias Utilizadas**

- **Backend**:
  - [Python](https://www.python.org/) - Linguagem principal para o processamento.
  - [Flask](https://flask.palletsprojects.com/) - Framework para construção da API.
  - [Flask-CORS](https://flask-cors.readthedocs.io/) - Para gerenciar políticas de origem cruzada.
  - [Cohere API](https://cohere.ai/) - Para análise e geração de explicações usando LLMs.

- **Frontend**:
  - Extensão para **Mozilla Firefox**.
  - **JavaScript** - Para comunicação entre navegador e backend.
  - **WebExtension APIs** - Para integração com o navegador.

---

## **Instalação**

### **Pré-requisitos**
- [Python 3.8+](https://www.python.org/)
- Pip (gerenciador de pacotes do Python)
- Navegador **Mozilla Firefox**
- Chave da API Cohere

### **Passos**
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/politica-clara.git

2. Navegue até o diretório do projeto:
   ```bash
   cd politica-clara

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt

4. Instale as dependências:

- No arquivo app.py, substitua 'SUA_CHAVE_API' pela sua chave da API Cohere.

6. Inicie o servidor Flask:
   ```bash
   python app.py

7. Carregue a extensão no Mozilla Firefox:
   -  Abra about:debugging#/runtime/this-firefox no Firefox.
   -  Clique em "Carregar Extensão Temporária" e selecione a pasta extension do projeto.

---
  
### **Como Usar**

  1. Selecione um texto em qualquer política de privacidade no navegador.
  2. Clique na extensão no canto superior da tela.
  3. Um popup será exibido com uma explicação clara e objetiva sobre o texto selecionado.

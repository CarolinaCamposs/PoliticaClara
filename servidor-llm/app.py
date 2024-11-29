import cohere
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Inicializa o cliente da API Cohere
co = cohere.Client('FIt4rbb19vc2KtzK6Z0aPkg0DWXqCrFlbsquz2Ti')

@app.route('/explain', methods=['POST'])
def explain_text():
    # Obtém os dados enviados pelo frontend
    data = request.get_json()
    selected_text = data.get('text', '').strip()
    
    if not selected_text:
        return jsonify({'error': 'Nenhum texto selecionado para análise.'}), 400
    
    # Prompt para a IA com critérios detalhados
    prompt = f"""
    Analise o seguinte trecho de uma política de privacidade: "{selected_text}".
    Explique de forma clara e objetiva os aspectos abaixo. Evite termos técnicos e garanta que "tratamento" e "uso" dos dados sejam abordados de maneira distinta. Use uma linguagem simples, adequada para quem não possui conhecimento técnico. Se um critério não for abordado no trecho, informe claramente.

    1. O que é coletado?
    Liste os tipos de dados pessoais mencionados, como cadastrais, financeiros, sensíveis, ou outros.

    2. Como os dados são tratados?
    Descreva os processos e operações realizadas com os dados, como coleta, organização, armazenamento, eliminação ou anonimização, e quem realiza esses processos.

    3. Para que os dados são usados?
    Informe as finalidades específicas do uso dos dados, como prestação de serviços, segurança, ou atendimento a obrigações legais.

    4. Os dados são compartilhados ou vendidos?
    Especifique com quem os dados podem ser compartilhados (ex.: empresas parceiras, instituições financeiras, órgãos públicos) e os motivos para isso.

    5. Como os dados são armazenados?
    Descreva como e onde os dados são guardados, se o trecho mencionar essa informação.

    6. O fornecimento dos dados é obrigatório ou opcional?
    Esclareça se o fornecimento dos dados é necessário para os serviços ou contratos, e o que acontece se o usuário não fornecê-los.

    7. Quais medidas de segurança protegem os dados?
    Explique brevemente como a empresa protege os dados, mencionando práticas ou políticas de segurança se estiverem descritas.

    Instruções adicionais:

    Resuma cada critério em no máximo duas frases claras e diretas.
    Inclua o título do critério antes de cada explicação.
    Diferencie claramente "tratamento" e "uso" para evitar redundância.
    Caso um critério não seja abordado no trecho, escreva: "Não mencionado."
    """
    
    try:
        # Chamada à API Cohere
        response = co.generate(
            model='command-nightly',
            prompt=prompt,
            max_tokens=600,  # Evitar respostas muito longas
            temperature=0.7,  # Reduzido para respostas mais consistentes
            k=0,  # Não utiliza amostragem (para respostas mais determinísticas)
            p=0.75  # Controla a diversificação das respostas
        )
        
        # Gera a explicação
        explanation = response.generations[0].text.strip()
        return jsonify({'explanation': explanation})
    
    except Exception as e:
        return jsonify({'error': f'Erro ao gerar explicação: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

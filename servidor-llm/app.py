import cohere
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Chave de API da Cohere
co = cohere.Client('')

@app.route('/explain', methods=['POST'])
def explain_text():
    data = request.get_json()
    selected_text = data['text']
    
    # Geração de explicação com base nos critérios
    prompt = f"""
    Analise o seguinte trecho de uma política de privacidade: "{selected_text}".
    Explique de forma clara e acessível, evitando termos técnicos complicados. Use uma linguagem simples, como se estivesse explicando para alguém sem conhecimento técnico. Para cada um dos seguintes aspectos, dê uma explicação fácil de entender:
    1. O que é coletado? (Explique quais informações a empresa pega sobre o usuário.)
    2. Como os dados são tratados? (Explique o que a empresa faz com os dados do usuário.)
    3. Como a empresa pode usar os dados coletados? (Explique para que os dados podem ser usados.)
    4. As informações podem ser compartilhadas ou vendidas para terceiros? (Explique se os dados do usuário são passados para outras empresas.)
    5. Como os dados são armazenados? (Explique como e onde os dados ficam guardados.)
    6. O fornecimento dos dados é voluntário ou obrigatório? Quais as consequências da recusa? (Explique se o usuário é obrigado a dar os dados e o que acontece se ele não quiser.)
    7. Quais medidas garantem a proteção dos dados? (Explique como a empresa protege os dados, sem usar palavras técnicas.)
    Resuma cada ponto em no máximo 2 frases simples e diretas.
    """
    try:
        # Chamada à API da Cohere
        response = co.generate(
            model='command-nightly',
            prompt=prompt,
            max_tokens=600,  # Ajustado para evitar explicações muito longas
            temperature=0.7  # Reduzido para maior consistência na resposta
        )
        
        explanation = response.generations[0].text.strip()
        return jsonify({'explanation': explanation})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

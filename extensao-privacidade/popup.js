document.addEventListener('DOMContentLoaded', () => {
    const explanationDiv = document.getElementById('explanation');
    const themeToggleButton = document.querySelector('.theme-toggle');
    const body = document.body;

    // Função para alternar entre tema claro e escuro
    function toggleTheme() {
        if (body.classList.contains('dark')) {
            body.classList.remove('dark');
            body.classList.add('light');
            explanationDiv.style.backgroundColor = "#ffffff"; 
            explanationDiv.style.color = "#333333"; 
            themeToggleButton.textContent = '🌞'; 
        } else {
            body.classList.remove('light');
            body.classList.add('dark');
            explanationDiv.style.backgroundColor = "#1b1033"; 
            explanationDiv.style.color = "#ffffff"; 
            themeToggleButton.textContent = '🌙'; 
        }
    }

    // Adiciona o evento de clique ao botão de alternância de tema
    themeToggleButton.addEventListener('click', toggleTheme);

    // Função para mostrar a explicação
    function showExplanation(text) {
        explanationDiv.textContent = text;
        explanationDiv.style.display = 'block';
    }

    // Carrega a explicação automaticamente ao abrir o popup
    function captureSelectionAndExplain() {
        browser.tabs.executeScript({
            code: "window.getSelection().toString();"
        }).then(selection => {
            const selectedText = selection[0].trim();
            if (selectedText) {
                fetch('http://localhost:5000/explain', { // URL da API
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ text: selectedText })
                })
                .then(response => response.json())
                .then(data => {
                    showExplanation(data.explanation);
                })
                .catch(error => {
                    showExplanation("Erro ao gerar explicação. Tente novamente.");
                    console.error("Erro ao gerar explicação:", error);
                });
            } else {
                showExplanation("Selecione um trecho para obter uma explicação.");
            }
        });
    }

    captureSelectionAndExplain();
});

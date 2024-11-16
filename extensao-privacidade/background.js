chrome.runtime.onInstalled.addListener(() => {
});

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.text) {
    fetch('http://localhost:5000/explain', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ text: request.text })
    })
      .then(response => response.json())
      .then(data => {
        const explanation = data.explanation;

        // Envia a explicação de volta para o popup.js
        sendResponse({ explanation });
      })
      .catch(error => {
        console.error("Erro ao gerar explicação:", error);
        sendResponse({ explanation: "Erro ao gerar explicação. Tente novamente." });
      });

    // Permite resposta assíncrona
    return true;
  }
});

// script.js

function guess(userGuess) {
    fetch('/flip', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ guess: userGuess })
    })
      .then(response => response.json())
      .then(data => {
        document.getElementById('result').innerText = data.message;
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
  
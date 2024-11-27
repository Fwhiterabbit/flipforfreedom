from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/flip', methods=['POST'])
def flip():
    data = request.json
    user_guess = data['guess']
    outcome = random.choice(['Heads', 'Tails'])
    
    if user_guess == outcome:
        message = f"You guessed {user_guess}. It's {outcome}. You win!"
    else:
        message = f"You guessed {user_guess}. It's {outcome}. You lose!"
    
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(debug=True)

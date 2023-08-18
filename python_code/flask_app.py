from flask import Flask, jsonify
import random

app = Flask(__name__)

# List of inspirational quotes
quotes = [
    "The only way to achieve the impossible is to believe it is possible.",
    "Don't watch the clock; do what it does. Keep going.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Your time is limited, don't waste it living someone else's life.",
]

@app.route('/quote')
def get_quote():
    quote = random.choice(quotes)
    return jsonify({'quote': quote})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

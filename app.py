from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# In-memory database of quotes
quotes = [
    {"id": 1, "quote": "The only limit to our realization of tomorrow is our doubts of today.", "author": "Franklin D. Roosevelt"},
    {"id": 2, "quote": "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.", "author": "Buddha"},
    {"id": 3, "quote": "The purpose of our lives is to be happy.", "author": "Dalai Lama"}
]

# Routes
@app.route('/')
def home():
    return "Welcome to the Quotes API!"

# Get all quotes
@app.route('/quotes', methods=['GET'])
def get_quotes():
    return jsonify(quotes)

# Get a random quote
@app.route('/quotes/random', methods=['GET'])
def get_random_quote():
    import random
    quote = random.choice(quotes)
    return jsonify(quote)

# Get a quote by ID
@app.route('/quotes/<int:quote_id>', methods=['GET'])
def get_quote_by_id(quote_id):
    quote = next((q for q in quotes if q['id'] == quote_id), None)
    if quote:
        return jsonify(quote)
    return jsonify({"error": "Quote not found"}), 404

# Add a new quote
@app.route('/quotes', methods=['POST'])
def add_quote():
    data = request.get_json()
    if "quote" in data and "author" in data:
        new_quote = {
            "id": quotes[-1]['id'] + 1 if quotes else 1,
            "quote": data["quote"],
            "author": data["author"]
        }
        quotes.append(new_quote)
        return jsonify(new_quote), 201
    return jsonify({"error": "Invalid data"}), 400

# Delete a quote
@app.route('/quotes/<int:quote_id>', methods=['DELETE'])
def delete_quote(quote_id):
    global quotes
    quotes = [q for q in quotes if q['id'] != quote_id]
    return jsonify({"message": "Quote deleted"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

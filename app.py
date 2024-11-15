from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"student_number": "200603533"})


@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse request from Dialogflow
    req = request.get_json(silent=True, force=True)
    intent_name = req.get('queryResult').get('intent').get('displayName')

    # Basic example response based on intent
    if intent_name == 'Favorite Dish':
        response_text = "One of my favorite dishes is Butter Paneer! Rich, creamy, and full of spices."
    else:
        response_text = "I'm not sure about that. Can you ask me something else?"

    # Return the response as JSON
    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(debug=True)
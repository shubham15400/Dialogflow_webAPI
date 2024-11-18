from flask import Flask, request, jsonify
import random

app = Flask(__name__)

recipes_suggestion = {
    "Butter Paneer": "A rich and creamy curry made with tomatoes, butter, and chicken.",
    "Daal": "A healthy soup with lentils, turmeric, and ginger for a nutritious meal.",
    "Chana Masala": "A quick stir-fry with chickpeas, and garam masala."
}

recipes = {
    "Butter Paneer": "You will need Paneer, Butter or cream, onion and tomato. For spices you will need chilli powder, turmeric powder, cumin-corriender powder, bay leaf, pepper and cumin"
    ,"Daal": "You'll need lentil of your choice, oil(any), onion and tomato. For spices you will need cumin, chilli powder, turmeric powder, cumin-corriander powder, garam masala, asofoetida, whole dried red chilli"
    ,"Chana Masala": "You'll need Chole Chana lentil, oil, onion, tomato. For the spices you will need cumin, chilli powder, turmeric powder, cumin-corriander powder, bay leaf, garam masala."
}

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
    elif intent_name == 'Recipe_Suggestion':
        dish_name = random.choice(list(recipes_suggestion.keys()))
        response_text = f"Here is a recipe for {dish_name}: {recipes_suggestion[dish_name]}"
    else:
        response_text = "I'm not sure about that. Can you ask me something else?"

    # Return the response as JSON
    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(debug=True)
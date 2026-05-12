import json
from scorer import calculate_score

# Load intents
with open("intents.json", "r") as file:
    intents = json.load(file)


def generate_response(user_input):
    user_input = user_input.lower()

    best_match = None
    highest_score = 0

    for intent in intents["intents"]:
        score = calculate_score(user_input, intent["patterns"])

        if score > highest_score:
            highest_score = score
            best_match = intent

    if best_match:
        return best_match["responses"][0]

    return "I'm still learning. Could you rephrase that?"

import spacy
import random

def chatbot_response(user_input):
    """Generate a response to the user's input."""
    responses = {
        "greet": [
            "Hello! How can I help you today?",
            "Hi there! What brings you here?",
            "Hey! How can I assist you?"
        ],
        "bye": [
            "Goodbye! Have a great day!",
            "See you later!",
            "Take care and stay safe!"
        ],
        "help": [
            "I'm here to assist you. Feel free to ask any questions!",
            "Sure, let me know how I can help.",
            "Ask me anything, and I'll do my best to assist."
        ],
        "weather": [
            "The weather looks great today!",
            "It's sunny and bright outside.",
            "Looks like it might rain later."
        ],
        "joke": [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats.",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ],
        "thanks": [
            "You're welcome! Happy to help.",
            "No problem at all!",
            "Anytime! Feel free to ask if you need more help."
        ],
        "fallback": [
            "I'm not sure I understand. Could you rephrase?",
            "Sorry, I didn't get that. Can you clarify?",
            "Hmm, I don't have an answer for that right now."
        ]
    }

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(user_input.lower())

    if any(token.lemma_ in ["hello", "hi", "hey"] for token in doc):
        return random.choice(responses["greet"])
    elif any(token.lemma_ in ["bye", "goodbye", "see"] for token in doc):
        return random.choice(responses["bye"])
    elif any(token.lemma_ in ["help", "assist", "support"] for token in doc):
        return random.choice(responses["help"])
    elif any(token.lemma_ in ["weather", "rain", "sunny"] for token in doc):
        return random.choice(responses["weather"])
    elif any(token.lemma_ in ["joke", "funny", "laugh"] for token in doc):
        return random.choice(responses["joke"])
    elif any(token.lemma_ in ["thanks", "thank"] for token in doc):
        return random.choice(responses["thanks"])
    else:
        return random.choice(responses["fallback"])

def main():
    print("Chatbot: Hello! Type 'bye' to exit the chat.")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()

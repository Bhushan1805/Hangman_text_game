# Rule-Based Chatbot in Python

def get_reply(user_input):
    """Returns a chatbot reply based on keyword matching."""
    
    text = user_input.lower().strip()

    # Greeting rules
    if any(word in text for word in ["hello", "hi", "hey", "howdy"]):
        return "Hi there! How can I help you?"

    # How are you
    elif any(phrase in text for phrase in ["how are you", "how r you", "how do you do"]):
        return "I'm fine, thanks for asking! How about you?"

    # Name
    elif any(phrase in text for phrase in ["your name", "who are you"]):
        return "I'm ChatBot, your friendly rule-based assistant!"

    # Joke
    elif any(word in text for word in ["joke", "funny", "laugh"]):
        return "Why don't scientists trust atoms? Because they make up everything!"

    # Help / features
    elif any(word in text for word in ["help", "what can you do"]):
        return "I can respond to greetings, answer how I'm doing, tell jokes, and say goodbye!"

    # Thanks
    elif any(word in text for word in ["thanks", "thank you", "thx"]):
        return "You're welcome!"

    # Goodbye
    elif any(word in text for word in ["bye", "goodbye", "see you", "exit", "quit"]):
        return "Goodbye! Have a great day!"

    # Default fallback
    else:
        return "I didn't understand that. Try: hello, how are you, tell me a joke, or bye."


def chatbot():
    """Main loop that runs the chatbot."""
    print("ChatBot: Hello! I'm your rule-based chatbot.")
    print("ChatBot: (Type 'bye' or 'quit' to exit)\n")

    while True:
        user_input = input("You: ")

        if not user_input.strip():
            continue  # Skip empty input

        reply = get_reply(user_input)
        print(f"ChatBot: {reply}\n")

        # Stop loop if user says goodbye
        if any(word in user_input.lower() for word in ["bye", "goodbye", "quit", "exit"]):
            break


# Run the chatbot
chatbot()
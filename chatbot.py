
def chatbot():
    responses = {
        "hello": "Hi!",
        "hi": "Hello!",
        "how are you": "I'm fine, thanks!",
        "bye": "Goodbye!"
    }

    print("Chatbot is ready! (type 'bye' to exit)")

    while True:
        user_input = input("You: ").lower().strip()
        if user_input in responses:
            print("Bot:", responses[user_input])
            if user_input == "bye":
                break
        else:
            print("Bot: Sorry, I don't understand.")

chatbot()

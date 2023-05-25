def greet():
    print("Chatbot: Welcome! How can I assist you today?")


def farewell():
    print("Chatbot: Thank you for contacting us. Have a great day!")


def process_user_input(user_input):
    if "order" in user_input:
        print("Chatbot: Sure, I can help you with placing an order. Please provide me with your details.")
        # Logic for order processing
    elif "payment" in user_input:
        print("Chatbot: For payment-related inquiries, please contact our customer support at support@example.com.")
    elif "track" in user_input:
        print("Chatbot: To track your order, please enter your order number.")
        # Logic for order tracking
    elif "cancel" in user_input:
        print("Chatbot: To cancel an order, please provide your order number.")
        # Logic for order cancellation
    elif "hello" in user_input or "hi" in user_input:
        print("Chatbot: Hello! How can I assist you?")
    elif "bye" in user_input or "goodbye" in user_input:
        return False
    else:
        print("Chatbot: I'm sorry, but I didn't understand. Could you please rephrase or ask a different question?")

    return True


def start_chat():
    greet()

    chatting = True
    while chatting:
        user_input = input("You: ")
        chatting = process_user_input(user_input)

    farewell()


# Start the chatbot
start_chat()

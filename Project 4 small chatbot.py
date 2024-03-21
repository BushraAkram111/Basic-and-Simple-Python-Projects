import random

def chatbot(message):
    """This function returns a response from the chatbot."""
    responses = ["Hi there!", "How can I help you?", "What's up?", "I'm doing well, thanks for asking!"]
    return random.choice(responses)

def main():
    """This function is the main entry point for the chatbot."""
    message = input("What would you like to say to the chatbot? ")
    response = chatbot(message)
    print(response)

if __name__ == "__main__":
    main()
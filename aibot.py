import nltk
nltk.download('punkt_tab')

# chatbot.py

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data (only run once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

# Preprocessing function
def preprocess(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered = [word for word in tokens if word.isalnum() and word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word) for word in filtered]
    return lemmatized

# Response rules
responses = {
    "hello": "Hi there! How can I assist you?",
    "hi": "Hello! What can I do for you?",
    "your name": "I'm a chatbot built using Python and NLTK!",
    "how are you": "I'm just code, but thanks for asking!",
    "bye": "Goodbye! Have a nice day.",
    "help": "Sure! I can help you with basic queries. Try asking 'your name', 'how are you', or say 'bye'.",
    "who is kalyani friend?":"he is sridhar a best friend of her",
    "who made you?":"i was created by kalyani"
}

# Matching logic
def get_response(user_input):
    processed_input = preprocess(user_input)
    for key in responses:
        key_words = preprocess(key)
        if any(word in processed_input for word in key_words):
            return responses[key]
    return "Sorry, I am still developing,not in that level yet."

# Chat loop
def chat():
    print("Chatbot: Hello! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        reply = get_response(user_input)
        print("Chatbot:", reply)

# Run the chatbot
if __name__ == "__main__":
    chat()

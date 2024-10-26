import openai
import os

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot_response(message):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a friendly and knowledgeable medical assistant helping with long-term condition reviews in the UK. You cover blood pressure, diabetes, and cholesterol management according to NICE and Bradford guidelines."},
            {"role": "user", "content": message}
        ]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    print("Welcome to the LTC-Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Bot:", response)

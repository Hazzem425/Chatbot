import openai


api_key = "API key"

def chat_with_gpt(prompt):

    client = openai.OpenAI(api_key=api_key) 

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    print("Chatbot is ready! Type 'exit' to stop.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break

        response = chat_with_gpt(user_input)
        print("Chatbot:", response)

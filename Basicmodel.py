import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

def chat_with_openai():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    print("Chat with the assistant (type 'exit' to stop):")
    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            break

        messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        assistant_response = response['choices'][0]['message']['content']
        print(f"Assistant: {assistant_response}")

        messages.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    chat_with_openai()

from openai import OpenAI

def main(): 
    print("Welcome to your personal assistant")
    
    while True:
        user_input = input("\nYou: \n")
        
        if user_input.lower() == 'quit':
            break
        
        try:
            print("\nChat GPT: \n")
            client = OpenAI()

            stream = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}],
                stream=True,
            )
            for chunk in stream:
                print(chunk.choices[0].delta.content or "", end="")
        except Exception as e:
            print("An Error occured: ", e)
            
if __name__ == '__main__':
    main()
import sys

def get_response(user_input):
    # Convert input to lowercase to make matching case-insensitive
    user_input = user_input.lower().strip()

    # Define simple rule-based responses
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! I am a simple rule-based AI. How can I help you today?"
        
    elif "your name" in user_input or "who are you" in user_input:
        return "I am a simple virtual assistant chatbot created for my CodSoft internship."
        
    elif "help" in user_input:
        return "Sure! I can answer basic questions. Try asking about my purpose or how I work."
        
    elif "how work" in user_input or "how do you work" in user_input:
        return "I process your inputs using predefined rules and match them using basic text logic!"
        
    elif "weather" in user_input:
        return "I don't have real-time internet access, but I hope it's sunny wherever you are!"
        
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day ahead."
        
    else:
        return "I'm sorry, I don't quite understand that. Could you try phrasing it differently?"

def main():
    print("==================================================")
    print("     🤖 WELCOME TO THE RULE-BASED CHATBOT 🤖     ")
    print("         (Type 'bye' or 'exit' to quit)         ")
    print("==================================================")
    
    while True:
        try:
            user_input = input("\nYou: ")
            
            # Check for termination keywords
            if user_input.lower().strip() in ['bye', 'exit']:
                print(f"Bot: {get_response(user_input)}")
                break
                
            response = get_response(user_input)
            print(f"Bot: {response}")
            
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()hhii
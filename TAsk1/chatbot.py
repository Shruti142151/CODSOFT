# CodSoft Internship - Task 1
# Chatbot created by Shruti Kumari (June Batch B35)

print("Bot: Hey there! I'm CodSoftBot. You can talk to me 😊")

while True:
    message = input("You: ").lower()  # user input in lowercase for easier matching

    if "hello" in message or "hi" in message:
        print("Bot: Hello! How are you doing?")
    
    elif "how are you" in message:
        print("Bot: I'm good, just running in this terminal! 😄")
    
    elif "your name" in message or "who are you" in message:
        print("Bot: I'm CodSoftBot, created for the AI Internship Task 1.")
    
    elif "help" in message or "what can you do" in message:
        print("Bot: I can answer simple questions. Try saying 'hello', 'bye', or ask my name.")
    
    elif "bye" in message or "exit" in message or "see you" in message:
        print("Bot: Okay, bye! Have a great day ahead. 👋")
        break
    
    else:
        print("Bot: Hmm, I didn't get that. Maybe try asking something else?")

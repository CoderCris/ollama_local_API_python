from ollama_interactor import OllamaInteractor

if __name__ == "__main__":
    # Define the Ollama command
    ollama_command = "ollama run phi3"
    
    print("Running the Ollama command: " + ollama_command)

    # Create an instance of the OllamaInteractor
    interactor = OllamaInteractor(ollama_command)
    
    try:
        while True:
            # Get input from the user
            user_input = input("Enter your message: ")
            
            if user_input.lower() == "exit":
                break
            
            # Send the message to Ollama and get the response
            response = interactor.send_message(user_input)
            
            # Print the response
            print("Ollama response:", response)
    finally:
        # Close the interactor
        interactor.close()

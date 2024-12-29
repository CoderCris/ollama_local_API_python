from ollama_interactor import OllamaInteractor
from ollama_interactor_2 import interact_with_powershell_script

def ollama_interactor_1(command):
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

def ollama_interactor_2():
     return interact_with_powershell_script()
     
if __name__ == "__main__":
     print("Script initialized")
     ollama_interactor_2()
     print("End of script")
    # Define the Ollama command
 

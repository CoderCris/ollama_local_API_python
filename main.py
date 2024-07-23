import subprocess

def run_ollama(command):
    try:
        # Run the Ollama command
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        
        # Capture and return the output
        return result.stdout
    
    except subprocess.CalledProcessError as e:
        # Handle errors in the command execution
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Define the Ollama command
    ollama_command = "ollama run phi3"

    # Run the command and capture the output
    output = run_ollama(ollama_command)

    if output:
        # Process the output as needed
        print("Ollama output:")
        print(output)

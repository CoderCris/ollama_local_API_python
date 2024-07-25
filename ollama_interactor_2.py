import subprocess

# Function to interact with the PowerShell script
def interact_with_powershell_script():
    # Start the PowerShell process
    process = subprocess.Popen(
        ["powershell.exe", "ollama", "run", "phi3"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Interact with the PowerShell script
    try:
        # Read initial output (welcome message)
        output = process.stdout.readline().strip()
        print(output)

        while True:
            # Get user input
            user_input = input("You: ")
            
            if user_input.lower() == 'exit':
                # Send 'exit' command to PowerShell script
                process.stdin.write('exit\n')
                process.stdin.flush()
                break
            
            # Send user input to PowerShell script
            process.stdin.write(f"{user_input}\n")
            process.stdin.flush()
            
            # Read response from PowerShell script
            output = process.stdout.readline().strip()
            print(output)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        return True

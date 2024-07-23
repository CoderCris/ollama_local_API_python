
import subprocess



class OllamaInteractor:
    def __init__(self, command):
        self.process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    def send_message(self, message):
        # Write the message to the process's stdin
        self.process.stdin.write(message + "\n")
        self.process.stdin.flush()
        
        # Read the response from stdout
        response = self.process.stdout.readline()
        return response.strip()
    
    def close(self):
        # Close the process's stdin to signal the end of input
        self.process.stdin.close()
        # Wait for the process to finish
        self.process.wait()
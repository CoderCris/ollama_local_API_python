import ollama_interactor_2 as oi2

def ollama_init():
  return None

def main():
  if oi2.check_ollama_windows():
    print("Ollama service is running")
  else:
    print("Ollama service is not running")
    return None
  return None


if __name__ == "__main__":
  main()
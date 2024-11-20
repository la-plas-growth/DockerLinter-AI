import os
from docker_linter import DockerLinter

# Configurazione
BEST_PRACTICES_URL = "https://docs.docker.com/build/building/best-practices/"
DOCKERFILE_PATH = "Dockerfile"

def main():
    # Leggi la chiave API dall'ambiente
    API_KEY = os.getenv("OPENAI_API_KEY")
    if not API_KEY:
        raise ValueError("OPENAI_API_KEY non è impostata come variabile di ambiente.")

    linter = DockerLinter(api_key=API_KEY, url=BEST_PRACTICES_URL)
    
    # Scarica le best practices
    linter.fetch_best_practices()
    
    # Leggi il Dockerfile
    dockerfile_content = linter.read_dockerfile(DOCKERFILE_PATH)
    
    # Analizza il Dockerfile
    analysis = linter.analyze_dockerfile(dockerfile_content)
    
    # Mostra il risultato
    print("Risultato dell'analisi del Dockerfile:")
    print(analysis)

if __name__ == "__main__":
    main()
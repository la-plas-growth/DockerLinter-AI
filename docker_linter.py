import requests
from bs4 import BeautifulSoup
from openai import OpenAI

class DockerLinter:
    def __init__(self, api_key, url):
        self.api_key = api_key
        self.url = url
        self.instructions = None
        self.client = OpenAI(api_key=api_key)
    
    def fetch_best_practices(self):
        """Scarica il contenuto di un URL e lo salva come testo."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            self.instructions = soup.get_text()
            print("Best practices scaricate con successo.")
        except Exception as e:
            raise RuntimeError(f"Errore durante il download delle best practices: {e}")
    
    def read_dockerfile(self, file_path):
        """Legge il contenuto di un Dockerfile da un file."""
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            raise RuntimeError(f"Dockerfile non trovato: {file_path}")
        except Exception as e:
            raise RuntimeError(f"Errore durante la lettura del Dockerfile: {e}")
    
    def analyze_dockerfile(self, dockerfile_content):
        """Invia il Dockerfile all'API OpenAI per l'analisi."""
        if not self.instructions:
            raise RuntimeError("Le istruzioni non sono state caricate. Usa fetch_best_practices prima.")
            
        try:
            completion = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": f"You are a docker linter. Use the following best practices for guidance: {self.instructions}"
                    },
                    {
                        "role": "user",
                        "content": f"Here is my Dockerfile to analyze:\n\n{dockerfile_content}"
                    }
                ]
            )
            return completion.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"Errore durante l'interazione con l'API OpenAI: {e}")
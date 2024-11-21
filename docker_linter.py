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
        """Downloads URL content and saves it as text"""
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            self.instructions = soup.get_text()
        except Exception as e:
            raise RuntimeError(f"Error while downloading best practices content: {e}")
    
    def read_dockerfile(self, file_path):
        """Read Dockerfile content from file"""
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            raise RuntimeError(f"Dockerfile not found: {file_path}")
        except Exception as e:
            raise RuntimeError(f"Error during Dockerfile reading: {e}")
    
    def analyze_dockerfile(self, dockerfile_content):
        """Send Dockerfile to API OpenAI for Analysis."""
        if not self.instructions:
            raise RuntimeError("Instructions are not been loaded. Use fetch_best_practices first.")

        try:
            completion = self.client.chat.completions.create(
                model="gpt-4o",
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
            raise RuntimeError(f"Error during API OpenAI iteration: {e}")
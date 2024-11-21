import os
import argparse
from docker_linter import DockerLinter

def parse_args():
    """Handles CLI arguments."""
    parser = argparse.ArgumentParser(description="Dockerfile Linter")
    parser.add_argument("dockerfile", help="Path to the Dockerfile to analyze")
    return parser.parse_args()

def main():

    # Read Enviroment Variable
    BEST_PRACTICES_URL = os.getenv("BEST_PRACTICES_URL")
    if not BEST_PRACTICES_URL:
        BEST_PRACTICES_URL = "https://docs.docker.com/build/building/best-practices/"

    API_KEY = os.getenv("OPENAI_API_KEY")
    if not API_KEY:
        raise ValueError("OPENAI_API_KEY not set as enviroment variable")

    linter = DockerLinter(api_key=API_KEY, url=BEST_PRACTICES_URL)
    
    # Download best practices
    linter.fetch_best_practices()
    
    # Parse Args
    args = parse_args()

    DOCKERFILE_PATH = args.dockerfile

    # Read Dockerfile
    dockerfile_content = linter.read_dockerfile(DOCKERFILE_PATH)
        
    # Analyze Dockerfile
    analysis = linter.analyze_dockerfile(dockerfile_content)
    
    # Show Results
    print("Here is the Analysis")
    print("-----------------------")
    print(analysis)

if __name__ == "__main__":
    main()
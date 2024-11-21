
# Dockerfile Linter

Dockerfile Linter is a tool designed to analyze Dockerfiles and verify their compliance with best practices. It leverages the OpenAI API to compare the Dockerfile content against guidelines downloaded from a specified URL.

## Features
- Downloads best practices guidelines from a URL (default: [Docker Best Practices](https://docs.docker.com/build/building/best-practices/)).
- Analyzes a Dockerfile and provides suggestions or warnings for any detected issues.
- Uses the OpenAI API to ensure accurate analysis.

## Installation
1. Clone the repository:
    ```bash
    git clone <repository URL>
    cd <repository name>
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Make sure you have an OpenAI API key and set it as an environment variable:
    ```bash
    export OPENAI_API_KEY="your_api_key"
    ```

## Usage
### Command Line
1. Run the script by specifying the path to the Dockerfile you want to analyze:
    ```bash
    python main.py /path/to/Dockerfile
    ```

2. The analysis results will be displayed in the terminal.

### Using Docker Container
You can also run the linter directly from a Docker container:

```bash
docker run   -e OPENAI_API_KEY="your_openai_api_key"   -v $(pwd):/app/Dockerfile   ghcr.io/la-plas-growth/dockerlinter-ai:4273633ddd1dd732d227a78d967745391a09291b   /app/Dockerfile
```

Replace `your_openai_api_key` with your actual OpenAI API key. This example mounts a local `Dockerfile` to the container and passes it for analysis.

## Environment Variables
- `OPENAI_API_KEY`: Required for authentication with OpenAI API.
- `BEST_PRACTICES_URL`: Optional. Specifies the URL for downloading Docker best practices. The default value is:
    ```
    BEST_PRACTICES_URL = "https://docs.docker.com/build/building/best-practices/"
    ```

## Main Files
- **`docker_linter.py`**: Contains the main logic for downloading best practices, reading the Dockerfile, and analyzing it using OpenAI.
- **`main.py`**: Handles command-line input and coordinates the workflow.
- **`requirements.txt`**: A list of required dependencies.
- **`Dockerfile`**: (Optional) Defines the environment to run the linter in a container.

## Dependencies
- `dockerfile-parse==2.0.1`
- `markdown-it-py==3.0.0`
- `openai==1.55.0`
- `beautifulsoup4==4.12.3`
- `requests==2.32.3`

## Notes
Ensure you have an active internet connection to download best practices and interact with the OpenAI API.

## Contributions
Contributions are welcome! Feel free to open a pull request or report issues.

## License
This project is released under the MIT License.

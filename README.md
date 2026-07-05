# DevMentor AI 🧠💻

DevMentor AI is your memory-powered CLI agent designed to assist developers directly from the terminal. By integrating long-term context memory (via a Hindsight-inspired architecture) and blazing-fast AI inference (via Groq), DevMentor acts as an intelligent pair-programmer that actually remembers your stack, your bugs, and your project nuances over time.

## Features
- **Hindsight Memory**: Learns and remembers your specific context. No more repeating yourself to the AI!
- **Fast Responses**: Powered by Groq for ultra-low latency AI interactions.
- **Sleek CLI Interface**: Built with Typer and Rich for a beautiful, colorful, and highly readable terminal experience.
- **Local Persistence**: Stores projects, bugs, and memories in a local SQLite database for privacy and speed.

## Prerequisites
- Python 3.8+
- Groq API Key (for LLM capabilities)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shivji2138/devmentor-ai.git
   cd devmentor-ai
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup:**
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

DevMentor provides an intuitive command-line interface.

### Chat with DevMentor
Ask a question, and DevMentor will leverage its memory context to give you a personalized, relevant answer:
```bash
python main.py chat "How do I connect my SQLite database in Python again?"
```

### Remember Context Manually
Manually feed DevMentor with specific context you want it to remember for future sessions:
```bash
python main.py remember "We are using Typer for the CLI and Rich for terminal formatting."
```

## Architecture overview
- `main.py`: Entry point that initializes the database and CLI application.
- `devmentor/cli.py`: Defines the CLI commands (`chat`, `remember`) using Typer and formats output with Rich.
- `devmentor/router.py`: Handles interactions with the Groq API for LLM reasoning.
- `devmentor/memory.py`: Manages the storage and retrieval of long-term context. 
- `devmentor/db.py`: Initializes the SQLite database schema for local persistence of projects, bugs, and generic memories.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue.

## License
MIT License

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from devmentor.cli import app
from devmentor.db import init_db

# Initialize database
init_db()

if __name__ == "__main__":
    app()

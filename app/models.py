import os
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv


# Load .env file
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


# Get API key
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise ValueError("ANTHROPIC_API_KEY not found in .env")


# Create Claude client
client = Anthropic(api_key=api_key)
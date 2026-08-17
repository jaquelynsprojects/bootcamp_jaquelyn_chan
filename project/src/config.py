import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

def load_env():
    """Load environment variables from .env file."""
    load_dotenv()

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    """Retrieve an environment variable by name."""
    load_env()
    return os.getenv(name, default)

if __name__ == "__main__":
    load_env()
    print("PROJECT_ROOT:", PROJECT_ROOT)
    print("DATA_DIR:", DATA_DIR)
    print(f"API_KEY present: {get_key('API_KEY') is not None}")
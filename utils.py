import os
from dotenv import load_dotenv

def load_environment_variables() -> None:
    """
    Load environment variables from a .env file into the process environment.
    This should be called once at application startup.
    """
    load_dotenv()
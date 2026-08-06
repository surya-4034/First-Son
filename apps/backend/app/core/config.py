
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.0-flash")
TIMEOUT = int(os.getenv("TIMEOUT", "120"))
CORS_ORIGIN = os.getenv("CORS_ORIGIN", "*")
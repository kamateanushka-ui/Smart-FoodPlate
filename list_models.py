import os
import google.generativeai as genai
from dotenv import load_dotenv

# Path to the .env file in the Backend directory
dotenv_path = os.path.join(os.path.dirname(__file__), 'Backend', '.env')
load_dotenv(dotenv_path)

api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)

print("Listing all models:")
try:
    for m in genai.list_models():
        print(f"{m.name}")
except Exception as e:
    print(f"Error: {e}")

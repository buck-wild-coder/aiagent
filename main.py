import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("API Key not found")

client = genai.Client(api_key=api_key)

response = client.models.generate_content( model='gemini-2.5-flash', contents="hi, reply with minimal words.")
if response.usage_metadata is None:
    raise RuntimeError("An error was occured during the api call")
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
import os
from dotenv import load_dotenv
from google import genai

env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain Gen AI in exactly 50 words."
)

print(response.text)

usage = response.usage_metadata

print("\nToken Usage")
print("Prompt Tokens:", usage.prompt_token_count)
print("Response Tokens:", usage.candidates_token_count)
print("Total Tokens:", usage.total_token_count)

print("\nFull Usage Metadata:")
print(usage)
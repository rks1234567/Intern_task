import os
from dotenv import load_dotenv
from google import genai
class ArticleSummarizer:
    def __init__(self):
        load_dotenv()

        api_key = os.getenv(
            "GEMINI_API_KEY"
        )

        if not api_key:
            raise ValueError(
                "API Key Missing"
            )

        self.client = genai.Client(
            api_key=api_key
        )
    def summarize(self, article, length, style):
        prompt = f"""
Summarize the following article.

Length: {length}
Style: {style}

Article:
{article}
"""
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text
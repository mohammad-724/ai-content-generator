import os
from dotenv import load_dotenv
from openai import OpenAI


# --------------------------------------------------
# 1. Load environment variables from .env
# --------------------------------------------------
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY was not found in the .env file.")


# --------------------------------------------------
# 2. Create OpenAI client
# --------------------------------------------------
client = OpenAI(api_key=api_key)


# --------------------------------------------------
# 3. Get information from the user
# --------------------------------------------------
topic = input("Enter your topic: ")
content_type = input("Enter content type (blog/linkedin/instagram): ")
tone = input("Enter tone (professional/friendly/creative): ")
length = input("Enter length (short/medium/long): ")


# --------------------------------------------------
# 4. Create the AI prompt
# --------------------------------------------------
prompt = f"""
Create {content_type} content about the following topic:

Topic: {topic}

Tone: {tone}

Length: {length}

Requirements:
- Make the content clear and engaging.
- Use appropriate language for the selected content type.
- Keep the response focused on the topic.
"""


# --------------------------------------------------
# 5. Send the prompt to the AI
# --------------------------------------------------
response = client.responses.create(
    model="gpt-5.6-luna",
    input=prompt
)


# --------------------------------------------------
# 6. Display the result
# --------------------------------------------------
print("\n" + "=" * 60)
print("GENERATED CONTENT")
print("=" * 60)
print(response.output_text)
print("=" * 60)
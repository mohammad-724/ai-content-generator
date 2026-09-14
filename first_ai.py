import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from the .env file
load_dotenv()

# Get the API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# Stop the program if the API key was not found
if not api_key:
    raise ValueError("OPENAI_API_KEY was not found in the .env file.")

# Create the OpenAI client
client = OpenAI(api_key=api_key)

# Ask the user for a topic
topic = input("Enter a topic: ")

# Send the prompt to the AI model
response = client.responses.create(
    model="gpt-5.6-luna",
    input=f"Write a short paragraph about {topic}."
)

# Display the generated response
print("\nGenerated Content:\n")
print(response.output_text)
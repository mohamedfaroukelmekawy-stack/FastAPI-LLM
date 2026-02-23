from dotenv import load_dotenv
import os
import cohere

# load environment variables
load_dotenv()

# read API key safely
co = cohere.Client(os.getenv("COHERE_API_KEY"))


async def generate_embedding(text: str):
    response = co.embed(
        texts=[text],
        model="embed-english-v3.0",
        input_type="search_document"
    )

    return response.embeddings[0]
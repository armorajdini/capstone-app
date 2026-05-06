import os
import litellm
from dotenv import load_dotenv

def test_connection():
    load_dotenv()
    
    model = os.getenv("LLM_MODEL", "openai/gpt-3.5-turbo")
    api_key = os.getenv("LLM_API_KEY")
    base_url = os.getenv("LLM_BASE_URL")
    
    print(f"Testing connection to {model} via {base_url}...")
    
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        print("Error: LLM_API_KEY is not set in .env")
        return

    try:
        response = litellm.completion(
            model=model,
            messages=[{"role": "user", "content": "Say hello!"}],
            api_key=api_key,
            base_url=base_url
        )
        print("Success!")
        print(f"Response: {response.choices[0].message.content}")
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    test_connection()

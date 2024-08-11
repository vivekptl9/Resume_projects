import google.generativeai as genai
import os

def use_gemini():
    try:
        # Configure the Gemini API
        api_key = os.getenv('GEMINI_API_KEY')
        genai.configure(api_key=api_key)

        # Choose a Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Use the model
        # ...

    except AttributeError as e:
        print(f"Error: {e}")
        # Handle the error, e.g., retry, log, or provide alternative actions


if __name__ == "__main__":
    use_gemini()

from google import genai

# replace with your API key
client = genai.Client(api_key="AIzaSyB8SF_Ks-kd19k2LOY40X-U4H4iR4gssak")


def summarize_text(text: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"Summarize this in 3 lines:\n{text}",
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

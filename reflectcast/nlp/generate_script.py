import os
from dotenv import load_dotenv
from openai import OpenAI  # new import style for v1.0+

load_dotenv()  # loads .env variables

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise Exception("OPENAI_API_KEY environment variable not set")

client = OpenAI(api_key=OPENAI_API_KEY)  # instantiate the client with your key

def create_script(reflection: str, emotion: str) -> str:
    """
    Generates a soothing, poetic podcast script based on user's reflection and detected emotion.
    Uses OpenAI GPT API to generate fresh content every time.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a gentle, calming bedtime podcast writer."},
                {"role": "user", "content": (
                    f"The user shared this reflection about {emotion}:\n\"\"\"{reflection}\"\"\"\n\n"
                    "Write a soothing, poetic, and comforting bedtime podcast script that flows naturally.\n"
                    "Do NOT include the words 'intro', 'body', or 'outro' in the script.\n"
                    "Make the tone soft, empathetic, and reassuring, helping the listener relax and sleep peacefully."

                )}
            ],
            max_tokens=350,
            temperature=0.7,
            top_p=1,
        )
        script = response.choices[0].message.content.strip()
        return script

    except Exception as e:
        print(f"Error generating script: {e}")
        fallback = (
            "Tonight, let’s take a moment just for you.\n\n"
            "Breathe deeply, you are safe here.\n\n"
            "Rest well and know that tomorrow is a new day."
        )
        return fallback

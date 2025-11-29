import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

def analyze_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Ou "grok-beta" se API disponível
        messages=[{"role": "user", "content": f"Analise sentimento e riscos: {text}"}]
    )
    return response.choices[0].message.content
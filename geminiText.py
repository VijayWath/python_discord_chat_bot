import os
from dotenv import load_dotenv

async def geminiText(txt:str):
    import google.generativeai as genai
    load_dotenv()
    GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(txt)
    response.resolve()
    return response.text
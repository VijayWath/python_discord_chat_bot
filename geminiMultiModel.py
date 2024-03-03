from io import BytesIO
from PIL import Image
import os
from dotenv import load_dotenv
import requests

async def geminiMultiModel(txt:str,url):
    import google.generativeai as genai

    load_dotenv()

    GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro-vision')

    response = requests.get(url)
    image_data = BytesIO(response.content)
    img = Image.open(image_data)

    response = model.generate_content([txt,img])
    response.resolve()
    return response.text




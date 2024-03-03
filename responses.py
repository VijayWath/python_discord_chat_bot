import os
from dotenv import load_dotenv

from discord import Message

from geminiImage import geminiImage
from geminiText import geminiText
from geminiMultiModel import geminiMultiModel


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

async def get_response(message:Message) -> str:
    channel = str(message.channel)
    if 'Direct Message' in channel:
        isPrivat = True
    else :
        isPrivat = False

    if  message.content == '' and  message.attachments != []:
        for attachment in message.attachments:
            if attachment.content_type.startswith('image'):
                image_url = attachment.url
                print(image_url)
                try:
                    responseMessage =  await geminiImage(image_url)
                    response =responseMessage
                    await message.author.send(response) if isPrivat else await message.channel.send(response)
                except Exception as e:
                        print(e)

    
    elif message.attachments == [] and  message.content != '':
        lowered = message.content.lower()
        if lowered[0] == '?':
            lowered = lowered[1:]
            isPrivat = True
        try:
            responseMessage =  await geminiText(lowered)
            response =responseMessage
            await message.author.send(response) if isPrivat else await message.channel.send(response)
        except Exception as e:
            print(e)

    elif message.attachments != [] and  message.content != '':
        lowered = message.content.lower()
        if lowered[0] == '?':
            lowered = lowered[1:]
            isPrivat = True

        for attachment in message.attachments:
            if attachment.content_type.startswith('image'):
                image_url = attachment.url
                print(image_url)

        try:
            responseMessage =  await geminiMultiModel(lowered,image_url)
            response =responseMessage
            await message.author.send(response) if isPrivat else await message.channel.send(response)
        except Exception as e:
            print(e)
        

    # for attachment in message.attachments:
    #     if attachment.content_type.startswith('image'):
    #         image_url = attachment.url
    #         print(f"Image URL: {image_url}")
    #     response = requests.get(image_url)
    #     image_data = BytesIO(response.content)


    
    # if isPrivat := lowered[0] == '?':
    #     lowered = lowered[1:]

    # try:
    #     response ="done"
    #     await message.author.send(response) if isPrivat else await message.channel.send(response)
    # except Exception as e:
    #     print(e)
    # img = Image.open(image_data)

    
 


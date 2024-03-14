from discord import Message

async def sendResponse(text:str,isPrivat:bool,message:Message):
    await message.author.send(text) if isPrivat else await message.channel.send(text)

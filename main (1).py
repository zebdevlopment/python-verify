import discord, os, keep_alive, base64, time, asyncio, datetime, pytz

client = discord.Client()
token = os.getenv('TOKEN')
decodedBytes = base64.b64decode(token)
decodedStr = str(decodedBytes, "utf-8")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    channel = client.get_channel(908976236963966997)
    if message.author == client.user:
        return

    if message.content.startswith('Có') or message.content.startswith('có'):
        await message.delete()
        time.sleep(0.5)
        await channel.send(f'**{message.author}**```Đã trả lời "Có" \nID: {message.author.id}```')
        botMess = await message.channel.send('Câu trả lời của bạn đã được ghi lại')
        time.sleep(2)
        await botMess.delete()
    else:
        await message.delete()
        time.sleep(0.5)
        await channel.send(f'**{message.author}**```Đã trả lời "{message.content}" \nID: {message.author.id}```')
        botMess = await message.channel.send('Xin lỗi có vẻ như bạn không làm đúng những điều trên. ID và tên của bạn đã được lưu lại chúc bạn may mắn! Tạm biệt...')
        time.sleep(5)
        await botMess.delete() 




keep_alive.keep_alive()
client.run(decodedStr)
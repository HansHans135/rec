import discord
import os
from datetime import datetime,timezone,timedelta
client = discord.Client()

@client.event   
async def on_ready():
    print('機器人已啟動，目前使用的bot：',client.user)


@client.event
async def on_message(message):
    dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
    dt2 = dt1.astimezone(timezone(timedelta(hours=8)))
    now = dt2.strftime("%Y-%m-%d %H:%M:%S")
    if message.content == 'h!rec':
        if message.author.guild_permissions.manage_messages:
            filepath = f"data/{message.channel.id}.txt"
            if os.path.isfile(filepath):
                with open(f"data/{message.channel.id}.txt", 'a') as filt:
                    filt.write(f'開始時間:{now}\n頻道名稱:{message.channel.name}\n開始人:{message.author}\n以下為詳細的對話紀錄:\n\n\n')
                await message.channel.send('已開始錄製!!')
            await message.channel.send('已經在錄製!!')
                
    if message.content == 'h!recstop':
        if message.author.guild_permissions.manage_messages:
            with open(f"data/{message.channel.id}.txt", 'a') as filt:
                filt.write(f'\n\n結束人:{message.author}\n結束時間:{now}')
            await message.channel.send('已結束錄製!!', file=discord.File(f"data/{message.channel.id}.txt"))
            fileTest = f"data/{message.channel.id}.txt"
            os.remove(fileTest)
            
    filepath = f"data/{message.channel.id}.txt"
    if os.path.isfile(filepath):
        with open(f"data/{message.channel.id}.txt", 'a') as filt:
            filt.write(f'{now}|{message.author}:{message.content}\n')
        
client.run("owo") 

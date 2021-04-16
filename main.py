import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('botto hi'):
        await message.channel.send('Yo what\'s up!')
        await message.channel.send()

    if message.content.startswith('botto bye'):
        await message.channel.send('Later bitch')
    
    if message.content.startswith('botto winans'):
      embedVar = discord.Embed(title="Winans: the leader of the free world", description="programming legend", color=0x00ff00)
      embedVar.add_field(name="RISC-V", value="the best architecture", inline=False)
      embedVar.add_field(name="RV32I", value="the worlds greatest instruction set", inline=False)
      await message.channel.send(embed=embedVar)

my_secret = os.environ['TOKEN']
client.run(my_secret)
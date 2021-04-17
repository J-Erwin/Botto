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
        

    if message.content.startswith('botto bye'):
        await message.channel.send('Later bitch')
    
    if message.content.startswith('botto winans'):
      embedVar = discord.Embed(title="Winans: the leader of the free world", description="programming legend", color=0x00ff00)
      embedVar.add_field(name="RISC-V", value="the best architecture", inline=False)
      embedVar.add_field(name="RV32I", value="the worlds greatest instruction set", inline=False)
      await message.channel.send(embed=embedVar)

    if message.content.startswith('botto abel'):
      embedVar = discord.Embed(title="Abel Vega Arteaga", description="omfg he looooves CSGO skins, he used to have a knife that was worth 200 USD but he sold it for a VR. He is a legend.", color=0x00ffff)
      embedVar.add_field(name="Strengths", value="comedian, loyal, and the gays love him", inline=False)
      embedVar.add_field(name="Weaknesses", value="he has a crippling chicken nugget addiction", inline=False)
      await message.channel.send(embed=embedVar)

    if message.content.startswith('botto beto'):
      embedVar = discord.Embed(title="Adalberto Orozco", description="loyal friend, social chameleon, and athletic build (even tho he is not 6ft)", color=0x00ffff)
      embedVar.add_field(name="Strengths", value="loyal, sexy, and strong willed", inline=False)
      embedVar.add_field(name="Weaknesses", value="over commits on rocket league all the time", inline=False)
      await message.channel.send(embed=embedVar)

    if message.content.startswith('botto cynthia'):
      embedVar = discord.Embed(title="Cynthia Hernandez", description="strong female lead, do not fuck with her... Also a really great friend", color=0x00ffff)
      embedVar.add_field(name="Strengths", value="Financially independent, hard worker, and brilliant", inline=False)
      embedVar.add_field(name="Weaknesses", value="none", inline=False)
      await message.channel.send(embed=embedVar)

    if message.content.startswith('botto john'):
      embedVar = discord.Embed(title="John Erwin", description="default character name, average person, great troll", color=0x00ffff)
      embedVar.add_field(name="Strengths", value="he makes great coffee", inline=False)
      embedVar.add_field(name="Weaknesses", value="he is a little joker brained sometimes", inline=False)
      await message.channel.send(embed=embedVar)
    
    if message.content.startswith('botto jesus'):
      embedVar = discord.Embed(title="Jesus Lua ... of course", description="super brilliant mind, often underestimated, but don't sleep on him, he could take you any day.", color=0x00ffff)
      embedVar.add_field(name="Strengths", value="he is a genius... need I say more?", inline=False)
      embedVar.add_field(name="Weaknesses", value="sometimes his burps kill bystanders", inline=False)
      await message.channel.send(embed=embedVar)
    
    if message.content.startswith('botto andrew'):
      embedVar = discord.Embed(title="Andrew Westgate", description="coffee, beer, and music connoisseur.", color=0x00ffff)
      embedVar.add_field(name="Strengths", value="listening, performing, and learning new things", inline=False)
      embedVar.add_field(name="Weaknesses", value="sometimes he gets the coffee sweats bad", inline=False)
      await message.channel.send(embed=embedVar)

my_secret = os.environ['TOKEN']
client.run(my_secret)
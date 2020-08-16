# ID: 743570969557467186
# Token: NzQzNTcwOTY5NTU3NDY3MTg2.XzWmbg.8tTV2ZwoY_CkEmMNAyCAizvFvLY
# Permissions: 218310737
# https://discordapp.com/oauth2/authorize?client_id=743570969557467186&scope=bot&permissions=218310737
#!spam @user 10t(imes)
#!spam @user 10s(econds)
AccessToCommand = {"Wolf":int("298916633139740672"),"Deran":int("272404440538021889")}
import discord
import time
#from discord.ext import commands
#client = discord.Client()

#bot = commands.Bot(command_prefix='$')
from discord.ext import commands

client = commands.Bot(command_prefix='!')


@client.event #event decorator/wrapper
async def on_ready():
    print(f"We have logged in as {client.user}")



@client.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('{} just got slapped for {}'.format(slapped, reason))

@client.command()
async def spam(ctx, times=1, *members):
    memlist = []
    for i in members:
        memlist.append(i)
    spammed = ", ".join(memlist)
    if (ctx.channel.id == 743572322878750760):
        try:
            int(times)
            for i in range(times):
                await ctx.send("Get spammed: {0} number: {1}".format(spammed, i + 1))
            await ctx.send("Done spamming")
        except TypeError:
            await ctx.send("please enter a number")
    else:
        await ctx.send("Please enter this command in Joe's Channel")


@client.event
async def on_message(message):
    await client.process_commands(message)
    #print(message.content)






"""
@client.event
async def on_message(ctx, message):
    SpamList = []
    channel = client.get_channel(1664318768)
    print(f"{message.channel}: {message.author.id}: {message.author.name}: {message.content}:")
    #message.content.lower()
    if "!spam" in message.content.lower() and message.author.id in AccessToCommand.values(): #If the user enters the !spam command and the user
        await message.channel.send("Who would you like to spam?")
        x = message.guild.members
        for member in x:
            SpamList.append(member.name)
        SpamList.pop()
        msg = await ctx.send(str(SpamList).strip("[]"))
        await msg.add_reaction(":one:")

    #print(id(channel))
"""


client.run("NzQzNTcwOTY5NTU3NDY3MTg2.XzWmbg.8tTV2ZwoY_CkEmMNAyCAizvFvLY")

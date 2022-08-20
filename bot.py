import discord
from discord.ext import commands
import random

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True) #makes member join and member remove functions work

client = commands.Bot(command_prefix = "!", intents = intents, help_command=None)

@client.event
async def on_ready():
    print("Bot is ready")
    channel = client.get_channel({put channel id here})
    await channel.send("I am now online")
    

@client.event
async def on_member_join(member):
    print(f"{member} has joined a server")
    await member.send(f"Welcome to Marxie's Server")
    channel = client.get_channel({put channel id here})
    await channel.send(f"{member} has joined the server")

@client.event
async def on_member_remove(member):
    print(f"{member} has left a server")
    channel = client.get_channel({put channel id here})
    await channel.send(f"{member} has left the server")

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."]   
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")


@client.command(aliases=["commands"])
async def help(ctx):
    await ctx.send("Prefix: !\nCommands:\n!commands/!help - Displays this information\n!8ball - Roll the 8ball E.G: !8ball (insert question here)\n")

client.run("{put token here}")

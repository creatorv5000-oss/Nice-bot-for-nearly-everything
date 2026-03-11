import discord
from discord.ext import commands

# Bot Token
TOKEN = 'YOUR_BOT_TOKEN'

# Intent
intents = discord.Intents.default()
intents.message_content = True

# Creating a bot instance
bot = commands.Bot(command_prefix='!', intents=intents)

# Load cogs (if you have any)
# bot.load_extension('cogs.some_cog')

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')

@bot.command()
async def amongus(ctx):
    await ctx.send('Among Us Game Started!')

@bot.command()
async def stop(ctx):
    await ctx.send('Game Stopped!')

bot.run(TOKEN)
import os
import discord
import logging
from dotenv import load_dotenv
from discord.ext import commands


class Spotify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Greetings
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user} ({self.bot.user.id})')

    # Reconnect
    @commands.Cog.listener()
    async def on_resumed(self):
        print('Bot has reconnected!')

     # Error Handlers
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # await ctx.send(error)

        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid Command!')


# Gateway intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True

# Bot prefix
bot = commands.Bot(command_prefix=commands.when_mentioned_or('S '),
                   description='Commands', intents=intents)

# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctine)s:%(levelnames :%{name}s: %(message)s'))
logger.addHandler(handler)

# Loading data from .env file
load_dotenv()
token = os.getenv('TOKEN')

if __name__ == '__main__':
    # Load extension
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            bot.load_extension(f'commands.{filename[: -3]}')

    bot.add_cog(Spotify(bot))
    bot.run(token, reconnect=True)

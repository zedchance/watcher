# watcher bot
# Automatically sends notifications when a user/bot goes offline

import logging
from discord.ext import commands

from config import owner_id, discord_key

logging.basicConfig(filename='bot.log',
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    level=logging.INFO)


# Prefix setup
def get_prefix(client, message):
    logging.info(f'[{message.guild}/{message.channel}] {message.author}: {message.content}')
    return commands.when_mentioned_or('watcher')(client, message)


# Bot setup
bot = commands.Bot(command_prefix=get_prefix,
                   description='A notification bot to tell you when other bots have gone down',
                   owner_id=owner_id,
                   case_insensitive=True)

# Cog setup
cogs = ['cogs.commands']


@bot.event
async def on_ready():
    logging.info(f'Logged on as {bot.user.name}!')
    for cog in cogs:
        logging.info(f'Loading {cog}')
        bot.load_extension(cog)
    logging.info("Cogs loaded")
    print(f'Up and running as {bot.user.name}')
    return

# Run bot
bot.run(discord_key, bot=True, reconnect=True)

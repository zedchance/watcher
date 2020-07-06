# events cog watches for change in user status

from discord.ext import commands


class Events(commands.Cog):
    """ Events cog that watches for change in user status """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='version',
                      description='Bot version',
                      aliases=['-v'],
                      case_insensitive=True)
    async def version_command(self, ctx):
        """ Shows bot version number """
        return await ctx.send('v0.1')


# Cog setup
def setup(bot):
    bot.add_cog(Events(bot))

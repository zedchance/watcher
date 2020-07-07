# events cog watches for change in user status

import yaml
import discord
from discord.ext import commands, tasks


def get_watchlist():
    """ Gets the current watchlist from yaml file """
    with open('data.yaml') as file:
        return yaml.full_load(file)


def write_watchlist(watchlist):
    """ Writes the current watchlist to yaml file """
    with open('data.yaml', 'w') as file:
        return yaml.dump(watchlist, file)


def add_to_watchlist(author, user_to_track, member_list):
    """ Adds a user_to_track to the author's watchlist """
    # Open YAML file and check if empty
    watchlist = get_watchlist()
    if watchlist is None:
        watchlist = dict()
    # Check to see if author is in the offline watchlist already
    if author not in watchlist:
        watchlist[author] = []
    # Search for user
    found = None
    for member in member_list:
        if str(user_to_track).__contains__(str(member.id)):
            found = member
    if not found:
        return False
    for entry in watchlist[author]:
        if entry['id'] == found.id:
            return False
    watchlist[author].append(dict(name=found.name, id=found.id))
    write_watchlist(watchlist)
    return True


class Commands(commands.Cog):
    """ Commands cog that watches for change in user status """

    def __init__(self, bot):
        self.bot = bot
        self.check_watchlist.start()

    @commands.command(name='version',
                      description='Bot version',
                      aliases=['-v'],
                      case_insensitive=True)
    async def version_command(self, ctx):
        """ Shows bot version number """
        return await ctx.send('Under development...')

    @commands.command(name='add',
                      description='Add a user to the offline watchlist',
                      case_insensitive=True)
    async def add_command(self, ctx, username):
        """ Adds a user to the offline watchlist """
        members = ctx.guild.members
        author = ctx.message.author.id
        successful = add_to_watchlist(author, username, members)
        if successful:
            description = f'Added {username} to {ctx.message.author.mention}\'s offline watchlist'
        else:
            description = f'Didn\'t add the user'  # TODO make this handle the user already existing also
        embed = discord.Embed(name='*watcher*', description=description)
        return await ctx.send(embed=embed)

    @tasks.loop(seconds=60.0)
    async def check_watchlist(self):
        """ Checks the watchlist to see if anyone is offline """
        print("RUNNING CHECK")
        watchlist = get_watchlist()
        members = self.bot.get_all_members()
        for member in members:
            for user, watches in watchlist.items():
                for watch in watches:
                    if watch['id'] == member.id and str(member.status) == 'offline':
                        print("  ", member.name, member.status)
                        dm = self.bot.get_user(user)
                        embed = discord.Embed(name='*watcher*',
                                              description=f'`{member.name}` is offline.')
                        await dm.send(embed=embed)
        return


# Cog setup
def setup(bot):
    bot.add_cog(Commands(bot))
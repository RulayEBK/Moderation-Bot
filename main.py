import discord  
from discord.ext import commands
import os

#Prefix & Status & Load CMD
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
bot.remove_command('help')
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('!help for commands'))





#Embed CMD
@bot.command(name='createembed', help='Create an embed with a footer')
@commands.has_permissions(manage_messages=True)
async def createembed(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel
    await ctx.send('**Create Embed**')
    await ctx.send('**Enter the title of the embed:**')
    title = await bot.wait_for('message', check=check)
    title = title.content
    await ctx.send('**Enter the description of the embed:**')
    description = await bot.wait_for('message', check=check)
    description = description.content
    await ctx.send('**Enter the footer of the embed:**')
    footer = await bot.wait_for('message', check=check)
    footer = footer.content
    await ctx.send('**Enter the image URL of the embed:**')
    image_url = await bot.wait_for('message', check=check)
    image_url = image_url.content
    embed = discord.Embed(title=title, description=description, color=0x000000)
    embed.set_footer(text=footer)
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)


#Clear command
@bot.command(name='clear', help='Clears the chat')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'**Cleared {amount} messages!**', delete_after=10)



#Kick CMD
@bot.command(name='kick', help='Kicks a member from the server')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'**Kicked {member.mention}!**', delete_after=10)

#Ban CMD
@bot.command(name='ban', help='Bans a member from the server')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'**Banned {member.mention}!**', delete_after=10)

#Kick All cmd
@bot.command(name='kickall', help='Kicks all members from the server')
@commands.has_permissions(administrator=True)
async def kickall(ctx):
    for member in ctx.guild.members:
        if member != ctx.author:
            await member.kick()
            await ctx.send(f'**Kicked all members!**', delete_after=10)

#Ban All cmd
@bot.command(name='banall', help='Bans all members from the server')
@commands.has_permissions(administrator=True)
async def banall(ctx):
    for member in ctx.guild.members:
        if member != ctx.author:
            await member.ban()
            await ctx.send(f'**Banned all members!**', delete_after=10)

#Help Panel
@bot.command(name='help', help='Displays this help panel')
async def help(ctx):
    embed = discord.Embed(title="Help Panel", description="Here are the available commands:", color=0x00ff00)
    embed.add_field(name="**General**", value="`help` - Displays this help panel")
    embed.add_field(name="**Moderation**", value="`kick` - `Ban` - ` Clear`")
    embed.add_field(name="**Admin**", value="`kickall` - `banall`")
    embed.set_footer(text="Create By @Rulay EBK")
    await ctx.send(embed=embed)
            



bot.run('Token HERE')

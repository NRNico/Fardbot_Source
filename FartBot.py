import discord
from discord.ext import commands
import random

from Token import TOKENIS

# Importing tracemalloc module
import tracemalloc
# Enabling tracemalloc to track memory allocations
tracemalloc.start()
# Creating a list of numbers
numbers = [i for i in range(1000000)]
# Printing the current memory usage
print(tracemalloc.get_traced_memory())
# Stopping tracemalloc and freeing memory
tracemalloc.stop()

#create command prefix and set intents
intents = discord.Intents.default()
intents.members = True
intents.message_content=True
bot = commands.Bot(command_prefix="!",intents=intents)

#Send a output if bot is ready

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

#Sync commands.

@bot.command(name="sync")
async def sync(ctx):
    try:
        fmt = await bot.tree.sync() #syncs bot tree when !sync is used
        await ctx.send(f"Synced {len(fmt)} command(s) to the current server")
    except Exception as e:
        await ctx.send(f"Error while syncing commands: {e}")
        return

#Check for errors when commands are used.

#Role creating
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error,  commands.MissingRequiredArgument): #sends a error message when a command used is missing a argument
        await ctx.send("Lil bro add the missin' argument.")
    if isinstance(error, commands.MissingPermissions): #sends a error message when a member doesnt have permission to use a command.
        await ctx.send("Omg lil bro, get za perms needed.")

@bot.command()
async def fart(ctx,*, FartType="normal"):
    guild = ctx.guild
    pleasant= guild.get_role(1198761033230192801)
    stinky = guild.get_role(1198760788698091530)
    poopy = guild.get_role(1198760859325972520)
    banished = guild.get_role(1179550830207193148)
    print(type(stinky))
    FartType.lower()
    user = ctx.message.author
    if user.id == 1115735704408965132:
        if FartType == "shart":
           await ctx.send("i wanna eat that tasty smelling crap...")
        else:
            if FartType == "normal":
                await ctx.send("mmmmmm, that fart smells GOOD. (pls dont shower)")
            else:
                await ctx.send("Your suddenly smelling gooood. *wink wink*")
        role_name = "Pleasant auroma"
        if role_name not in user.roles:
            await user.add_roles(pleasant)
    else:
        role_name="Stinky"
        rolename="Poopy"
        if FartType == "normal":
            await ctx.send("That fart, smells HORRIBLE. PLEASE TAKE A SHOWER!")
        elif FartType == "silent":
            await ctx.send("HOLY CRAP YOU SMELL HORRIBLE AHHHHHH")
        elif FartType=="shart":
            await ctx.send("did you just shart your pants? holy hell i ca-")
        if stinky not in user.roles:
            if FartType != "shart":
                await user.add_roles(stinky)
        if poopy not in user.roles:
            if  FartType == "shart":
                await user.add_roles(poopy)
                await user.add_roles(banished)



@bot.command(name="shower")
async def shower(ctx):
    guild = ctx.guild
    pleasant= guild.get_role(1198761033230192801)
    stinky = guild.get_role(1198760788698091530)
    poopy = guild.get_role(1198760859325972520)
    banished = guild.get_role(1179550830207193148)
    user = ctx.message.author
    if poopy in user.roles:
       await ctx.send("You tried to shower away a poopy, hahaha loser")
    else:
        if user.id == 1115735704408965132:
            await user.remove_roles(pleasant)
            await ctx.send("Aghh, you washed away the nice smelling farty")
        else:
            await user.remove_roles(stinky)
            await ctx.send("You washed your stinky away!")
           
#Slaps for !slap command
slaps= ["with a big fish","with a nokia","","with a spiky cactus","with a dog","with a piece of air, Dafuq?"]

#Slap command

@bot.command()
async def slap(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if type(user) == discord.member.Member:
        await ctx.send(f'{ctx.message.author.mention} has slapped {user.mention} {random.choice(slaps)}')
    else:
        await ctx.send(f'{ctx.message.author.mention} got slapped {random.choice(slaps)}')

#Kiss command.

@bot.command()
async def kiss(ctx, *,user : discord.Member = None):
    await ctx.message.delete()
    if type(user) == discord.member.Member:
        await ctx.send(f'{ctx.message.author.mention} kissed {user.mention}, What a simp...')
    else:
        await ctx.send(f'{ctx.message.author.mention} has kissed the mirror, loneliness hits.')
@bot.command()
async def murder(ctx, *,user : discord.Member = None):
    await ctx.message.delete()
    if type(user) == discord.member.Member:
        await ctx.send(f'{ctx.message.author.mention} murdered {user.mention}, What a kill!')
    else:
        await ctx.send(f'{ctx.message.author.mention} commited suicide! loser')

bot.run(TOKENIS)
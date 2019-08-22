import discord
from discord.ext import commands, tasks
from itertools import cycle
import os




client = commands.Bot(command_prefix = '.')
status= cycle(['Hola', 'bebeto'])



@client.event
async def on_ready():
	change_status2.start()
	print('Ando de rucula')

@tasks.loop(seconds=5)
async def change_status2():
	await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, endswithxtension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')
	
@client.command()	
@commands.has_permissions(manage_messages=True)
async def clear(ctx, ammount=2):
	amount=1
	if ammount>amount:
		await ctx.channel.purge(limit=ammount+1)
	else:
		await ctx.send('¿Y si me decís bien el numerito?')

@client.command()		
async def nsfw(ctx):
	if ctx.channel.nsfw==True:
		await ctx.send("Ta hot el canal")
	else:
		await ctx.send("No mandes marranadas")




for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')



client.run('NjA2NDcxNjg0OTE2MjQ4NTc4.XV1uSw.CoFdVlj8ZdoMiqD1saLhh6UlW9U')




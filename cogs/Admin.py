import discord	
from discord.ext import commands, tasks

class Administrar(commands.Cog):

	def __init__(self, client):
		self.client=client




		@client.command()
		@commands.has_permissions(administrator=True)
		async def kick(ctx, member:discord.Member = None):
			if not member:
				await ctx.send("Y si me decis un gil para kickear?")
				return
			await member.kick()
			await ctx.send(f"{member.mention} nos vimo gato")
		@kick.error
		async def kick_error(ctx, error):
			if isinstance(error, commands.CheckFailure):
				await ctx.send("No te hagas el vivo, No tenes permisos")				
			await ctx.send("No te hagas el vivo, No tenes permisos")
		

		@client.command()
		@commands.has_permissions(administrator=True)
		async def ban(ctx, member:discord.Member = None):
			if not member:
				await ctx.send("Y si me decis un gil para banear?")
				return
			await member.ban()
			await ctx.send(f"{member.mention} banea3")
	
		@ban.error
		async def kick_error(ctx, error):
			if isinstance(error, commands.CheckFailure):
				await ctx.send("No te hagas el vivo, No tenes permisos")
			
		
		@client.command()
		@commands.has_permissions(administrator=True)
		async def unban(ctx, *, member):
			banned_users = await ctx.guild.bans()
			member_name, member_discriminator = member.split('#')
			for ban_entry in banned_users:
				user = ban_entry.user
				if (user.name, user.discriminator) == (member_name, member_discriminator):
					await ctx.guild.unban(user)
					await ctx.send(f'{user.mention} puede volver')
					return




		@client.command()
		@commands.has_permissions(administrator=True)
		async def mute (ctx, member:discord.Member=None):
			if not member:
				await ctx.send("Y si me decis un gil para mutear?")
				return
			role=discord.utils.get(ctx.guild.roles, name="muted")
			await member.add_roles(role)

		@mute.error	
		async def mute_error(ctx, error):
			if isinstance(error, commands.CheckFailure):
				await ctx.send("No te hagas el vivo no tenes permisos")



def setup(client):
	client.add_cog(Administrar(client))

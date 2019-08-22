import discord
import random
from discord.ext import commands


class Bola_8(commands.Cog):
	def __init__(self, client):
		self.client=client


		@client.command(aliases=['8ball'])
		async def _8ball(ctx, *, question):
			responses = ['Pa mi que si.',
						'Muy verdad.',
						'TIENE que ser así.',
						'Capáz nomás.',
						'Pinta bien.',
						'Me da que si.',
						'No tengo pruebas pero tampoco tengo dudas.',
						'Chi cheñol https://pbs.twimg.com/media/Dvg7z2PU8AI6Qbo.jpg',
						'Confía que sale.',
						'No te escuché, dale de nuevo.',
						'Ando con las manos llenas, en 5 min pregunta de vuelta.',
						'Si te lo digo no pasará lo que tenga que pasar.',
						'No te lo puedo mandar ahora.',
						'Puede ser.',
						'F.',
						'Nel perro.',
						'Probrecito...',
						'Lo que tengo en vista no es bueno.',
						'DUDOSO.']

			await ctx.send(f'Pregunta: {question}\nRespuesta: {random.choice(responses)}')



def setup(client):
	client.add_cog(Bola_8(client))

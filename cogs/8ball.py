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
						'BUENARDOOOO.',
						'Douuu vas re chetE.',
						'Foooertee.',
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
						'DUDOSO.',
						'ESTOY TOTALMENTE DE ACUERDO CONTIGO',
						'Mira el papel lamentable que estás haciendo',
						'DOOOOU']


			await ctx.send(f'Pregunta: {question}\nRespuesta: {random.choice(responses)}')


		@client.command()
		async def bola(ctx):
			responses = ['Pa mi que si.',
						'Muy verdad.',
						'TIENE que ser así.',
						'Capáz nomás.',
						'Pinta bien.',
						'Me da que si.',
						'No tengo pruebas pero \n tampoco tengo dudas.',
						'BUENARDOOOO.',
						'Douuu vas re chetE.',
						'Foooertee.',
						'Chi cheñol https://pbs.twimg.com/media/Dvg7z2PU8AI6Qbo.jpg',
						'Confía que sale.',
						'No te escuché, \n dale de nuevo.',
						'Ando con las manos llenas,\n en 5 min pregunta de vuelta.',
						'Si te lo digo no pasará \n lo que tenga que pasar.',
						'No te lo puedo mandar ahora.',
						'Puede ser.',
						'F.',
						'Nel perro.',
						'Probrecito...',
						'Lo que tengo en vista no es bueno.',
						'DUDOSO.',
						'ESTOY TOTALMENTE DE \n ACUERDO CONTIGO',
						'Mira el papel lamentable \n que estás haciendo']


			await ctx.send(f'{random.choice(responses)}')
			



def setup(client):
	client.add_cog(Bola_8(client))

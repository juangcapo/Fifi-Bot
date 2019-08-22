import discord
from discord.ext import commands
import requests
import random	
import xmltodict
import pprint
import json


tagsito=None
randomeado=random.randrange	(2,50)
x=" ";

class Wallpaper_o_NSFW(commands.Cog):

	def __init__(self, client, tagsito=None, randomeado=randomeado):
		self.client=client
		self.tagsito=tagsito
		self.randomeado=randomeado


	@commands.command()
	async def r34(self, ctx, tagsito, randomeado=None):
		randomeado=str(random.randint(2,50))
		link={"base":"https://rule34.xxx/index.php?page=dapi&s=post&q=index&limit=1&pid={randomeado}&tags={tagsito}"}
		#print(link["base"])

		r=requests.get(link["base"].format(randomeado=randomeado, tagsito=tagsito))
		#print (r)
		#print(r.content)
		respuesta_texto=r.text
		#print (respuesta_texto)
		
		respuesta_str=str(respuesta_texto)
		print()

		#print (respuesta_str)

		my_xml=r.content
		my_dict=xmltodict.parse(my_xml)
		#print (my_dict)
		#print(my_dict['posts'])
		if ctx.channel.nsfw==True:
			print(my_dict['posts']['post']['@file_url'])
			await ctx.send(my_dict['posts']['post']['@file_url'])

		else:
			await ctx.send('¡ACA NO MANDES HENTAI!')



	@commands.command()

	async def konachan(self, ctx, tagsito, randomeado=None):
		randomeado=str(random.randint(2,50))
		link={"base":"https://konachan.com/post.json?tags={tagsito}&page={randomeado}&limit=1"}
		print(link["base"])
			
		r=requests.get(link["base"].format(tagsito=tagsito, randomeado=randomeado))
		respuesta_lista=r.json()
		#print(respuesta_lista)
		respuesta_dic=respuesta_lista[0]


		if ctx.channel.nsfw==True:
			print (respuesta_dic['file_url'])
			await ctx.send (respuesta_dic['file_url'])
		else:
			await ctx.send('¡ACA NO MANDES HENTAI')

	@commands.command()
	async def wallpaper(self, ctx, tagsito, randomeado=None):
		randomeado=str(random.randint(2,50))
		link={"base":"https://konachan.net/post.json?tags={tagsito}&page={randomeado}&limit=1"}
		#print(link["base"])
			
		r=requests.get(link["base"].format(tagsito=tagsito, randomeado=randomeado))
		respuesta_lista=r.json()
		#print(respuesta_lista)
		respuesta_dic=respuesta_lista[0]
		#print (respuesta_dic['file_url'])
		await ctx.send (respuesta_dic['file_url'])




def setup(client):
	client.add_cog(Wallpaper_o_NSFW(client))

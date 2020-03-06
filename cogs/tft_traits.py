import discord
from discord.ext import commands
import pickle
import json
import xmltodict


traitsInfo=[{
	"name": "Alchemist",
	"innate": "Alchemists move through other units and never stop moving."
	},{
	"name": "Assassin",
	"innate": "Assassins sneak across the battlefield at the start of combat, placing themselves opposite from where they started.",
	"description": "Deploying multiple Assassins grant them critical strike chance and increased critical strike damage, increasing with more Assassins.",
	"sets": [3, 6]
	},{
	"name": "Avatar",
	"description": "An Avatar's element is counted twice for trait bonuses.",
	},{
	"name": "Berserker",
	"innate": "At the start of combat, Berserkers leap to the nearest enemy.",
	"description": "Deploying multiple Berserkers grants their attacks a chance to deal damage in a cone behind the target. The chance increases with more Berserkers.",
	"sets": [3, 6]
	},{
	"name": "Blademaster",
	"description": "Deploying multiple Blademasters grants their attacks a chance to hit extra times, increasing with more Blademasters.",
	"sets": [2, 4, 6]
	},{
	"name": "Cloud",
	"description": "Deploying multiple Cloud champions grants your team dodge change. The dodge chance increases if more Cloud champions are deployed.",
	"sets": [2, 3, 4]
	},{
	"name": "Crystal",
	"description": "Deploying multiple Crystal champions grants them a maximum amount of damage they can take from a single attack or ability hit.",
	"sets": [2, 4]
	},{
	"name": "Desert",
	"description": "Deploying multiple Desert champions reduces the enemy team's armor. The reduction increases if more Desert champions are deployed.",
	"sets": [2, 4]
	},{
	"name": "Druid",
	"description": "Deploying two Druids grants all Druids health regeneration.",
	"sets": [2]
	},{
	"name": "Electric",
	"description": "Deploying multiple Electric champions causes them to damage adjacent enemies whenever they critically strike or are critically struck.",
	"sets": [2, 3, 4]
	},{
	"name": "Glacial",
	"description": "Deploying multiple Glacial champions grants their attacks a chance to stun their target, increasing with more Glacials.",
	"sets": [2, 4, 6]
	},{
	"name": "Inferno",
	"description": "Deploying multiple Inferno champions causes their abilities to temporarily ignite the ground beneath their targets, damaging enemies standing in the fire. Damage increases with more Inferno champions.",
	"sets": [3, 6, 9]
	},{
	"name": "Light",
	"description": "Deploying multiple Light champions causes them to, on death, heal other Light champions for a percentage of their max health and grant them attack speed for the remainer of the round (stacking with multiple Light champion deaths). Heal and attack speed increse with more Light champions.",
	"sets": [3, 6, 9]
	},{
	"name": "Lunar",
	"description": "Deploying multiple Lunar champions grants all allies critical strike chance, critical strike damage, and spell power, increasing over time.",
	"sets": [2]
	},{
	"name": "Mage",
	"description": "Deploying multiple Mages grants them a chance after casting an ability to cast it again. This chance increases with more Mages.",
	"sets": [3, 6]
	},{
	"name": "Mountain",
	"description": "Deploying multiple Mountain champions grants a massive shield to a random ally at the start of combat.",
	"sets": [2]
	},{
	"name": "Mystic",
	"description": "Deploying multiple Mystics grants all allies magic resist, increasing with more Mystics.",
	"sets": [2, 4]
	},{
	"name": "Ocean",
	"description": "Deploying multiple Ocean champions periodically grants allies mana. The amount increases with more Ocean champions.",
	"sets": [2, 4, 6]
	},{
	"name": "Poison",
	"description": "Deploying mutliple Poison champions causes their damaging attacks and abilities to increase the mana costs of their targets' abilities.",
	"sets": [3]
	},{
	"name": "Predator",
	"description": "Deploying multiple Predators causes their attacks and abilities to immediately kill low-health enemies.",
	"sets": [3]
	},{
	"name": "Ranger",
	"description": "Deploying multiple Rangers periodically grants them a chance to gain a burst of attack speed, increasing with more Rangers.",
	"sets": [2, 4, 6]
	},{
	"name": "Shadow",
	"description": "Deploying multiple Shadow champions causes them to deal increased damage for the first few seconds of combat, as well as for a few seconds when they score a takedown. Deploying more Shadow champions causes all of them to deal increased damage when any of them score a takedown.",
	"sets": [2, 4]
	},{
	"name": "Steel",
	"description": "Deploying multiple Steel champions causes them to briefly become immune to damage when they drop below 50% health.",
	"sets": [2, 3, 4]
	},{
	"name": "Summoner",
	"description": "Deploying multiple Summoners increases the health and duration of their spawned allies, increasing with more Summoners. Summoners' pets benefit from Element and Class bonuses, but don't count as additional units toward activiating higher levels of those bonuses.",
	"sets": [3, 6]
	},{
	"name": "Warden",
	"description": "Deploying multiple Wardens grants them armor, increasing with more Wardens.",
	"sets": [2, 4, 6]
	},{
	"name": "Woodland",
	"description": "Deploying multiple Woodland champions causes one of them to randomly create a clone of themselves (including items) at the start of combat.",
	"sets": [3]
	}]



tftchampsInfo=[
  {
    "champion": "Aatrox",
    "cost": 3,
    "traits": [
      "Light",
      "Blademaster"
    ]
  },
  {
    "champion": "Annie",
    "cost": 4,
    "traits": [
      "Inferno",
      "Summoner"
    ]
  },
  {
    "champion": "Ashe",
    "cost": 4,
    "traits": [
      "Crystal",
      "Ranger"
    ]
  },
  {
    "champion": "Azir",
    "cost": 3,
    "traits": [
      "Desert",
      "Summoner"
    ]
  },
  {
    "champion": "Brand",
    "cost": 4,
    "traits": [
      "Inferno",
      "Mage"
    ]
  },
  {
    "champion": "Braum",
    "cost": 2,
    "traits": [
      "Glacial",
      "Warden"
    ]
  },
  {
    "champion": "Diana",
    "cost": 1,
    "traits": [
      "Inferno",
      "Assassin"
    ]
  },
  {
    "champion": "DrMundo",
    "cost": 3,
    "traits": [
      "Poison",
      "Berserker"
    ]
  },
  {
    "champion": "Ezreal",
    "cost": 3,
    "traits": [
      "Glacial",
      "Ranger"
    ]
  },
  {
    "champion": "Ivern",
    "cost": 1,
    "traits": [
      "Woodland",
      "Druid"
    ]
  },
  {
    "champion": "Janna",
    "cost": 4,
    "traits": [
      "Cloud",
      "Mystic"
    ]
  },
  {
    "champion": "Jax",
    "cost": 2,
    "traits": [
      "Light",
      "Berserker"
    ]
  },
  {
    "champion": "Karma",
    "cost": 3,
    "traits": [
      "Lunar",
      "Mystic"
    ]
  },
  {
    "champion": "KhaZix",
    "cost": 4,
    "traits": [
      "Desert",
      "Assassin"
    ]
  },
  {
    "champion": "Kindred",
    "cost": 3,
    "traits": [
      "Shadow",
      "Inferno"
    ]
  },
  {
    "champion": "KogMaw",
    "cost": 1,
    "traits": [
      "Poison",
      "Predator"
    ]
  },
  {
    "champion": "LeBlanc",
    "cost": 2,
    "traits": [
      "Woodland",
      "Assassin"
    ]
  },
  {
    "champion": "Leona",
    "cost": 1,
    "traits": [
      "Lunar",
      "Warden"
    ]
  },
  {
    "champion": "Lux",
    "cost": 7,
    "traits": [
      "Crystal",
      "Electric",
      "Glacial",
      "Inferno",
      "Light",
      "Steel",
      "Ocean",
      "Shadow",
      "Cloud",
      "Woodland",
      "Avatar"
    ]
  },
  {
    "champion": "Malphite",
    "cost": 4,
    "traits": [
      "Mountain",
      "Warden"
    ]
  },
  {
    "champion": "Malzahar",
    "cost": 2,
    "traits": [
      "Shadow",
      "Summoner"
    ]
  },
  {
    "champion": "Maokai",
    "cost": 1,
    "traits": [
      "Woodland",
      "Druid"
    ]
  },
  {
    "champion": "MasterYi",
    "cost": 5,
    "traits": [
      "Shadow",
      "Mystic"
    ]
  },
  {
    "champion": "Nami",
    "cost": 5,
    "traits": [
      "Ocean",
      "Mystic"
    ]
  },
  {
    "champion": "Nasus",
    "cost": 1,
    "traits": [
      "Light",
      "Warden"
    ]
  },
  {
    "champion": "Nautilus",
    "cost": 3,
    "traits": [
      "Ocean",
      "Warden"
    ]
  },
  {
    "champion": "Neeko",
    "cost": 2,
    "traits": [
      "Woodland",
      "Druid"
    ]
  },
  {
    "champion": "Nocturne",
    "cost": 3,
    "traits": [
      "Steel",
      "Assassin"
    ]
  },
  {
    "champion": "Olaf",
    "cost": 4,
    "traits": [
      "Glacial",
      "Berserker"
    ]
  },
  {
    "champion": "Ornn",
    "cost": 1,
    "traits": [
      "Electric",
      "Warden"
    ]
  },
  {
    "champion": "Qiyana",
    "cost": 3,
    "traits": [
      "Ocean",
      "Inferno",
      "Cloud",
      "Woodland",
      "Assassin"
    ]
  },
  {
    "champion": "RekSai",
    "cost": 2,
    "traits": [
      "Steel",
      "Predator"
    ]
  },
  {
    "champion": "Renekton",
    "cost": 1,
    "traits": [
      "Desert",
      "Berserker"
    ]
  },
  {
    "champion": "Singed",
    "cost": 5,
    "traits": [
      "Poison",
      "Alchemist"
    ]
  },
  {
    "champion": "Sion",
    "cost": 3,
    "traits": [
      "Shadow",
      "Berserker"
    ]
  },
  {
    "champion": "Sivir",
    "cost": 3,
    "traits": [
      "Desert",
      "Blademaster"
    ]
  },
  {
    "champion": "Skarner",
    "cost": 2,
    "traits": [
      "Crystal",
      "Predator"
    ]
  },
  {
    "champion": "Soraka",
    "cost": 3,
    "traits": [
      "Light",
      "Mystic"
    ]
  },
  {
    "champion": "Syndra",
    "cost": 2,
    "traits": [
      "Ocean",
      "Mage"
    ]
  },
  {
    "champion": "Taliyah",
    "cost": 1,
    "traits": [
      "Mountain",
      "Mage"
    ]
  },
  {
    "champion": "Taric",
    "cost": 5,
    "traits": [
      "Crystal",
      "Warden"
    ]
  },
  {
    "champion": "Thresh",
    "cost": 2,
    "traits": [
      "Ocean",
      "Warden"
    ]
  },
  {
    "champion": "Twitch",
    "cost": 4,
    "traits": [
      "Poison",
      "Ranger"
    ]
  },
  {
    "champion": "Varus",
    "cost": 2,
    "traits": [
      "Inferno",
      "Ranger"
    ]
  },
  {
    "champion": "Vayne",
    "cost": 1,
    "traits": [
      "Light",
      "Ranger"
    ]
  },
  {
    "champion": "Veigar",
    "cost": 3,
    "traits": [
      "Shadow",
      "Mage"
    ]
  },
  {
    "champion": "Vladimir",
    "cost": 1,
    "traits": [
      "Ocean",
      "Mage"
    ]
  },
  {
    "champion": "Volibear",
    "cost": 2,
    "traits": [
      "Glacial",
      "Electric"
    ]
  },
  {
    "champion": "Warwick",
    "cost": 1,
    "traits": [
      "Glacial",
      "Predator"
    ]
  },
  {
    "champion": "Yasuo",
    "cost": 2,
    "traits": [
      "Cloud",
      "Blademaster"
    ]
  },
  {
    "champion": "Yorick",
    "cost": 4,
    "traits": [
      "Light",
      "Summoner"
    ]
  },
  {
    "champion": "Zed",
    "cost": 5,
    "traits": [
      "Electric",
      "Summoner",
      "Assassin"
    ]
  },
  {
    "champion": "Zyra",
    "cost": 1,
    "traits": [
      "Inferno",
      "Summoner"
    ]
  }
]











class Traints_Information(commands.Cog):

	def __init__(self, client):
		self.client=client

		@client.command()
		async def traitsHelp(ctx):
			await ctx.send("Type .traits and the trait you want to know about.")


		@client.command(aliases=['traits'])
		async def Traits(ctx, nameInput):

			#print(strFile)

			#print(file[1]["name"])

			if nameInput=="Alchemist":
				listNumber=0
			elif nameInput=="Assassin":
				listNumber=1
			elif nameInput=="Avatar":
				listNumber=2
			elif nameInput=="Berserker":
				listNumber=3
			elif nameInput=="Blademaster":
				listNumber=4
			elif nameInput=="Cloud":
				listNumber=5
			elif nameInput=="Crystal":
				listNumber=6
			elif nameInput=="Desert":
				listNumber=7
			elif nameInput=="Druid":
				listNumber=8
			elif nameInput=="Electric":
				listNumber=9
			elif nameInput=="Glacial":
				listNumber=10
			elif nameInput=="Inferno":
				listNumber=11
			elif nameInput=="Light":
				listNumber=12
			elif nameInput=="Lunar":
				listNumber=13
			elif nameInput=="Mage":
				listNumber=14
			elif nameInput=="Mountain":
				listNumber=15
			elif nameInput=="Mystic":
				listNumber=16
			elif nameInput=="Ocean":
				listNumber=17
			elif nameInput=="Poison":
				listNumber=18
			elif nameInput=="Predator":
				listNumber=19
			elif nameInput=="Ranger":
				listNumber=20
			elif nameInput=="Shadow":
				listNumber=21
			elif nameInput=="Steel":
				listNumber=22
			elif nameInput=="Summoner":
				listNumber=23
			elif nameInput=="Warden":
				listNumber=24
			elif nameInput=="Woodland":
				listNumber=25


			if traitsInfo[listNumber]["name"]!=None:
				await ctx.send(traitsInfo[listNumber]["name"])

			try:
				await ctx.send(traitsInfo[listNumber]["innate"])
			except:
				await ctx.send(f'{traitsInfo[listNumber]["name"]} has no innate')

			try:
				await ctx.send(traitsInfo[listNumber]["description"])
			except:
				await ctx.send(traitsInfo[listNumber]["name"], "has no description")

			try:
				await ctx.send(traitsInfo[listNumber]["sets"])
			except:
				await ctx.send(traitsInfo[listNumber]["name"], "has no sets")		



		@client.command(aliases=["tftChampions", "tftchampions"])
		async def TFTChampions(ctx):
			await ctx.send(tftchampsInfo)






def setup(client):
	client.add_cog(Traints_Information(client))

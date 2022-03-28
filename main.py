import discord
from discord.ext import commands
import random

classic = ['Yes', 'No', 'Hohoho', 'bleh', '']

mod = [
    'Yes', 'No', 'Hohoho', 'bleh', '', 'Dumb', '?', 'Oh', 'Ok',
    '* DELETE NUMBER *'
]

soco = [
    '* Dá Um Soco Na Cara *', '* Dá Um Soco Na Barriga *', '* ele Desmaia *'
]

client = commands.Bot(command_prefix="gametb>", case_insensitive=True)

#event name


@client.event
async def on_ready():
    print('{0.user}'.format(client))


@client.command()
async def ben(ctx):
    variavel = random.choice(classic)
    await ctx.send(f'{variavel}')


@client.command()
async def repetir(ctx, message=""):
    await ctx.send(message)


@client.command()
async def benMod(ctx):
    variavel = random.choice(mod)
    await ctx.send(f'{variavel}')


@client.command()
async def socar(ctx):
    variavel = random.choice(soco)
    await ctx.send(f'{variavel}')


@client.command()
async def p1(ctx):
    await ctx.send(f'* explodir *')


@client.command()
async def p2(ctx):
    await ctx.send(f'* bebendo a poção, Sotando Fogo Pela Boca *')


@client.command()
async def p3(ctx):
    await ctx.send(f'* sorriso assustador *')


@client.command()
async def p4(ctx):
    await ctx.send(f'* Nada *')


@client.command()
async def p5(ctx):
    await ctx.send(f'* TORNADO DE PLASMA *')


@client.command()
async def p6(ctx):
    await ctx.send(f'* Fogo Saiu Da Poção *')


client.run('')

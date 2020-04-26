from bs4 import BeautifulSoup
import requests
import re
import discord
from discord.ext import commands

from datetime import datetime
import asyncio

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('I am ready!')


@client.command('COVID-19')
async def coronavirus(ctx):
    link = 'https://www.worldometers.info/coronavirus/'
    url = requests.get(link)
    soup = BeautifulSoup(url.content, 'html.parser')
    match = soup.findAll(class_='maincounter-number')
    match = str(match)

    result = re.sub('<[^<]+?>', '', match)
    result = result.replace('[', ' ')
    result = result.replace(',', ' ')
    result = result.replace(']', ' ')
    result = result.strip()
    ls = []
    for i in result:
        if i == ' ':
            ''
        elif i == '\n':
            ''
        else:
            i.split()
            ls.append(i)
    ls_cases = (ls[0:7])
    cases = ''
    for i in ls_cases:
        cases = cases + str(i)

    ls_deaths = (ls[7:12])
    deaths = ''
    for i in ls_deaths:
        deaths = deaths + str(i)
    ls_recovered = (ls[12:])
    recovered = ''
    for i in ls_recovered:
        recovered = recovered + str(i)

    stats = []
    stats.append(cases)
    stats.append(deaths)
    stats.append(recovered)
    embed = discord.Embed(color=0x69FFB4, title=f'Cases: {stats[0]} \nDeaths: {stats[1]} \nRecovered: {stats[2]}')
    embed.set_footer(text=f'Live Coronavirus info.')
    await ctx.send(embed=embed)



client.run('token')

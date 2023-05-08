import discord
from discord.ext import commands
import requests
from web import site
import os
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='>', intents=intents)
token = os.getenv("token")

async def main():
  for filename in os.listdir('./cogs'):
     if filename.endswith('.py'):
         print(f"found {filename}")
         await bot.load_extension(f'cogs.{filename[:-3]}')
         #moment 
         
asyncio.run(main())

print("test")

base_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = os.getenv("apikey")

@bot.command()
async def weather(ctx, *, city: str):
  city_name = city
  complete_url = base_url + "appid=" + api_key + "&q=" + city_name
  response = requests.get(complete_url)
  x = response.json()
  channel = ctx.message.channel
  if x["cod"] != "404":
    async with channel.typing():
      y = x["main"]
      current_temperature = y["temp"]
      current_temperature_celsiuis = str(round(current_temperature - 273.15))
      current_humidity = y["humidity"]
      z = x["weather"]
      weather_description = z[0]["description"]
      weather_description = z[0]["description"]
      embed = discord.Embed(title=f"Weather in {city_name}",
                              color=ctx.guild.me.top_role.color,
                              timestamp=ctx.message.created_at,)
      embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
      embed.add_field(name="Temperature", value=f"**{current_temperature_celsiuis}°C**", inline=False)
      embed.add_field(name="Humidity", value=f"**{current_humidity}%**", inline=False)
      embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
      embed.set_footer(text=f"Requested by {ctx.author.name}")
      await channel.send(embed=embed)
  else:
    await channel.send("City not found.")

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (bot.latency * 1000)} ms')



        
#===============================================================================


@bot.command()
async def loadall(ctx):
    text = ""
    em = discord.Embed(title = "Loading all cogs....", description = ":loading:", color = discord.Color.blue())
    msg = await ctx.send(embed = em)

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                text = text + f":small_green_triangle: **{filename}**" + "\n`>` `Successfully loaded.`" + "\n"
                em = discord.Embed(title = "Log", description = text, color = discord.Color.blue())
                await msg.edit(embed = em)
            except Exception as a:
                text = text + f":small_red_triangle: **{filename}**" + f"\n`>` `{a}`" + "\n"
                em = discord.Embed(title = "Log", description = text, color = discord.Color.blue())
                await msg.edit(embed = em)

@bot.command()
async def load(ctx, extension):
    try:
        await bot.load_extension(f'cogs.{extension}')
        await ctx.send(f"successfully loaded {extension}.")
    except Exception as a:
        await ctx.send(f"error in loading {extension}\n`{a}`")

@bot.command()
async def unload(ctx, extension):
        try:
            await bot.unload_extension(f'cogs.{extension}')
            await ctx.send(f"successfully unloaded {extension}.")
        except Exception as a:
            await ctx.send(f"error in unloading {extension}\n`{a}`")

@bot.command()
async def reload(ctx, extension):
        try:
            await bot.unload_extension(f'cogs.{extension}')
            await bot.load_extension(f'cogs.{extension}')
            await ctx.send(f"successfully reloaded {extension}.")
        except Exception as a:
            await ctx.send(f"error in reloading {extension}\n`{a}`")


@bot.command()
async def la(ctx):
    text = ""
    em = discord.Embed(title = "Loading all cogs....", description = "<a:loading:970301436174929930>", color = discord.Color.blue())
    msg = await ctx.send(embed = em)

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                text = text + f"<:small_green_triangle:970305160263893002> **{filename}**" + "\n`>` `Successfully loaded.`" + "\n"
                em = discord.Embed(title = "Load log", description = text, color = discord.Color.blue())
                await msg.edit(embed = em)
            except Exception as a:
                text = text + f"🔺 **{filename}**" + f"\n`>` `{a}`" + "\n"
                em = discord.Embed(title = "Load log", description = text, color = discord.Color.blue())
                await msg.edit(embed = em)

@bot.command()
async def rla(ctx):
    text = ""
    em = discord.Embed(title = "Reloading all cogs....", description = "⭕", color = discord.Color.blue())
    msg = await ctx.send(embed = em)

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.unload_extension(f'cogs.{filename[:-3]}')
                await bot.load_extension(f'cogs.{filename[:-3]}')
                
                text = text + f"<:small_green_triangle:970305160263893002> **{filename}**" + "\n`>` `Successfully reloaded.`" + "\n"
                em = discord.Embed(title = "Reload log", description = text, color = discord.Color.blue())
                await msg.edit(embed = em)
            except Exception as a:
                text = text + f"🔺 **{filename}**" + f"\n`>` `{a}`" + "\n"
                em = discord.Embed(title = "Reload log", description = text, color = discord.Color.blue())
                await msg.edit(embed = em)


site()
bot.run(token)
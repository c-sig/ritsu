import os
import discord
from dbhandler import db, User, Qualification, UserQualification

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
#ping command
@bot.slash_command(name="ping", description="Measure ping")
async def ping(ctx):
    await ctx.respond(f"Pong! ({bot.latency*1000}ms)")
    

TOKEN = os.environ.get('RITSU_TOKEN')
bot.run(TOKEN)


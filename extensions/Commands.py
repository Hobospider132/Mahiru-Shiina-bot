import lightbulb
import hikari
import random
import string
   

commands_plugin = lightbulb.Plugin('Commands')



@commands_plugin.command
@lightbulb.command('ln','Get EPUBS and PDFS for the Light Novel')
@lightbulb.implements(lightbulb.SlashCommand)
async def ln(ctx):
    await ctx.respond("Here: https://drive.google.com/drive/folders/1vAM64BhLwSZo8iPUpHHmCDUwguxrs26r. Make sure to check out the reading order for vol 5.5 special booklet, have fun.")

def load(bot):
    bot.add_plugin(commands_plugin)
from ast import arg

#from sqlalchemy import null
from discord.ext import commands
import discord
import datetime
from dependencies import token 
from get_data import *

from commands_help import *


bot = commands.Bot(command_prefix='!')
bot.remove_command('help')


@bot.command()
async def daodash(ctx):

    embed=discord.Embed(
        title='DAO Dash Help',
        description="""DAODash offers insights about your DAO’s health right here in Discord. 

See below for the commands DAODash accepts. 

Please enter any command followed by help to get more information on the command.

Example: !members help
""",
        color = discord.Colour.red()
    )

    embed.add_field(
        name='!members',
        value='returns a sorted list of active or inactive members in channel.',
        inline=False
    )

    embed.add_field(
        name='!multisig',
        value="""returns the wallets and amounts of DAO tokens that were distributed from a specific
multisig address""",
        inline=False
    )

    embed.add_field(
        name='!snapshot',
        value='returns metrics around community engagement in the last X votes',
        inline=False
    )
    embed.add_field(
        name='!roles',
        value='returns data around users acquiring a specific DAO Discord role',
        inline=False
    )

    await ctx.send(embed=embed)

@bot.command()
async def members(ctx,*args):
        start_time = str(datetime.datetime.now()).replace(":",".")
        params =  ','.join(args)
        print(len(args))
        

        if args[0] == 'help':
            await ctx.send(embed=member_help_embed)
        else:
            ##argument 2 will not exist if roles aren't specified
            if len(args)>2:
                dri = args[2]
            else:
                dri = ''

            print (dri)
            ##object of values used in querying
            obj = {
            'days':args[1],
            'channel_id':'840982271309250590',
            'discord_role_ids':dri,
            'table_request':args[0]+'_table',
            'start_time':start_time,
            'user':ctx.author.name,        
            }

            ##function which kicks off db querying, chart creation
            community_health(obj)

            filename = 'CommunityHealth - '+start_time +'.png'
        ##bot sends message with file attached
            await ctx.send('Hey @'+str(ctx.author)+', Here is your requested chart \n\n',file=discord.File(r"images/"+filename))

@bot.command()
async def multisig(ctx,*args):
    #create filename
     start_time = str(datetime.datetime.now()).replace(":",".")
     filename = 'Multisig - '+start_time +'.csv'


     if args[0]=='help':
        await ctx.send(embed=multisig_help_embed)
     else:
        if len(args)>1:
                sd = args[1]
        else:
                sd = False

        obj = {
        'wallet':args[0],
        'start_date':sd,
        'filename':filename,
        'user':ctx.author.name
        }

        multisig_analysis(obj)

        await ctx.send('Hey @'+str(ctx.author)+', Here is your requested data.',file=discord.File(r"data/"+filename))

bot.run(token)
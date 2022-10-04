from ast import arg

#from sqlalchemy import null
from discord.ext import commands
import discord
import datetime
from dependencies import token 
from get_data import *

from commands_help import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!',intents=intents)
bot.remove_command('help')



@bot.command()
async def daodash(ctx):

    await ctx.send(embed=daodash_embed)

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
            'channel_id':ctx.channel.id,
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
     filename = 'Multisig - '+start_time +'.png'


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
        'user':ctx.author.name,
        'start_time':start_time
        }

        multisig_analysis(obj)

        

        await ctx.send('Hey @'+str(ctx.author)+', Here is your requested chart.',file=discord.File(r"images/"+filename))


@bot.command()
async def snapshot(ctx,*args):
    #create filename
     start_time = str(datetime.datetime.now()).replace(":",".")
     filename = 'Snapshot - '+start_time +'.png'

     if len(args)>0:
        if args[0]=='help':
            await ctx.send(embed=snapshot_help_embed)
        else:
             votes = args[0]
     else: ##default is 5 if no parameter
            votes = 5

     obj = {
        'votes':votes,
        'filename':filename,
        'user':ctx.author.name,
        'start_time':start_time
        }

     snapshot_analysis(obj)
        

     await ctx.send('Hey @'+str(ctx.author)+', Here is your requested chart.',file=discord.File(r"images/"+filename))



@bot.command()
async def activity(ctx,*args):
    start_time = str(datetime.datetime.now()).replace(":",".")
    filename = 'Users - '+start_time +'.png'

    if args[0]=='help':
        await ctx.send(embed=roles_activity_embed)

    else: 
        obj = {
            'roles':args[0],
            'filename':filename,
            'user':ctx.author.name,
            'start_time':start_time
            }
        role_activity(obj)
        await ctx.send('Hey @'+str(ctx.author)+', Here is your requested chart.',file=discord.File(r"images/"+filename))





@bot.command()
async def roles(ctx,*args):
    start_time = str(datetime.datetime.now()).replace(":",".")
    filename = 'Users - '+start_time +'.png'

    if args[0]=='help':
        await ctx.send(embed=roles_help_embed)

    else: 
        obj = {
            'roles':args[1],
            'months':args[0],
            'filename':filename,
            'user':ctx.author.name,
            'start_time':start_time
            }
        roles_analysis(obj)
        await ctx.send('Hey @'+str(ctx.author)+', Here is your requested chart.',file=discord.File(r"images/"+filename))


@bot.command()
async def soft_votes(ctx,*args):
    start_time = str(datetime.datetime.now()).replace(":",".")
    filename = 'Soft_votes - '+start_time +'.png'
    print(str(len(args)) + ' -- length')

    obj = {
            'filename':filename,
            'user':ctx.author.name,
            'start_time':start_time
     }

    ##send help menu
    if len(args)>0 and args[0] =='help':
        await ctx.send(embed=discourse_help_embed)

    ##query sql with date range
    elif len(args)>0:
        obj['range']=True
        obj['start_date'] = args[0]
        obj['end_date']=args[1]
        discourse_analysis(obj)
        await ctx.send('Hey @'+str(ctx.author)+', Here is your requested chart.',file=discord.File(r"images/"+filename))
    ##query sql for last month
    else:
        obj['range']=False
        obj['start_date']=''
        obj['end_date']=''
        discourse_analysis(obj)
        await ctx.send('Hey @'+str(ctx.author)+', Here is your requested chart.',file=discord.File(r"images/"+filename))


bot.run(token)
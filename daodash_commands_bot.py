from ast import arg
from discord.ext import commands
import discord
import datetime
from dependencies import token 



from get_data import community_health

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

# @bot.command()
# async def try(ctx):
#     await ctx.send( ctx.guild)
#     await ctx.send( ctx.author)
#     await ctx.send( ctx.message.id)
#     await ctx.send( ctx)


@bot.command()
async def name(ctx,arg1,arg2):
    await ctx.send(f'{arg1} is the first value, {arg2} is the second value')

@bot.command()
async def values(ctx,*args):
    all = ','.join(args)
    print(args)
    await ctx.send(f'here is {all}')


@bot.command()
async def daodash(ctx):

    embed=discord.Embed(
        title='DAO Dash Help',
        description='DAO Dash can help with your analytics.',
        color = discord.Colour.red()
    )

    embed.add_field(
        name='!help',
        value='returns all dashbot commands currently available.',
        inline=True
    )

    # embed.add_field(
    #     name='!chart_list',
    #     value='returns a list of all charts currently available for that server.',
    #     inline=False
    # )


    embed.add_field(
        name='!members',
        value='List of Discord users who have been <in>active in the respective channel in the last <x> days.  Sorted by the most recently active user, bar chart indicates number of days inactive\n\n'+
        'Parameters: members [-inactive/active] [activity_threshold] [roles]\n '+
        '[inactive/active] - Ex: Active (String)\n'+
         '[activity_threshold] - Number of days '+
         '\n[discord_role(s)] - List out roles in quotes'
         '\n\nExample: !members active 10 "analytics_guild, guest pass"',
        inline=False
    )

    embed.add_field(
        name='!multisig',
        value='List of wallet addresses that received <token> from <multisig address> in the last <x> days. (flow thickness is proportional to amount of tokens transferred)',
        inline=False
    )

    await ctx.send(embed=embed)

@bot.command()
async def members(ctx,*args):
        start_time = str(datetime.datetime.now()).replace(":",".")
        params =  ','.join(args)
        print(len(args))
        
        ##print(ctx.channel.id)

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



bot.run(token)
from ast import arg
from discord.ext import commands
import discord

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
        params =  ','.join(args)
        print(args)
        
        ##print(ctx.channel.id)

        obj = {
    'table_request':args[0]+'_table',
    'days':args[1],
    'channel_id':'840982271309250590',
    'user':ctx.author
}
        print (obj)


    ##bot will not respond to bot message
        await ctx.send('Hey @'+str(ctx.author)+', The data will be here soon',file=discord.File(r"images/CommunityHealth - 2022-05-31 14.14.17.370546.png"))



bot.run('OTgxMzkyMjM1MjE0MDE2NTQ1.G5gn1B.kFocQSfv9TCiK8isOgwp7d742oi3ooSPe123oA')
import discord


##member comamand embed
member_help_embed=discord.Embed(
        title='Command: !members',
        description="""returns a sorted list of active or inactive members in channel.""",
        color = discord.Colour.red()
    )

member_help_embed.add_field(
        name='Syntax',
        value='!members active|inactive [activity threshold] [roles]',
        inline=False
    )

member_help_embed.add_field(
        name='Parameters:',
        value="""[inactive|active] - determines whether active or inactive members will be returned.

[activity_threshold] - determine the # of days that a user hasn’t commented in the channel to be considered in active. Default is 30. 

[discord_role(s)] - filters results to only include users with certain roles. Expression should be wrapped in quotes, roles separated by commas.""",
        inline=False
    )

member_help_embed.add_field(
        name='Example',
        value="""!members active 10 “analytics_guild, guest pass”""",
        inline=False
    )


##multisig command embed
multisig_help_embed=discord.Embed(
        title='Command: !multisig',
        description="""returns the amounts of DAO token that were distributed from the multisig address""",
        color = discord.Colour.red()
    )

multisig_help_embed.add_field(
        name='Syntax',
        value='!multisig multisig_address [start_date] [end_date]',
        inline=False
    )

multisig_help_embed.add_field(
        name='Parameters:',
        value="""multisig_address - eth address of the multisig in 0x format 

[start_date] - filters transfers to only include transfers that occurred after this date. Formatted as yyyy-mm-dd. Default is 30 days prior to today. 

[end_date] - filters transfers to only include transfers that occurred before this date. Formatted as yyyy-mm-dd. Default is today.""",
        inline=False
    )

multisig_help_embed.add_field(
        name='Example',
        value="""!multisig 0xe7636c7ef670a3Bcf772D9d57244c9e88aD90437 06-01-2022 06-30-2022""",
        inline=False
    )



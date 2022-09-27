import discord

###daodash embed
daodash_embed=discord.Embed(
        title='DAO Dash Help',
        description="""DAODash offers insights about your DAO’s health right here in Discord. 

                        See below for the commands DAODash accepts. 

                        Please enter any command followed by help to get more information on the command.

                        Example: !members help""",
        color = discord.Colour.red()
    )

daodash_embed.add_field(
        name='!members',
        value='returns a sorted list of active or inactive members in channel.',
        inline=False
    )

daodash_embed.add_field(
        name='!multisig',
        value="""returns the wallets and amounts of DAO tokens that were distributed from a specific
                 multisig address""",
        inline=False
    )

daodash_embed.add_field(
        name='!snapshot',
        value='# of wallet addresses who have voted in each of the last <x> snapshot votes',
        inline=False
    )

daodash_embed.add_field(
        name='!activity',
        value='returns a summary of users (who hold the requested roles) who have been active in specific time periods',
        inline=False
    )
daodash_embed.add_field(
        name='!roles',
        value='returns data around users acquiring a specific DAO Discord role',
        inline=False
    )

daodash_embed.add_field(
        name='!discourse',
        value='tbd',
        inline=False
    )



##member command embed
member_help_embed=discord.Embed(
        title='Command: !members',
        description="""returns a sorted list of active or inactive members in channel. The channel is specific to where the user is sending the message.""",
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
        value="""!members active 10 “Analytics Guild, Guest Pass”""",
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
        value='!multisig multisig_address start_date',
        inline=False
    )

multisig_help_embed.add_field(
        name='Parameters:',
        value="""multisig_address - eth address of the multisig in 0x format 

                [start_date] - filters transfers to only include transfers that occurred after this date. Formatted as yyyy-mm-dd. Default is 30 days prior to today. """,
        inline=False
    )

multisig_help_embed.add_field(
        name='Example',
        value="""!multisig 0xe7636c7ef670a3Bcf772D9d57244c9e88aD90437 2022-06-01""",
        inline=False
    )


##multisig command embed
snapshot_help_embed=discord.Embed(
        title='Command: !snapshot',
        description="""# of wallet addresses who have voted in each of the last <x> snapshot votes""",
        color = discord.Colour.red()
    )

snapshot_help_embed.add_field(
        name='Syntax',
        value='!snapshot [number_of_proposals]',
        inline=False
    )

snapshot_help_embed.add_field(
        name='Parameters:',
        value="""[number_of_proposals] - limits the results to the last number_of_proposals. Default is 5.""",
        inline=False
    )

snapshot_help_embed.add_field(
        name='Example',
        value="""!snapshot 10""",
        inline=False
    )

##multisig command embed
roles_help_embed=discord.Embed(
        title='Command: !roles',
        description="""Count of new users who were assigned/taken on this role in the last X months""",
        color = discord.Colour.red()
    )

roles_help_embed.add_field(
        name='Syntax',
        value='!roles [# of months] [discord_role(s)] ',
        inline=False
    )

roles_help_embed.add_field(
        name='Parameters:',
        value=""" [months] - number of months of datato include output
        [discord_role(s)] - filters results to only include users with certain roles. Expression should be wrapped in quotes, roles separated by commas.""",
        inline=False
    )

roles_help_embed.add_field(
        name='Example',
        value="""!roles 2 “Analytics Guild, Guest Pass”""",
        inline=False
    )

roles_activity_embed=discord.Embed(
        title='Command: !activity',
        description="""This insight is focused on understanding more macro trends - understanding the overall pattern of engagement in DAO/specific role.""",
        color = discord.Colour.red()
    )

roles_activity_embed.add_field(
        name='Syntax',
        value='!activity [discord_role(s)] ',
        inline=False
    )

roles_activity_embed.add_field(
        name='Parameters:',
        value="""[discord_role(s)] - filters results to only include users with certain roles. Expression should be wrapped in quotes, roles separated by commas.""",
        inline=False
    )

roles_activity_embed.add_field(
        name='Example',
        value="""!activity “Analytics Guild, Writers Guild”""",
        inline=False
    )


##discourse embed
discourse_help_embed=discord.Embed(
        title='Command: !discourse',
        description="""In Progress""",
        color = discord.Colour.red()
    )

discourse_help_embed.add_field(
        name='Syntax',
        value=' ',
        inline=False
    )

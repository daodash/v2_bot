

def create_health_query(comm_inputs):
    
    if len(comm_inputs['discord_role_ids']) >0:

        submitted_roles = comm_inputs['discord_role_ids'].split(',')
        print(submitted_roles)
        query_roles=[]
        i=1

        for r in submitted_roles:
    
            if i == len(submitted_roles):
                print(str(i)+ ' i first')
                
                print(i, r)
                query_roles.append('\''+r.strip())
                role_string = ''.join(query_roles)
                
            else:
                print(i, r)
                print(str(i)+ ' second')
                query_roles.append('\''+r.strip()+'\',')
                i+=1 
                
        role_string = ''.join(query_roles)  + '\'' 
        print(role_string)
            

        append_string = f"""AND 
        /*PYTHON PARAMETER  - WHERE STATEMENT FOR ROLE*/
        dr.role_name IN ("""+role_string+f""")
        """
    else:
        append_string=''


    return  f"""/* QUERY MESSAGES TABLE WITHIN PERIOD*/
    with active_user_messages as (
    SELECT m.channel_id,m.channel_name, m.TIMESTAMP, d.username as user,d.discord_user_id, EXTRACT( EPOCH FROM (CURRENT_DATE - m.TIMESTAMP))/86400  as activity_period FROM discord_messages m
    JOIN discord_user d ON d.discord_user_id = m.author_user_id 
    WHERE 
    /*PYTHON PARAMETER - ACTIVITY PERIOD */
    m.timestamp > CURRENT_DATE - {comm_inputs['days']}
    AND 
    /*PYTHON PARAMETER - WHERE STATEMENT FOR CHANNEL*/
    m.channel_id = {comm_inputs['channel_id']}
    ),

    /* GET USERS WITH SPECIFIC ROLE (role is active) */
    /*what if role is partially active during period? */
    users_with_roles  as (
    SELECT  du.discord_user_id,du.username as user ,r.discord_role_id, dr.role_name FROM discord_user_roles r 
    JOIN discord_roles dr ON r.discord_role_id = dr.discord_role_id
    JOIN discord_user du ON du.discord_user_id = r.discord_user_id
    WHERE
    r.active = True
    """+append_string+f"""),

    /*USERS WITH ROLE IN SPECIFIC PERIOD*/
    active_table as (
    SELECT u1.channel_name, u1.user, floor(min(u1.activity_period)) as days_since_active, 'Active Member Analysis' as report_name FROM active_user_messages u1
    INNER JOIN users_with_roles u2 ON u1.discord_user_id = u2.discord_user_id
    GROUP BY 1,2
    ORDER BY 3
    ),

    /* QUERY MESSAGES TABLE OUTSIDE OF PERIOD*/
    inactive_user_messages as (
    SELECT m.channel_id,m.channel_name, m.TIMESTAMP, d.username as user,d.discord_user_id, EXTRACT( EPOCH FROM (CURRENT_DATE - m.TIMESTAMP))/86400  as activity_period FROM discord_messages m
    JOIN discord_user d ON d.discord_user_id = m.author_user_id 
    WHERE 
    /*PYTHON PARAMETER - ACTIVTY PERIOD */
    m.timestamp < CURRENT_DATE - {comm_inputs['days']}
    AND 
    /*PYTHON PARAMETER - WHERE STATEMENT FOR CHANNEL*/
    m.channel_id = {comm_inputs['channel_id']}
    ),

    /*Users with role who are inactive in activity period*/

    inactive_table as (SELECT u4.channel_name,u3.user as user, floor(min(u4.activity_period)) as days_since_active,'Inactive Member Analysis' as report_name from users_with_roles u3
    LEFT JOIN inactive_user_messages u4 ON u3.discord_user_id = u4.discord_user_id
    WHERE u3.user NOT IN (
                            SELECT a.user from active_table a GROUP BY 1
                            )
    AND 
    u4.channel_name IS NOT NULL
    GROUP BY 1,2
    ORDER BY 3
    LIMIT 25
    )
    select * from {comm_inputs['table_request']}
    """

def create_multisig_query(ms_inputs):
    


    if ms_inputs['start_date']:
        print('date range')

        return f""" 
        select sg.from_address ,sg.to_address, CASE when cn.discord_user_name IS NULL
        THEN sg.to_address
        ELSE cn.discord_user_name END as user,sum(sg.amount_display), sg.timestamp_display from public.stg_subgraph_bank_1 sg
        left join coordinape_nodes cn on
        upper(sg.to_address) = upper(cn.address)
        where upper(from_address) = upper('{ms_inputs['wallet']}')
        and date(timestamp_display) >= '{ms_inputs['start_date']}'
        and date(CURRENT_DATE) <= CURRENT_DATE
        group by 1,2,3,5
        order by timestamp_display desc
        """
    else: 
        print('30 days')
        print(ms_inputs)
        return f"""
        select sg.from_address ,sg.to_address,CASE when cn.discord_user_name IS NULL
        THEN sg.to_address
        ELSE cn.discord_user_name END as user, sum(sg.amount_display), sg.timestamp_display from public.stg_subgraph_bank_1 sg
        left join coordinape_nodes cn on
        upper(sg.to_address) = upper(cn.address)
        where upper(from_address) = upper('{str(ms_inputs['wallet'])}')
        and date(timestamp_display) >= NOW() - INTERVAL '30 DAYS'
        group by 1,2,3,5
        order by timestamp_display desc
"""

def create_snapshot_query(obj):
    return f"""
    select bsh.title, to_timestamp(bsh.start_date)::date as VoteStartDate,
	count(voter) as Votes, sum(cast(bank_voting as decimal(15,2))) as BANK
from bankless_snapshot_header_1 bsh 
left join  stg_bankless_snapshot_1 sbs on
	bsh.proposal_id = sbs.proposal_id 
	group by 1,2
order by VoteStartDate desc
limit {obj['votes']}
    """

def role_activity_query(obj):
   return"""  select
days_since_latest_touchpoint_bin, role_list, discord_user_id
from vw_user_analytics user_analytics;"""


def create_users_query(obj):

    submitted_roles = obj['roles'].split(',')

    query_roles=[]
    i=1

    for r in submitted_roles:

        if i == len(submitted_roles):
            print(str(i)+ ' i first')
            
            print(i, r)
            query_roles.append('\''+r.strip())
            role_string = ''.join(query_roles)
            
        else:
            print(i, r)
            print(str(i)+ ' second')
            query_roles.append('\''+r.strip()+'\',')
            i+=1 
            
    role_string = ''.join(query_roles)  + '\'' 


    return f"""Select discord_role_name as role_name,role_activated_at_date as role_acquisition_date , count(role_activated_at_date ) from vw_discord_active_user_roles 
WHERE 

 role_activated_at_date >= date_trunc('week', CURRENT_TIMESTAMP - interval '{obj['months']}' month')
 and
 role_activated_at_date < date_trunc('week', CURRENT_TIMESTAMP)
AND 
discord_role_name IN ({role_string})
GROUP BY 1 ,2"""

def discourse_query(obj):
    return "This will work soon!"
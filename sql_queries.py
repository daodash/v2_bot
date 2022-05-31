

def create_health_query(comm_inputs):
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
    AND 
    /*PYTHON PARAMETER  - WHERE STATEMENT FOR ROLE*/
    dr.discord_role_id = {comm_inputs['discord_role_ids']}
    ),



    /*USERS WITH ROLE IN SPECIFIC PERIOD*/
    active_table as (
    SELECT u1.channel_name, u1.user, min(u1.activity_period) as days_since_active, 'Active Member Analysis' as report_name FROM active_user_messages u1
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

    inactive_table as (SELECT u4.channel_name,u3.user as user, min(u4.activity_period) as days_since_active,'Inactive Member Analysis' as report_name from users_with_roles u3
    LEFT JOIN inactive_user_messages u4 ON u3.discord_user_id = u4.discord_user_id
    WHERE u3.user NOT IN (
                            SELECT a.user from active_table a GROUP BY 1
                            )
    AND 
    u4.channel_name IS NOT NULL
    GROUP BY 1,2
    ORDER BY 3

    )

    select * from {comm_inputs['table_request']}
    """


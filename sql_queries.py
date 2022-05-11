

community_health_query ="""/* QUERY MESSAGES TABLE WITHIN PERIOD*/
with active_user_messages as (
SELECT m.channel_id,m.channel_name, m.TIMESTAMP, d.username as user,d.discord_user_id, CURRENT_DATE - m.TIMESTAMP as activity_period FROM discord_messages m
JOIN discord_user d ON d.discord_user_id = m.author_user_id 
WHERE 
/*PYTHON PARAMETER - ACTIVTY PERIOD */
m.timestamp > CURRENT_DATE - 60
AND 
/*PYTHON PARAMETER - WHERE STATEMENT FOR CHANNEL*/
m.channel_id = '840982271309250590'
),

/* GET USERS WITH SPECIFIC ROLE (role is active) */
/*what if role is partially active during period? */
users_with_roles  as (
SELECT  du.discord_user_id,du.username ,r.discord_role_id, dr.role_name FROM discord_user_roles r 
JOIN discord_roles dr ON r.discord_role_id = dr.discord_role_id
JOIN discord_user du ON du.discord_user_id = r.discord_user_id
WHERE
r.active = True
AND 
/*PYTHON PARAMETER  - WHERE STATEMENT FOR ROLE*/
dr.role_name = 'Analytics Guild'
),

/*Users with role who are active in activity period*/
active_table as (
SELECT u1.channel_name, u1.user, min(u1.activity_period) as days_since_active FROM active_user_messages u1
INNER JOIN users_with_roles u2 ON u1.discord_user_id = u2.discord_user_id
GROUP BY 1,2
ORDER BY 3
),

inactive_user_messages as (
SELECT m.channel_id,m.channel_name, m.TIMESTAMP, d.username as user,d.discord_user_id, CURRENT_DATE - m.TIMESTAMP as activity_period FROM discord_messages m
JOIN discord_user d ON d.discord_user_id = m.author_user_id 
WHERE 
/*PYTHON PARAMETER - ACTIVTY PERIOD */
m.timestamp < CURRENT_DATE - 60
AND 
/*PYTHON PARAMETER - WHERE STATEMENT FOR CHANNEL*/
m.channel_id = '840982271309250590'
),

/*Users with role who are inactive in activity period*/
inactive_table as (
SELECT u4.channel_name,u3.username, min(u4.activity_period) ,'Analytics' as Channel from users_with_roles u3
LEFT JOIN inactive_user_messages u4 ON u3.discord_user_id = u4.discord_user_id
WHERE u3.username NOT IN (
                          SELECT user from active_table GROUP BY 1
                          /* Why is this not working?*/
                          )
GROUP BY 1,2
ORDER BY 3
)

SELECT * from active_table """

print(community_health_query)
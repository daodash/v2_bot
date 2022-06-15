import pandas as pd
from sql_queries import create_health_query
from connect_to_db import db_query
from charts import *
import datetime


##get community health data
def community_health(obj):

  

    ##update sql string with user parameters
    sql_string = create_health_query(obj)
    #print(sql_string)
    
    ##call database with updated sql string
    query_results = db_query(sql_string)
    query_results.to_csv('testdata.csv')
    #print(query_results)
    
    ##create chart
    health_bar_chart(query_results,obj)



##object with parameters
# obj = {
#     'days':10,
#     'channel_id':'840982271309250590',
#     'discord_role_ids':r'Analytics Guild, Guest Pass',
#     'table_request':'active_table',
#     'user':'aar0n'
# }

# community_health(obj)





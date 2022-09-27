import pandas as pd
from sql_queries import *
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
    #print(query_results)
    
    ##create chart
    health_bar_chart(query_results,obj)

##get multisig data
def multisig_analysis(obj2):
    ##update sql string with user parameters
    sql_string = create_multisig_query(obj2)
    #print(sql_string)

    ##call database with updated sql string
    query_results = db_query(sql_string)

    ##create chart
    multisig_sankey(query_results,obj2)

def snapshot_analysis(obj):
        ##update sql string with user parameters
    sql_string = create_snapshot_query(obj)
    print(sql_string)

    ##call database with updated sql string
    query_results = db_query(sql_string)

    ##create chart
    snapshot_chart(query_results,obj)


def role_activity(obj):
    sql_string = role_activity_query(obj)
    print(sql_string)

    ##call database with updated sql string
    df = db_query(sql_string)

    ##filter for specific roles
    df['role_list'] = df['role_list'].str.lower() #convert roles_list field to lowercase
    lookup = "|".join(obj['roles'].split(',')).lower() #combining keywords with logical OR "|"
    print(obj['roles'].split(','))
    print(lookup)
    df_filter = df[df['role_list'].str.contains(lookup,na=False)]
    ##remove first 3 characters
    df_filter['days_since_latest_touchpoint_bin'] = df_filter['days_since_latest_touchpoint_bin'].str[3:]
    df_pivot = df_filter.groupby(['days_since_latest_touchpoint_bin']).count().reset_index()

        
    
    ##create chart
    role_activity_chart(df_pivot,obj)



def roles_analysis(obj):

    sql_string = create_users_query(obj)
    print(sql_string)
    query_results = db_query(sql_string)

    roles_chart(query_results,obj)

def discourse_analysis(obj):

    sql_string = discourse_query(obj)
    print(sql_string)
    query_results = db_query(sql_string)

    #discourse_chart(query_results,obj)

##obj multisig 
##obj2={
#     'wallet':'0xdfdf2d882d9ebce6c7eac3da9ab66cbfda263781',
#     'start_date':'2021-01-01',
#     'user':'aar0n'
# } 

##multisig(obj2)

##object with parameters
# obj = {
#     'days':10,
#     'channel_id':'840982271309250590',
#     'discord_role_ids':r'Analytics Guild, Guest Pass',
#     'table_request':'active_table',
#     'user':'aar0n'
# }

# community_health(obj)





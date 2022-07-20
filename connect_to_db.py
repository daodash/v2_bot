
from dependencies import creds
import psycopg2
import pandas as pd
import os

##access env variables
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

print(os.getenv('USER'))
##print(creds)

def db_query(sql_string):
#connect to database
    con = psycopg2.connect(    
    host = os.getenv('HOST'),
    database= os.getenv('DATABASE'),
    user = os.getenv('USER'),
    password = os.getenv('PASSWORD'),
    port = os.getenv('PORT'),
    sslmode =os.getenv('SSLMODE')
    )

    #create cursor
    cur = con.cursor()

    #execute query
    cur.execute(sql_string)
    rows = cur.fetchall()

    #create pandas dataframe
    columns_from_table = []
    for elt in cur.description:
        columns_from_table.append(elt[0])

    df = pd.DataFrame(data=rows,columns=columns_from_table)

    print(df)
    #close cursor
    cur.close()

    #close connection
    con.close()

    return df
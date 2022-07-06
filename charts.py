    # %%
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go



def health_bar_chart(df,obj):
    #change days since active to a number
    print(obj)
    active = obj['table_request'].split('_')[0].title()

    print(df.iat[0,0])

    df['days_since_active']=df['days_since_active'].astype(float)

    # %%
    ## chart properties
    fig = px.bar(df,x='days_since_active',y='user',orientation='h',text_auto=True)
    fig.update_layout(
        bargroupgap=.08,
        height=800,
        width=700,
        margin=dict(r=10, l=60, b=80, t=250),
        title=("<b>"+str(df.iat[0,0])+" Channel - Community Health Report</b><br>" +
            "<i>Requested by: "+obj['user']+"<i><br>" +
            "<i><b>"+active+"</b> Users in last <b>"+str(obj['days'])+"</b> days <i><br>" +
            "<i>For users with role(s): "+str(obj['discord_role_ids'].title())+"<br>"+
            "<i>Runtime:"+obj['start_time']+"<br><br>"),
        title_font_color="black",
        title_font_family="Arial",
        uniformtext_minsize=12,
        font_family="Arial"
        
    )

    fig.update_traces(
        marker_color='red',
        textposition='outside',
        marker_line_color='rgb(0,0,0)',
        marker_line_width=1.5,)
        
    ## add images
    fig.add_layout_image(
        dict(
            source=r'images\bankless-logo.png',
            xref="paper", yref="paper",
            x=1, y=1.05,
            sizex=0.2, sizey=0.2,
            xanchor="right", yanchor="bottom"
        )
    )

    fig.add_layout_image(
        dict(
            source=r'images\daodashlogo.jpg',
            xref="paper", yref="paper",
            x=.8, y=1.07,
            sizex=0.15, sizey=0.15,
            xanchor="right", yanchor="bottom"
        )
    )

    fig.write_image(r"images/CommunityHealth - "+obj['start_time']+".png")
    print (obj['start_time']+".png")
    ##use file name to know what file to send
   
#df = pd.read_csv('test2.csv').round(2)

# obj = {
#     'days':40,
#     'channel_id':'840982271309250590',
#     'discord_role_ids':'846796122907475978',
#     'table_request':'active_table',
#     'user':'aar0n'
# }

# health_bar_chart(df,obj)

def multisig_sankey(df,obj):

    ##set endpoints (from address to user)
    nodes = np.unique(df[["from_address","user"]],axis=None)
    nodes = pd.Series(index=nodes, data=range(len(nodes)))

    ##build sankey chart
    fig =  go.Figure(
            go.Sankey(
                node={"label": nodes.index},
                link={
                    "source": nodes.loc[df["from_address"]],
                    "target": nodes.loc[df["user"]],
                    "value": df["sum"],
                },
            )
        )
    ##write image
    print(obj['filename'])
    fig.write_image(r"images/"+obj['filename'])


    ##testing for multisig
# df = pd.read_csv('Multisig_-_2022-07-05_22.42.23.542698.csv')

# obj3=  {
#         'wallet':'0xe7636c7ef670a3Bcf772D9d57244c9e88aD90437',
#         'start_date':'2022-01-01',
#         'filename':'testmultisig.png',
#         'user':'aaron'
#         }
# multisig_sankey(df,obj3)

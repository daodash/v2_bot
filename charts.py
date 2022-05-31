    # %%
import pandas as pd
import plotly.express as px
import datetime

start_time = str(datetime.datetime.now()).replace(":",".")
print(start_time)

def health_bar_chart(df,obj):
    #change days since active to a number
    print(obj)


    df['days_since_active']=df['days_since_active'].astype(float)

    # %%
    ## chart properties
    fig = px.bar(df,x='days_since_active',y='user',orientation='h',text_auto=True)
    fig.update_layout(
        bargroupgap=.08,
        height=800,
        width=700,
        margin=dict(r=10, l=60, b=80, t=250),
        title=("<b>"+str(obj['channel_id'])+" Channel - Community Health Report</b><br>" +
            "<i>Requested by: aar0n<i><br>" +
            "<i><b>Inactive</b> Users in last <b>"+str(obj['days'])+"</b> days <i><br>" +
            "<i>For users with role(s): "+str(obj['discord_role_ids'])+"<br>"+
            "<i>Runtime:"+start_time+"<br><br>"),
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
    fig.show()

    fig.write_image(r"images/CommunityHealth - "+start_time+".png")

#df = pd.read_csv('test2.csv').round(2)

# obj = {
#     'days':40,
#     'channel_id':'840982271309250590',
#     'discord_role_ids':'846796122907475978',
#     'table_request':'active_table',
#     'user':'aar0n'
# }

# health_bar_chart(df,obj)

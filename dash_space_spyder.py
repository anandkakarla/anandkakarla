# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 23:53:00 2022

@author: anand
"""

# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")

#%%
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                # dcc.Dropdown(id='site-dropdown',...)
                                dcc.Dropdown(id='site-dropdown', 
                                # Update dropdown values using list comphrehension
                                options=[{'label':  'CCAFS LC-40', 'value':'OPT1'},{'label':  'CCAFS SLC-40', 'value': 'OPT2'},{'label':  'KSC LC-39A', 'value': 'OPT3'},{'label':  'VAFB SLC-4E', 'value': 'OPT4'},{'label':  'ALL SITES', 'value': 'OPT5'}],
                                value='OPT5',
                                placeholder="Select landing site",
                                searchable=True),
                                html.Br(),
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),
                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                # dcc.RangeSlider(id='payload-slider',...)
                                dcc.RangeSlider(0, 10000, 2500, value=[2500, 7500], id='payload-slider'),
                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                                             html.Div(dcc.Graph(id='success-payload-scatter-chart'))   ])
#%%
# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(
               Output(component_id='success-pie-chart', component_property='figure'),
               Input(component_id='site-dropdown', component_property='value'),
               # REVIEW4: Holding output state till user enters all the form information. In this case, it will be chart type and year
               )
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output

#%%
# Add computation to callback function and return graph
def get_graph(chart):
      
        # Select data
        # df =  airline_data[airline_data['Year']==int(year)]
       
        if chart == 'OPT1':
            
            #df1 =  spacex_df[spacex_df['Launch Site']=='CCAFS LC-40']
            df1=spacex_df.loc[spacex_df['Launch Site'] == 'CCAFS LC-40']

            # Percentage of diverted airport landings per reporting airline
            pie_fig = px.pie(data_frame=df1, names='class', title='failure and success')
            return pie_fig       
        elif chart == 'OPT2':
            
            #df1 =  spacex_df[spacex_df['Launch Site']=='CCAFS LC-40']
            df1=spacex_df.loc[spacex_df['Launch Site'] == 'CCAFS SLC-40']

            # Percentage of diverted airport landings per reporting airline
            pie_fig = px.pie(data_frame=df1, names='class', title='failure and success')
            return pie_fig    

        elif chart == 'OPT3':
            
            #df1 =  spacex_df[spacex_df['Launch Site']=='CCAFS LC-40']'
            df1=spacex_df.loc[spacex_df['Launch Site'] == 'KSC LC-39A']

            # Percentage of diverted airport landings per reporting airline
            pie_fig = px.pie(data_frame=df1, names='class', title='failure and success')
            return pie_fig     
            
    
        elif chart == 'OPT4':
            
            #df1 =  spacex_df[spacex_df['Launch Site']=='CCAFS LC-40']
            df1=spacex_df.loc[spacex_df['Launch Site'] == 'VAFB SLC-4E']

            # Percentage of diverted airport landings per reporting airline
            pie_fig = px.pie(data_frame=df1, names='class', title='failure and success')
            return pie_fig       

        else:
            # REVIEW7: This covers chart type 2 and we have completed this exercise under Flight Delay Time Statistics Dashboard section
            # Compute required information for creating graph from the data
             df1 =  spacex_df
            
            # Percentage of diverted airport landings per reporting airline
             pie_fig = px.pie(df1, values='class', names='Launch Site', title='success rate distribution')
             return pie_fig   
         
            
@app.callback(
      Output(component_id='success-payload-scatter-chart', component_property='figure'),
      [Input(component_id='site-dropdown', component_property='value'),Input(component_id='payload-slider', component_property='value')],
      # REVIEW4: Holding output state till user enters all the form information. In this case, it will be chart type and year
      )
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output

#%%
# Add computation to callback function and return graph
def get_graph2(chart,sliderV):
  
    # Select data
    # df =  airline_data[airline_data['Year']==int(year)]
    df2 = spacex_df[(spacex_df['Payload Mass (kg)']>=sliderV[0])
        &(spacex_df['Payload Mass (kg)']<=sliderV[1])]   

    if chart == 'OPT1':
        
        #df1 =  spacex_df[spacex_df['Launch Site']=='CCAFS LC-40']
        df1=df2.loc[df2['Launch Site'] == 'CCAFS LC-40']

        # Percentage of diverted airport landings per reporting airline
        scatter_fig = px.scatter(data_frame=df1,x="Payload Mass (kg)", y="class", color="Booster Version Category")
        return scatter_fig       
    elif chart == 'OPT2':
        
        #df1 =  df2[df2['Launch Site']=='CCAFS LC-40']
        df1=df2.loc[df2['Launch Site'] == 'CCAFS SLC-40']

        # Percentage of diverted airport landings per reporting airline
        scatter_fig = px.scatter(data_frame=df1,x="Payload Mass (kg)", y="class",color="Booster Version Category")
        return scatter_fig    

    elif chart == 'OPT3':
        
        #df1 =  df2[df2['Launch Site']=='CCAFS LC-40']'
        df1=df2.loc[df2['Launch Site'] == 'KSC LC-39A']

        # Percentage of diverted airport landings per reporting airline
        scatter_fig = px.scatter(data_frame=df1,x="Payload Mass (kg)", y="class",color="Booster Version Category")
        return scatter_fig     
        

    elif chart == 'OPT4':
        
        #df1 =  df2[df2['Launch Site']=='CCAFS LC-40']
        df1=df2.loc[df2['Launch Site'] == 'VAFB SLC-4E']

        # Percentage of diverted airport landings per reporting airline
        scatter_fig = px.scatter(data_frame=df1, x="Payload Mass (kg)", y="class", color="Booster Version Category")
        return scatter_fig       

    else:
        # REVIEW7: This covers chart type 2 and we have completed this exercise under Flight Delay Time Statistics Dashboard section
        # Compute required information for creating graph from the data
         df1 =  df2
        
        # Percentage of diverted airport landings per reporting airline
         scatter_fig = px.scatter(df1, x="Payload Mass (kg)", y="class", color="Booster Version Category")
         return scatter_fig  

            
# Run the app
if __name__ == '__main__':
    app.run_server()

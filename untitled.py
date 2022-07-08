import streamlit as st
import numpy as np
import pandas as pd
#Librabries to import
import pandas as pd 
import pathlib
import os
from pathlib import Path
from pathlib import PurePath
import numpy as np
import plotly.io as pio
import plotly.graph_objs as go
import statistics
import plotly.express as px
import random
import matplotlib.pyplot as plt


from PIL import Image

img=Image.open("logo.png")
st.image(img,width=210)

with st.sidebar:
    st.title('Demand Supply ')
    
st.markdown(
         f"""
         <style>
         .stApp {{
             
             background-color: #F8F8F8
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

st.markdown('Select Supply Growth %')
Supply = st.select_slider('',options=['5', '10', '12', '15'])
st.markdown('Select Demand Growth %')
Demand = st.select_slider(' ',options=['5', '10', '15', '20', '25'])
 
 
Slider_Cursor = st.markdown(''' <style> div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
    background-color: #34e834; box-shadow: #34e834 0px 0px 0px 0.2rem;} </style>''', unsafe_allow_html = True)




if (Supply == '5' and Demand == '5'):
    
    # Assuming increase of next ten years
    supply_increase_demand = 1.05 # 10% increase
    supply_increase_supply = 1.05 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
    


    Demand_est_growth_mean = 0.07
    Demand_est_growth_std = 0.145

    Supply_est_growth_mean = 0.05
    Supply_est_growth_std = 0.0175



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
    
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig)
    
if (Supply == '5' and Demand == '10'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.10 # 10% increase
    supply_increase_supply = 1.05 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
    


    Demand_est_growth_mean = 0.11
    Demand_est_growth_std = 0.141

    Supply_est_growth_mean = 0.05
    Supply_est_growth_std = 0.0175



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
    
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig)

if (Supply == '5' and Demand == '15'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.15 # 10% increase
    supply_increase_supply = 1.05 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
    

    Demand_est_growth_mean = 0.14
    Demand_est_growth_std = 0.141

    Supply_est_growth_mean = 0.05
    Supply_est_growth_std = 0.0175



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig)

if (Supply == '5' and Demand == '20'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.20 # 10% increase
    supply_increase_supply = 1.05 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)



    Demand_est_growth_mean = 0.18
    Demand_est_growth_std = 0.145

    Supply_est_growth_mean = 0.05
    Supply_est_growth_std = 0.0175



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
    
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig)



if (Supply == '5' and Demand == '25'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.25 # 10% increase
    supply_increase_supply = 1.05 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
     


    Demand_est_growth_mean = 0.21
    Demand_est_growth_std = 0.152

    Supply_est_growth_mean = 0.05
    Supply_est_growth_std = 0.0175



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig)

if (Supply == '10' and Demand == '5'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.05 # 10% increase
    supply_increase_supply = 1.10 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
     


    Demand_est_growth_mean = 0.07
    Demand_est_growth_std = 0.145

    Supply_est_growth_mean = 0.09
    Supply_est_growth_std = 0.029



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig)



if (Supply == '10' and Demand == '10'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.20 # 10% increase
    supply_increase_supply = 1.10 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
     


    Demand_est_growth_mean = 0.11
    Demand_est_growth_std = 0.141

    Supply_est_growth_mean = 0.09
    Supply_est_growth_std = 0.029



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    

    st.plotly_chart(fig)
if (Supply == '10' and Demand == '20'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.20 # 10% increase
    supply_increase_supply = 1.10 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
     


    Demand_est_growth_mean = 0.18
    Demand_est_growth_std = 0.145

    Supply_est_growth_mean = 0.09
    Supply_est_growth_std = 0.029



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    

    st.plotly_chart(fig)
if (Supply == '10' and Demand == '15'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.05 # 10% increase
    supply_increase_supply = 1.10 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
     


    Demand_est_growth_mean = 0.14
    Demand_est_growth_std = 0.141

    Supply_est_growth_mean = 0.09
    Supply_est_growth_std = 0.029



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    
    st.plotly_chart(fig)
if (Supply == '10' and Demand == '25'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.05 # 10% increase
    supply_increase_supply = 1.10 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
     

    Demand_est_growth_mean = 0.21
    Demand_est_growth_std = 0.152

    Supply_est_growth_mean = 0.09
    Supply_est_growth_std = 0.029



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    
    st.plotly_chart(fig)

if (Supply == '12' and Demand == '5'):
# Assuming increase of next ten years
    supply_increase_demand = 1.05 # 10% increase
    supply_increase_supply = 1.12 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
     


    Demand_est_growth_mean = 0.07
    Demand_est_growth_std = 0.145

    Supply_est_growth_mean = 0.10
    Supply_est_growth_std = 0.0377



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    st.plotly_chart(fig)
if (Supply == '12' and Demand == '10'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.15 # 10% increase
    supply_increase_supply = 1.12 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
     


    Demand_est_growth_mean = 0.11
    Demand_est_growth_std = 0.141

    Supply_est_growth_mean = 0.10
    Supply_est_growth_std = 0.0377



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    
    st.plotly_chart(fig)
if (Supply == '12' and Demand == '15'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.15 # 10% increase
    supply_increase_supply = 1.12 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
     


    Demand_est_growth_mean = 0.14
    Demand_est_growth_std = 0.141

    Supply_est_growth_mean = 0.10
    Supply_est_growth_std = 0.0377



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    
    st.plotly_chart(fig)
if (Supply == '12' and Demand == '20'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.20 # 10% increase
    supply_increase_supply = 1.12 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
     


    Demand_est_growth_mean = 0.18
    Demand_est_growth_std = 0.145

    Supply_est_growth_mean = 0.10
    Supply_est_growth_std = 0.0377



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    
    st.plotly_chart(fig)
if (Supply == '12' and Demand == '25'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.25 # 10% increase
    supply_increase_supply = 1.12 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
    


    Demand_est_growth_mean = 0.21
    Demand_est_growth_std = 0.152

    Supply_est_growth_mean = 0.10
    Supply_est_growth_std = 0.0377



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    
    st.plotly_chart(fig)

if (Supply == '15' and Demand == '5'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.05 # 10% increase
    supply_increase_supply = 1.15 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
     


    Demand_est_growth_mean = 0.21
    Demand_est_growth_std = 0.152

    Supply_est_growth_mean = 0.12
    Supply_est_growth_std = 0.0506



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    
    st.plotly_chart(fig)
if (Supply == '15' and Demand == '10'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.15 # 10% increase
    supply_increase_supply = 1.15 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
     


    Demand_est_growth_mean = 0.11
    Demand_est_growth_std = 0.141

    Supply_est_growth_mean = 0.12
    Supply_est_growth_std = 0.050



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    

    st.plotly_chart(fig)
if (Supply == '15' and Demand == '15'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.15 # 10% increase
    supply_increase_supply = 1.15 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
    


    Demand_est_growth_mean = 0.07
    Demand_est_growth_std = 0.145

    Supply_est_growth_mean = 0.12
    Supply_est_growth_std = 0.050



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
    
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    
    st.plotly_chart(fig)
if (Supply == '15' and Demand == '20'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.20 # 10% increase
    supply_increase_supply = 1.15 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
     


    Demand_est_growth_mean = 0.18
    Demand_est_growth_std = 0.145

    Supply_est_growth_mean = 0.12
    Supply_est_growth_std = 0.050



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    
    st.plotly_chart(fig)

if (Supply == '15' and Demand == '25'):
    # Assuming increase of next ten years
    supply_increase_demand = 1.25 # 10% increase
    supply_increase_supply = 1.15 # 9% increa
    year_range =  list(range(2022, 2030))

    # calculated mean and stds of demand and supply data
    ## Data import from excel to dataframe 
    file_name = 'updated_data_supply_demand.xlsx'
    demand_supply_historial_data=  pd.read_excel(file_name)
     


    Demand_est_growth_mean = 0.21
    Demand_est_growth_std = 0.152

    Supply_est_growth_mean = 0.12
    Supply_est_growth_std = 0.050



    data_temp_supply = []
    data_temp_demand = []
    growth_increase_supply_df = []
    growth_increase_demand_df = []
    year = []
    for ii in year_range:
        #print(ii)
        if ii == year_range[0]:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(76503.21)
            data_temp_demand.append(50520.6)
            year.append(ii)          
        else:
            growth_increase_supply =  random.triangular( Supply_est_growth_mean- Supply_est_growth_std, Supply_est_growth_mean*2,  Supply_est_growth_mean +  Supply_est_growth_std )
            growth_increase_supply_df.append(growth_increase_supply) 
            growth_increase_demand =  random.triangular(Demand_est_growth_mean -Demand_est_growth_std, Demand_est_growth_mean*2, Demand_est_growth_mean +Demand_est_growth_std)
            growth_increase_demand_df.append(growth_increase_demand)     
            data_temp_supply.append(data_temp_supply[-1]*(1+growth_increase_supply))
            data_temp_demand.append(data_temp_demand[-1]*(1+growth_increase_demand))
            year.append(ii)

    
    d = {'Year': year, 'Yearly Supply':data_temp_supply, 'Yearly Demand':data_temp_demand, 'Yearly Supply change':growth_increase_supply_df,
    'Yearly Demand change':growth_increase_demand_df,  }
    df = pd.DataFrame(data=d)
     
    # Plot each element of graph as separate scatter figure
    fig =go.Figure()
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Supply']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#9467bd', width=6),name="Yearly Supply",))
    fig.add_trace(go.Scatter(x=demand_supply_historial_data['Year'], y=demand_supply_historial_data['Demand']
        , mode='lines +markers',marker_symbol=2,marker_size = 15,line = dict(color='#1f77b4', width=6),name="Yearly Demand",))

    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Supply'], name="Yearly Supply (Forecast)",line=dict(color="#F06A6A", dash="dash", width=6,)))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Yearly Demand'], name="Yearly Demand (Forecast)",line=dict(color="#1f77b4", dash="dash", width=6,)))
    fig.update_layout(
        legend_orientation="v",
        yaxis_title="Supply (graduates) vs Demand (vacancies)",
        xaxis_title="Year",
        title = "Supply (graduates) vs Demand (vacancies)",
        font=dict(
        family="Franklin Gothic",
        size=20,
        color="#7f7f7f"
        ), 
        legend=dict(
                x=0,
                y=1))
    fig.update_layout(
        title={
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    sliders = [dict(
        active=10,
        currentvalue={"prefix": "Frequency: "},
        pad={"t": 50},
        
    )]

    fig.update_layout(
        sliders=sliders
    )
    
    st.plotly_chart(fig)

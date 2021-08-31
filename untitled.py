import streamlit as st
import numpy as np
import pandas as pd


from PIL import Image

img=Image.open("0.png")
st.image(img,width=910)
choices = st.sidebar.selectbox(
    'What would you like to perform?',
    ('Compensation Data Analysis','Company Performance', 'Historic Trends','Predictive')
)

df = pd.read_excel('CEO.xlsx')
Company = pd.read_excel('company.xlsx')
CMO = df[df['Sector'] == 'CMO']
Pharma = df[df['Sector']=='Pharma']

CMO_Company = Company[Company['Sector'] == 'CMO']
Pharma_Company = Company[Company['Sector'] == 'Pharma']


import plotly.express as px
img=Image.open("undraw_Charts_re_5qe9.png")
st.sidebar.image(img,width=299)

if choices == 'Compensation Data Analysis':
    st.header("Compensation")
    
    
    st.subheader("Total Compensation")
    choices = st.selectbox(
    'What would you like to perform?',
    ('CMO','Pharma'))
    if choices == 'CMO':
        
        
    
        CMO.sort_values('Total Salary', axis = 0, ascending = True,inplace = True, na_position ='last')
        fig = px.bar(CMO, y=CMO['Total Salary'], x=CMO['Company'], text=CMO['Total Salary'],color=CMO['Total Salary'],
                     color_continuous_scale=["#b3e0a6", "#5ea654", "#24693d"])



        st.plotly_chart(fig)
    
    if choices == 'Pharma':
    
        CMO.sort_values('Total Salary', axis = 0, ascending = True,inplace = True, na_position ='last')
        fig = px.bar(Pharma, y=Pharma['Total Salary'], x=Pharma['Company'], text=Pharma['Total Salary'],color=Pharma['Total Salary'],
                     color_continuous_scale=["#b3e0a6", "#5ea654", "#24693d"])



        st.plotly_chart(fig)
    
    st.subheader("Base Compensation")
    hoices = st.selectbox(
    'What would you like  to perform?',
    ('CMO - Base Compensation','Pharma- Base Compensation'))
    
    if hoices == 'CMO - Base Compensation':
        CMO.sort_values('Basic Salary', axis = 0, ascending = True,inplace = True, na_position ='last')
        fig = px.bar(CMO, y=CMO['Basic Salary'], x=CMO['Company'], text=CMO['Basic Salary'],color=CMO['Basic Salary'],
                             color_continuous_scale=["#b3e0a6", "#5ea654", "#24693d"],labels={
                             "Company": "Companies",
                             "Basic Salary": "Base Compensation - Million USD",
                             "species": "Species of Iris"
                         },
                        title="CMO-Base compensation Pencentiles")
        



        st.plotly_chart(fig)
    
    if hoices == 'Pharma- Base Compensation':
        Pharma.sort_values('Basic Salary', axis = 0, ascending = True,inplace = True, na_position ='last')
        fig = px.bar(Pharma, y=Pharma['Basic Salary'], x=Pharma['Company'], text=Pharma['Basic Salary'],color=Pharma['Basic Salary'],
                             color_continuous_scale=["#b3e0a6", "#5ea654", "#24693d"],labels={
                             "Company": "Companies",
                             "Basic Salary": "Base Compensation - Million USD",
                             "species": "Species of Iris"
                         },
                        title="Pharma-Base compensation Pencentiles")
        st.plotly_chart(fig)
        
    st.subheader("Total Compensation Versus Turnover")
    oices = st.selectbox(
    'What would you like  to perform?',
    ('CMO - Total Compensation Versus Turnover','Pharma- Total Compensation Versus Turnover'))
    import plotly.graph_objects as go
    
    if oices == 'CMO - Total Compensation Versus Turnover':
        fig = go.Figure(data=[
        go.Bar(name='Total Compensation',x=CMO_Company['Company'],marker=dict(color='#b3e0a6'), y=CMO['Total Salary'], text=CMO['Total Salary'],textposition= 'outside'),
        go.Bar(name='Turnover',x=CMO_Company['Company'],marker=dict(color='#5ea654'),y=CMO_Company['Turnover'],text=CMO_Company['Turnover'],textposition= 'outside')
    ])
    # Change the bar mode
    fig.update_layout(barmode='group')
    st.plotly_chart(fig)
    
    if oices == 'Pharma- Total Compensation Versus Turnover':
        import plotly.graph_objects as go

        fig = go.Figure(data=[
            go.Bar(name='Total Compensation',x=Pharma['Company'],marker=dict(color='#b3e0a6'), y=Pharma['Total Salary'], text=Pharma['Total Salary'],textposition= 'outside'),
            go.Bar(name='Turnover',x=Pharma_Company['Company'],marker=dict(color='#5ea654'),y=Pharma_Company['Turnover'],text=Pharma_Company['Turnover'],textposition= 'outside')
        ])
        # Change the bar mode
        fig.update_layout(barmode='group')
        
    
        st.plotly_chart(fig)
    
    
    
    
    
    
    
    
    
    
    
if choices == 'Company Performance':
    import plotly.graph_objects as go
    choices = st.selectbox(
    'What would you like to perform?',
    ('CMO','Pharma'))
    if choices == 'CMO':

        fig = go.Figure(data=[
            go.Bar(name='No of Employee',x=CMO_Company['Company'],marker=dict(color='#b3e0a6'), y=CMO_Company['Number of Employees']/10000),
            go.Bar(name='Net Income',x=CMO_Company['Company'],marker=dict(color='#5ea654'),y=CMO_Company['Net Income'])
        ])
        # Change the bar mode
        fig.update_layout(barmode='group')
        #fig.update_traces(marker=dict(color='green'))
        st.plotly_chart(fig)
    if choices == 'Pharma':
    
        import plotly.graph_objects as go

        fig = go.Figure(data=[
            go.Bar(name='No of Employee',x=Pharma_Company['Company'],marker=dict(color='#b3e0a6'), y=Pharma_Company['Number of Employees']/10000),
            go.Bar(name='Net Income',x=Pharma_Company['Company'],marker=dict(color='#5ea654'),y=Pharma_Company['Net Income'])
        ])
        # Change the bar mode
        fig.update_layout(barmode='group')
        #fig.update_traces(marker=dict(color='green'))
        st.plotly_chart(fig)


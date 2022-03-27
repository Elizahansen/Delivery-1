# App  
# Eliza Mathisen Hansen, KEA, Delivery 1

############################## Imports #####################
from turtle import color
from matplotlib.colors import rgb2hex
import dash
from dash import html
from dash import dcc 
from dash.dependencies import Input, Output

# Div.
import pandas as pd
import numpy as np
import calendar

# Plotly
import plotly.express as px
import plotly.graph_objects as go

############################## Get data #####################
import Database_connect as myDB
thisConn = myDB.dbconnect()

# Data
SQL_data_empsales = pd.read_sql_query("select * from employeesales", thisConn)
SQL_data_prosales = pd.read_sql_query("select * from categorysales", thisConn)

########## Diagram - Employee Sales & Product Sales #########
fig_employee=px.histogram(SQL_data_empsales,x='employee_id', y='sold', title='Employee sales' ) 
fig_employee.update_layout(bargap=0.2) 
fig_product=px.histogram(SQL_data_prosales,x='productname', y='sold', title='Product sales' )

dash_app=dash.Dash(__name__)
app=dash_app.server

######################## Layout ###########################
dash_app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.H1(children='Sales report for employees'),

        html.Div(children='''
            Her skal stå noget sejt.
        '''),

        dcc.Graph(
            id='employeesales',
            figure=fig_employee
        ),  
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.H1(children='Sales report for products'),

        html.Div(children='''
            Her skal stå noget sejt.
        '''),

        dcc.Graph(
            id='categorysales',
            figure=fig_product
        ),  
    ]),
])

##################### Run the app #######################
if __name__ == '__main__':
    dash_app.run_server(debug=True)
## set up dashboard display
## use flask to set up the dashboard

from flask import Flask, render_template
import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
import numpy as np
import os

# set up the flask app
server = Flask(__name__)

# set up the dash app
app = dash.Dash(__name__, server=server)

# read in the CDC data
# set path to the data
path = os.getcwd()
filepath = path + '/U.S._Chronic_Disease_Indicators.csv'

cdc_data = pd.read_csv(filepath)

# create a list of the unique states
states = cdc_data['LocationDesc'].unique()

# create a list of the unique indicators
indicators = cdc_data['Question'].unique()

# create a list of the unique years
years = cdc_data['YearStart'].unique()

# create app layout
app.layout = html.Div([
    html.H1('CDC Chronic Disease Indicators'),
    html.Div([
        html.Label('Select State'),
        dcc.Dropdown(
            id='state-dropdown',
            options=[{'label': state, 'value': state} for state in states],
            value='Alabama'
        )
    ]),
    html.Div([
        html.Label('Select Indicator'),
        dcc.Dropdown(
            id='indicator-dropdown',
            options=[{'label': indicator, 'value': indicator} for indicator in indicators],
            value='Current asthma prevalence among adults aged >= 18 years'
        )
    ]),
    # daterange picker (start and end year)
    html.Div([
        html.Label('Start Year'),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': year, 'value': year} for year in years],
            value=2011
        ),
    ]),
    # end daterange picker
    html.Div([
        html.Label('End Year'),
        dcc.Dropdown(
            id='year-dropdown',
            options=[{'label': year, 'value': year} for year in years],
            value=2011
        ),


    dcc.Graph(id='indicator-graph')
])


@app.callback(
    dash.dependencies.Output('indicator-graph', 'figure'),
    [dash.dependencies.Input('state-dropdown', 'value'),
     dash.dependencies.Input('indicator-dropdown', 'value'),
     dash.dependencies.Input('year-dropdown', 'value')]
)
def update_graph(selected_state, selected_indicator, selected_year):
    filtered_data = cdc_data[
        (cdc_data['LocationDesc'] == selected_state) &
        (cdc_data['Question'] == selected_indicator) &
        (cdc_data['YearStart'] == selected_year)   ]
    # convert data value to numeric
    filtered_data['DataValue'] = pd.to_numeric(filtered_data['DataValue'], errors='coerce')
    fig = px.bar(filtered_data, x='DataValue', y='StratificationCategory1', orientation='h')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

# run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)
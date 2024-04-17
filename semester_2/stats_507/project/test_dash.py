import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback_context, dash_table
import plotly.express as px
from flask import Flask

# Reading the data from the zipped CSV file
cdc_data = pd.read_csv('cdc_data.zip', compression='zip')

# Flask server setup
server = Flask(__name__)

# Initialize the Dash app and suppress callback exceptions
app = Dash(__name__, server=server, suppress_callback_exceptions=True)

# Utility function to create dropdown options
def create_dropdown_options(column_name):
    unique_values = sorted(cdc_data[column_name].dropna().unique())
    return [{'label': item, 'value': item} for item in unique_values]

# Define the application layout with tabs for data table and line chart
app.layout = html.Div([
    html.H1("CDC Data Dashboard"),
    
    # Dropdown filters
    html.Div([
        html.Label('Select State:'),
        dcc.Dropdown(
            id='location-dropdown',
            options=create_dropdown_options('LocationAbbr'),
            value=None  # Default value is intentionally None for no selection
        ),
        
        html.Label('Select Question:'),
        dcc.Dropdown(
            id='question-dropdown',
            options=create_dropdown_options('Question'),
            value=None  # Default value is intentionally None for no selection
        ),
        
        html.Label('Select Stratification Category:'),
        dcc.Dropdown(
            id='strat-category-dropdown',
            options=create_dropdown_options('StratificationCategory1'),
            value=None  # Default value is intentionally None for no selection
        ),
        
        html.Label('Select Data Value Type:'),
        dcc.Dropdown(
            id='data-value-type-dropdown',
            options=create_dropdown_options('DataValueType'),
            value=None  # Default value is intentionally None for no selection
        ),
    ], className="filters-panel"),
    
    # Tabs for switching between DataTable and LineChart
    dcc.Tabs(id='tabs', children=[
        dcc.Tab(label='Data Table', value='tab-datatable'),
        dcc.Tab(label='Line Chart', value='tab-linechart'),
    ]),
    
    # Div that will contain the content of the tabs
    html.Div(id='tabs-content')
])

# Callback for rendering tab content dynamically
@app.callback(
    Output('tabs-content', 'children'),
    [
        Input('tabs', 'value'),
        Input('location-dropdown', 'value'),
        Input('question-dropdown', 'value'),
        Input('strat-category-dropdown', 'value'),
        Input('data-value-type-dropdown', 'value')
    ]
)
def render_tab_content(tab, state, question, strat_category, data_value_type):
    # Use callback context to prevent triggering before all dropdowns are set
    if not (state and question and strat_category and data_value_type):
        triggered = callback_context.triggered[0]
        if not triggered['value']:  # Nothing has triggered the callback yet
            return html.Div("Please select filters above to show data.")
        else:
            return html.Div("Select values from all dropdowns to see results.")

    # Apply filtering based on the selected dropdown options
    filtered_df = cdc_data[
        (cdc_data['LocationAbbr'] == state) &
        (cdc_data['Question'] == question) &
        (cdc_data['StratificationCategory1'] == strat_category) &
        (cdc_data['DataValueType'] == data_value_type)
    ]

    # Choose what to render based on the selected tab
    if tab == 'tab-datatable':
        if filtered_df.empty:
            return html.Div("No data available for the selected criteria.")
        else:
            # Define columns to display in the Data Table
            columns = ['YearStart', 'LocationAbbr', 'Question',
                       'DataValue',
                       'StratificationCategory1',
                       'StratificationCategory2']
            # Return DataTable with filtering applied
            return dash_table.DataTable(
                data=filtered_df.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in filtered_df.columns if i in columns],
                page_size=10,
                style_table={'overflowY': 'auto'}  # Make the table horizontally scrollable
            )
    elif tab == 'tab-linechart':
        if filtered_df.empty:
            return html.Div("No data available for the selected criteria.")
        else:
            # Check if we should use stratification for the line chart
            if strat_category and strat_category != "Overall":
                # Generate and return LineChart figure with Stratification 2
                figure = px.line(
                    filtered_df,
                    x='YearStart',
                    y='DataValue',
                    color='StratificationCategory2'  # Differentiating lines by Stratification Category 2
                )
            else:
                # Generate and return LineChart without Stratification 2
                figure = px.line(
                    filtered_df,
                    x='YearStart',
                    y='DataValue'
                )
            return dcc.Graph(figure=figure)
    else:
        return html.Div("Something went wrong. Please try selecting the filters again.")

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
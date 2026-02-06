import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# We will load the cleaned sales csv file from previous task
df = pd.read_csv("Sales_data.csv")
# print(df)

# We will check how the date is stored
# print(df.info())

# we need to ensure that date is treated as datetime object so it can be formatted and plotted correctly
df['Date'] = pd.to_datetime(df['Date'])
# print(df.info())

# We will now initialze the dash app and define its layout
app = Dash(__name__, title="Pink Morsel Sales Dashboard")


# Function to generate the figure based on selected region
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales Trend ({selected_region.capitalize()})",
        labels={"Date": "Date", "Sales": "Sales in $"},
    )

    fig.update_layout(
        title_x=0.5,
        plot_bgcolor="#f9f9f9",
        paper_bgcolor="#ffffff",
        font=dict(size=14)
    )

    return fig


# We will now define the title of the dashboard
app.layout = html.Div(children=[

    html.H1(
        "Pink Morsel Sales Visualization Graph",
        className="page-title"
    ),

    html.Div(
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            className="radio-style"
        ),
        style={"textAlign": "center"}
    ),

    # Graph starts empty which callback fills it
    dcc.Graph(id="sales-line-chart", figure={})
])


# We will import the required libraries for making the line graph responsive
from dash.dependencies import Input, Output

# Defining the function to trigger by input and output values
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)

# Update and return the chart
def update_graph(selected_region):
    return update_chart(selected_region)


# Deploy the app server
if __name__ == "__main__":
    print("Server has initialized...")
    app.run(debug=True)

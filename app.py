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

# We will now use plotly to create line chart to visualize the Pink morsel sales over time
fig = px.line(
    df,
    x = "Date",
    y = "Sales",
    title = "Pink Morsel Sales Trend Over Time",
    labels = {"Date": "Date", "Sales": "Sales in $"}
)

# We will now initialze the dash app and define its layout
app = Dash(__name__)

# We will define its layout now
app.layout = html.Div(children = [
    html.H1(
        "Pink Morsel Sales Visualization Graph" ,
        style = { "textAlign": "center"}
    ),

    dcc.Graph(
        id = "sales-line-chart",
        figure = fig
    )
])

print("Reached server start...")
# Deploy the app server
if __name__ == "__main__":
    app.run(debug=True)
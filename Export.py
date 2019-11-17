import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv("C:/src/Python/DataVisualizationProjects/RealEstateReal Estate Data YOY .csv")
print(df.head())

i = 0
cols = [col for col in df.columns]
cols =  cols[1:] #all our data columns for each year
for col in cols:
    fig = go.Figure(data=go.Choropleth( 
        locations=df['State'], # Spatial coordinates
        z = df[col].astype(float), # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        colorscale = 'viridis',
        showscale=True,
    ))

    fig.update_layout(
        title_text = 'Percent Change In Sales Price - ' + str(col),
        geo_scope='usa', # limite map scope to USA
    )
    fig.write_image(f"C:/Users/jingl/Videos/Youtube/Plotting Maps with Python/Tests/test{i}.png", width=1920, height=1080)
    i += 1


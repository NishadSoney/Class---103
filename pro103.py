import pandas as pd
import plotty.express as px

df = pd.read_csv("Copy+of+data+-+data.csv")
fig = px.scatter(df, x = "Date", y = "Number of cases", size = "Percentage", color = "Coutry", size_max = 15)

fig.show()
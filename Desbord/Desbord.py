import pandas as pd
import numpy as np 
import plotly.express as px
import plotly.graph_objects as go

Database = pd.read_csv("apple_products.csv")
# print(Database.head())
# print(Database.isnull().sum())
# print(Database.describe())

Heigthest_reated = Database.sort_values(by = "Star Rating",ascending=False)
Heigthest_reated = Heigthest_reated.head(10)
# print(Heigthest_reated['Product Name'])

iphone = Heigthest_reated['Product Name'].value_counts()
Graph = iphone.index
count = Heigthest_reated['Ram']

figure = px.bar(Heigthest_reated,x=Graph,y=count,title="Number of heigest reated iphon")

figure.show()
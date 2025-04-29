import matplotlib.pyplot as plt
from pathlib import Path 
import csv
import plotly.express as px
import pandas as pd 

path = Path('eq_data\world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
head_row = next(reader)
print(head_row)

lons, lats, bnes = [], [], []
for row in reader:
    lon = float(row[1])
    lat = float(row[0])
    bne = float(row[2])
    lons.append(lon)
    lats.append(lat)
    bnes.append(bne)

data = pd.DataFrame(
    data=zip(lons, lats, bnes), columns=['经度','纬度','火灾强度']
)

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    title='各地火灾强度分布图',
    color='火灾强度',
    size='火灾强度',
    size_max=10
)

fig.write_html('fire.html')
fig.show()
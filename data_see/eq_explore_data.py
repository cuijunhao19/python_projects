from pathlib import Path
import json
import plotly.express as px
import pandas as pd 

# 数据作为字符串读取并转换为Python对象
path = Path('eq_data\eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# # 将数据⽂件转换为更易于阅读的版本
# path = Path('eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

# 查看数据集中的所有地震
all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

mags, titles, lons, lats = [], [], [], [] 
for eq_dict in all_eq_dicts:
    try:
        mag = eq_dict['properties']['mag']
        title = eq_dict['properties']['title']
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
    except ValueError:
        print("Data is not exist!")
    mags.append(mag)
    titles.append(title) 
    lons.append(lon) 
    lats.append(lat) 

data = pd.DataFrame(
     data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
)
data.head()

fig = px.scatter(
    x = lons,
    y = lats,
    labels={'x':'经度', 'y':'纬度'},
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title=('全球地震散点图')
)

fig.write_html('global_earthquakes.html')
fig.show()
import json
import requests
import pandas as pd
from sqlalchemy import create_engine

url = "http://opendata2.epa.gov.tw/AQI.json"
df = pd.read_json(url)
engine = create_engine('sqlite:///:memory:')
df.to_sql('AQI_table', engine, index=False)
#print(df)
county = "臺北市"
avg = 10
query = "select \"County\", \"SiteName\", \"AQI\", \"PM2.5_AVG\", Status from AQI_table where \"County\" = ? and \"PM2.5_AVG\" > ? \
                        order by cast(\"PM2.5_AVG\" as int) desc"
print(pd.read_sql_query(query,engine, params=[county, avg]))
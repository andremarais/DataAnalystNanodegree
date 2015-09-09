from pandas import *
from ggplot import *
import pandasql

df = pandas.read_csv('C:/Udacity/Data Science/Data Visualizing/turnstile_data_master_with_weather.csv')

df.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

q = """
SELECT
daten,
sum(entriesn_hourly) as DailyEntries,
avg(mintempi) as AveTemp,
avg(rain) as Rain

FROM
df

GROUP BY
daten
"""

df_ss = pandasql.sqldf(q.lower(), locals())
df_ss.daten = pandas.to_datetime(df_ss.daten)

plot = ggplot(df_ss, aes(x = 'daten', y = 'dailyentries', shape = 'rain')) + geom_point() + geom_line()

print plot
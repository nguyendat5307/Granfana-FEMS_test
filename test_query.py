from influxdb import InfluxDBClient
import pandas
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'Savina')
data = client.query('select * from GateWay02 where "tag" = \'I2:Total_Energy\'').get_points()
df_data = pandas.DataFrame(data).set_index('time')
df_data.index = pandas.to_datetime(df_data.index)
print(df_data.resample('1H').max())
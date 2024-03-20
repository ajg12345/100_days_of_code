import pandas

# in a pandas dataframe every column is a series
data = pandas.read_csv('weather_data.csv')
# print(data['temp'])


# print average
temp_list = data['temp'].to_list()
temp_len = len(temp_list)
# print(sum(temp_list)/temp_len)
# or
# print(data['temp'].mean())
# print(data['temp'].max())


# series access
# print(data.temp)


# row access
print(data[data.temp.max() == data.temp])

# create a new dataframe and save it to a csv
my_data = {'big': [1,2,3], 'small': [4,5,6]}
my_dataframe = pandas.DataFrame(my_data)
my_dataframe.to_csv('my_data.csv')

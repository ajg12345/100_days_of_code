import pandas

#read some squirrel data and run some computations
# how many grey, how many cinnamon, how many black


# in a pandas dataframe every column is a series
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey_count = data[data['Primary Fur Color'] == 'Gray']['Primary Fur Color'].count()
cinnamon_count = data[data['Primary Fur Color'] == 'Cinnamon']['Primary Fur Color'].count()
black_count = data[data['Primary Fur Color'] == 'Black']['Primary Fur Color'].count()
squirrels = pandas.DataFrame({'Grey':grey_count, 'Cinnamon':cinnamon_count, 'Black':black_count}, index=[0])
squirrels.to_csv('squirrel_counts.csv')
# print(data['temp'])


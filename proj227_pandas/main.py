
data = []
with open('weather_data.csv') as wea:
    file = wea.read()
    data = file.split('\n')

print(data)

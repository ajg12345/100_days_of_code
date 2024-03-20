import csv

temps = []
with open('weather_data.csv') as wea:
    data = csv.reader(wea)
    for row in data:
        if row[1].isdigit():
            temps.append(int(row[1]))

print(temps)



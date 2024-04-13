import csv
import folium
import webbrowser

def auto_open(path):
    html_page = f'{path}'
    webbrowser.open(html_page, new=2)

filename = 'ShuttleData.csv'
keys = ('Longitude', 'Latitude')
records = []

with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        records.append({key: row[key] for key in keys}) # populates records with the longitude and latitude of each shuttle destiantion

for record in records:
    longitude, latitude = record['Longitude'], record['Latitude']
    record['Longitude'] = float(longitude)
    record['Latitude'] = float(latitude)

map = folium.Map(location=[29.9652, -90.108948], zoom_start=20) # starts zoom in map.html close to school
map.save('map.html')

auto_open('templates/map.html')
import csv
import re
from unshortenit import UnshortenIt

unshortener = UnshortenIt()
final = open('locations_coordinates.csv', mode='w')
csv_writer = csv.writer(final, dialect='excel')
with open('locations_link.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        url = row[1]
        if len(url) == 31 or len(url) == 32:
            url = unshortener.unshorten(row[1])
        if re.search('@(\-?[0-9]+\.[0-9]+),(\-?[0-9]+\.[0-9]+)', url, re.DOTALL):
            location = re.search('@(\-?[0-9]+\.[0-9]+),(\-?[0-9]+\.[0-9]+)', url, re.DOTALL)
            latitude  = location.groups()[0]
            longitude = location.groups()[1]
            csv_writer.writerow([row[0], latitude, longitude])
            print(f'Location {row[0]}: latitude={latitude} and longitude = {longitude}')
        elif re.search('q=(\-?[0-9]+\.[0-9]+),(\-?[0-9]+\.[0-9]+)', url, re.DOTALL):
            location = re.search('q=(\-?[0-9]+\.[0-9]+),(\-?[0-9]+\.[0-9]+)', url, re.DOTALL)
            latitude  = location.groups()[0]
            longitude = location.groups()[1]
            csv_writer.writerow([row[0], latitude, longitude])
            print(f'Location {row[0]}: latitude={latitude} and longitude = {longitude}')
final.close()

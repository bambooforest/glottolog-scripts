import csv
from pyglottolog.api import Glottolog

api = Glottolog('/Users/stiv/Github/glottolog/')
gc2iso = {l.id: l.iso for l in api.languoids() if l.iso}

with open('gc2iso.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in gc2iso.items():
       writer.writerow([key, value])

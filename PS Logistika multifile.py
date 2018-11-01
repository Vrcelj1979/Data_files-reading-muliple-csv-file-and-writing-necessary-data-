import glob
import pandas as pd
import csv

df = pd.concat([pd.read_csv(f) for f in glob.glob('Vozilo*.csv')], ignore_index = True)


diler1 = df.loc[df.NASLOV == 'AUTONIPPON: Rijeka: Ty', 'NASLOV'] + ', ' + df.loc[df.NASLOV == 'AUTONIPPON: Rijeka: Ty','TIME_RECEIVED_MIN'],
diler2 = df.loc[df.NASLOV == 'ROMIH: Zg: GM', 'NASLOV'] + ', ' + df.loc[df.NASLOV == 'ROMIH: Zg: GM','TIME_RECEIVED_MIN']


dt = (diler1, diler2)

with open('Delivery_time.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(dt)


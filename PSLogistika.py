import pandas as pd
import csv

vozilo = pd.read_csv('Vozilo1.csv')

diler1 = vozilo.loc[vozilo.NASLOV == 'AUTONIPPON: Rijeka: Ty', 'NASLOV'] + ', ' + vozilo.loc[vozilo.NASLOV == 'AUTONIPPON: Rijeka: Ty','TIME_RECEIVED_MIN'],
diler2 = vozilo.loc[vozilo.NASLOV == 'ROMIH: Zg: GM', 'NASLOV'] + ', ' + vozilo.loc[vozilo.NASLOV == 'ROMIH: Zg: GM','TIME_RECEIVED_MIN']
diler3 = vozilo.loc[vozilo.NASLOV == 'Motiro RB vulkanizacija, Ivanja Reka','NASLOV'] + ', ' + vozilo.loc[vozilo.NASLOV == 'Motiro RB vulkanizacija, Ivanja Reka','TIME_RECEIVED_MIN']
diler4 = vozilo.loc[vozilo.NASLOV == 'AUTO KUA `TARKELJ: Zg: RN', 'NASLOV'] + ', ' + vozilo.loc[vozilo.NASLOV == 'AUTO KUA `TARKELJ: Zg: RN','TIME_RECEIVED_MIN']
diler5 = vozilo.loc[vozilo.NASLOV == 'AUTO Krk: Krk: RN', 'NASLOV'] + ', ' + vozilo.loc[vozilo.NASLOV == 'AUTO Krk: Krk: RN','TIME_RECEIVED_MIN']
diler6 = vozilo.loc[vozilo.NASLOV == 'AUTO ONDI: Solin: Ty', 'NASLOV'] + ', ' + vozilo.loc[vozilo.NASLOV == 'AUTO ONDI: Solin: Ty','TIME_RECEIVED_MIN']


df = (diler1, diler2, diler3, diler4, diler5, diler6)

print(df)

with open('Delivery_time.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(df)
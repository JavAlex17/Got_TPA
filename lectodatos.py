import pandas as pd
datos=list(pd.read_csv('character_deaths.csv',header=0))
print(datos[0:13])
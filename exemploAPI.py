import requests
import pandas as pd


# 1. Configuration
api_key = "TU_API_KEY"  # pon aquí tu clave real
base_url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/"


# 2. First request
response = requests.get(base_url, params={"api_key": api_key})
data_info = response.json()


if "datos" not in data_info:
    raise Exception("Error retrieving the data URL. Check your API key and request.")


data_url = data_info["datos"]


# 3. Request to download the real data
stations_response = requests.get(data_url)
records = stations_response.json()


# 5. Create data frame
df = pd.DataFrame(records)
print("\n---- DATAFRAME HEAD ----\n")
print(df.head())


# 6. Descriptive analysis
## Stations per province
stations_per_province = df["provincia"].value_counts()
print("\n---- STATIONS PER PROVINCE ----\n")
print(stations_per_province)
## Highest-altitude station
df["altitud"] = pd.to_numeric(df["altitud"], errors="coerce")
highest_station = df.loc[df["altitud"].idxmax()]
print("\n---- HIGHEST ALTITUDE STATION ----\n")
print(highest_station)


# 7. Export to csv
df.to_csv("aemet_weather_stations.csv", index=False)
print("\nCSV file saved as: aemet_weather_stations.csv\n")


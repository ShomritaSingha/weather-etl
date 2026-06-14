from extract.weather_api import get_weather_data
from transform.weather_transform import  transformed_weather_data
from load.weather_loader import load_etl

raw_data = get_weather_data()


transformed_data = transformed_weather_data(raw_data)

# print(trans)

load_data = load_etl(transformed_data)
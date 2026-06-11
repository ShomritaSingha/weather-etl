from extract.weather_api import get_weather_data
from transform.weather_transform import  transformed_weather_data

raw_data = get_weather_data()


trans = transformed_weather_data(raw_data)

print(trans)

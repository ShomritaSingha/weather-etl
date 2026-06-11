import requests

def get_weather_data():
    
    response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=22.57&longitude=88.36&current=temperature_2m,is_day,wind_speed_10m&timezone=America%2FNew_York")
    print(response.status_code)
    

    data = response.json()
  
    return data
   
    
get_weather_data()


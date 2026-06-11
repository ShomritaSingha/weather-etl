


def transformed_weather_data(raw_data):
    transformed_data = {
    "latitude": raw_data["latitude"],
    "longitude": raw_data["longitude"],
    "temperature": raw_data["current"]["temperature_2m"],
    "temperature_unit": raw_data["current_units"]["temperature_2m"],
    "time": raw_data["current"]["time"],
    "wind_speed": raw_data["current"]["wind_speed_10m"],
    "wind_speed_unit": raw_data["current_units"]["wind_speed_10m"]
}
        
       
    
    
     
    
    return transformed_data


        
                
                

        
    
        
        

    



def tranformed_weather_data(raw_data):
    transfomred_data =  {
        "location": (f"{raw_data['latitude']}, {raw_data['longitude']}"),
        "temperature" : (f"Temparature: {raw_data['current']['temperature_2m'] } {raw_data['current_units']['temperature_2m']}"),
        "time" : (f" time :{raw_data['current'][ 'time']}"),
        "wind_speed" : (f"wind_speed: {raw_data['current']['wind_speed_10m'] } {raw_data['current_units']['wind_speed_10m']}")
        
       
    }
    print("works")
     
    
    return transfomred_data


        
                
                

        
    
        
        

    
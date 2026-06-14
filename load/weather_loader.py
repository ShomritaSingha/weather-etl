import mysql.connector



def load_etl(transformed_data):
    
    

    config = mysql.connector.connect(
        
        
        host="localhost",
        user="root",
        database = "weather_etl" )
    
    mycursor = config.cursor()
    
    
    
    







    #sanity check to see if the database is connected and working
    # for x in mycursor:
    #     print(x)
    
    insert_query = """
    INSERT INTO weather_daily_load
    (latitude, longitude, temperature, temperature_unit, weather_time, wind_speed, wind_speed_unit)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values  =(transformed_data["latitude"], 
            transformed_data["longitude"], 
            transformed_data["temperature"], 
            transformed_data["temperature_unit"], 
            transformed_data["weather_time"], 
            transformed_data["wind_speed"], 
            transformed_data["wind_speed_unit"]
            )
    
    
    mycursor.execute(insert_query, values)
    config.commit()
    print("Data inserted successfully.")
    
    return transformed_data

    
    

  
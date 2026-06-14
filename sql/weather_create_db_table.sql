CREATE DATABASE IF NOT EXISTS weather_etl;

USE weather_etl;

CREATE TABLE IF NOT EXISTS weather_daily_load (
    id INT AUTO_INCREMENT PRIMARY KEY,
    latitude FLOAT,
    longitude FLOAT,
    temperature FLOAT,
    temperature_unit VARCHAR(10),
    weather_time DATETIME,
    wind_speed FLOAT,
    wind_speed_unit VARCHAR(10),
    update_ts DATETIME DEFAULT CURRENT_TIMESTAMP
);
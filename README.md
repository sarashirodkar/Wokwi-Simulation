# iot_assignment3

This report details developing a cloud-based IoT system using Wokwi for simulation and ThingSpeak for data collection and visualization.

1. Wokwi Simulation

The code connects to the Wi-Fi network identified by WIFI_SSID and WIFI_PASSWORD. This enables ThingSpeak and the internet to be accessed by the emulated device. We can create a Wokwi project with simulated sensors (temperature, humidity) that publish data to ThingSpeak using MQTT.

The generate_sensor_data function produces random values within the specified ranges for temperature, humidity, and CO2.

The publish_to_thingspeak function utilizes the MQTT protocol to publish sensor data to ThingSpeak channels. It connects to the ThingSpeak MQTT broker using the provided credentials and publishes data to separate topics designated for each sensor (temperature, humidity, CO2).

The code maintains a list (historical_data) to store the generated sensor readings. This allows for retrieving data over a specified time window. It also implements logic to limit the stored data to approximately five hours by removing older entries when the list exceeds a certain size.

The code continuously runs within a loop: 
-Generates random sensor data.
-Publishes data to ThingSpeak. 
-Stores data in the historical data list. 
-Waits for a specified interval before repeating (adjusted to 5 seconds for faster simulation).

The get_last_five_hours_data function retrieves sensor data from the historical list for a specific sensor type (temperature, humidity, CO2) within the last five hours.

2. ThingSpeak Data Retrieval (MATLAB Code)

The code defines the ThingSpeak channel ID (channelID) and read API key (readAPIKey).
It retrieves the current time (currentTime) and calculates the time five hours ago (fiveHoursAgo).
The code builds a URL to access ThingSpeak's API for fetching sensor data within the specified time window (start and end parameters).
It uses webread to fetch data from the constructed URL.
The code checks for retrieved data (data.feeds). If data exists, it extracts sensor readings (sensorData) and timestamps (timestamps) from the specific field (assuming field 1) and displays them. Otherwise, it indicates no data found for the time range.

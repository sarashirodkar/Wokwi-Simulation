import network
import time
import urandom
from umqtt.simple import MQTTClient

mqtt_client_id = "EyQxJB80PTgJPRUyNScuHSk"
mqtt_user = "EyQxJB80PTgJPRUyNScuHSk"
mqtt_password = "iOEBRwLTim1+XT802mkQ0VGB"
mqtt_server = "mqtt3.thingspeak.com"
mqtt_port = 1883
mqtt_topic_temperature = "channels/2488606/publish/fields/field1"
mqtt_topic_humidity = "channels/2488606/publish/fields/field2"
mqtt_topic_co2 = "channels/2488606/publish/fields/field3"

WIFI_SSID = "Wokwi-GUEST"
WIFI_PASSWORD = ""

historical_data = []

# random sensor values
def generate_sensor_data():
    temperature = urandom.uniform(-50, 50)
    humidity = urandom.uniform(0, 100)
    co2 = urandom.uniform(300, 2000)
    return temperature, humidity, co2

def publish_to_thingspeak(temperature, humidity, co2):
    client = MQTTClient(mqtt_client_id, mqtt_server, user=mqtt_user, password=mqtt_password)
    client.connect()
    client.publish(mqtt_topic_temperature, str(temperature))
    client.publish(mqtt_topic_humidity, str(humidity))
    client.publish(mqtt_topic_co2, str(co2))
    client.disconnect()

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(WIFI_SSID, WIFI_PASSWORD)

while not sta_if.isconnected():
    pass

print("Connected to Wi-Fi")

while True:
    temperature, humidity, co2 = generate_sensor_data()
    publish_to_thingspeak(temperature, humidity, co2)
    print("Published: Temperature={:.2f}C, Humidity={:.2f}%, CO2={:.2f}ppm".format(temperature, humidity, co2))
    historical_data.append((temperature, humidity, co2)) 
    if len(historical_data) > 720: 
        historical_data.pop(0)  
    time.sleep(5)  

def get_last_five_hours_data(sensor_type):
    sensor_index = {'temperature': 0, 'humidity': 1, 'co2': 2}[sensor_type]
    last_five_hours_data = [(data[sensor_index],) for data in historical_data[-720:]]
    return last_five_hours_data

last_five_hours_temperature = get_last_five_hours_data('temperature')
print("Last five hours temperature data:", last_five_hours_temperature)
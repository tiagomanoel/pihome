import os
from mqtt_connection.mqtt_client_connection import MqttClientConnection
import time
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path='/home/tiagomanoel/Dev/piHome/dotenv_files/.env')

def start():
    broker_ip = os.getenv('MQTT_HOST')
    port = os.getenv('MQTT_PORT')
    client_name = os.getenv('MQTT_CLIENT_NAME')
    keepalive = os.getenv('MQTT_KEEPALIVE')
    topic = os.getenv('MQTT_TOPIC')

    print(f"MQTT_HOST={broker_ip}, MQTT_PORT={port}, MQTT_CLIENT_NAME={client_name}, MQTT_KEEPALIVE={keepalive}, MQTT_TOPIC={topic}")

    if not all([broker_ip, port, client_name, keepalive, topic]):
        raise ValueError("One or more MQTT environment variables are not set")

    mqtt_client_connection = MqttClientConnection(
        broker_ip=broker_ip,
        port=int(port),
        client_name=client_name,
        keepalive=int(keepalive),
        topic=topic
    )
    mqtt_client_connection.start_connection()

    while True:
        time.sleep(0.001)


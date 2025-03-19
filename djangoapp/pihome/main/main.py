import os
from mqtt_connection.mqtt_client_connection import MqttClientConnection
import time
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql
from datetime import datetime

# Carregar variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path='/home/tiagomanoel/Dev/piHome/dotenv_files/.env')

conn = psycopg2.connect(
    database="data_db",  # Name of the database
    user="user",      # Database user
    host='127.0.0.1',      # Host where the database is located
    password="user123",  # User's password
    port=5432     # Port number for the database connection
)

def on_message(client, userdata, msg):
    print(f"Message received: {msg.topic} {msg.payload}")
    action = msg.payload.decode('utf-8')
    if action not in ["ON", "OFF"]:
        return  # Ignorar mensagens que não sejam "ON" ou "OFF"
    # Verificar se a mensagem já foi salva no banco de dados
    cur = conn.cursor()
    cur.execute(
        sql.SQL("SELECT COUNT(*) FROM pihome_action WHERE date = %s AND time = %s AND action = %s AND topic = %s"),
        (datetime.now().date(), datetime.now().time(), action, msg.topic)
    )
    if cur.fetchone()[0] > 0:
        cur.close()
        return  # Ignorar mensagens duplicadas
    # Salvar a mensagem no banco de dados
    cur.execute(
        sql.SQL("INSERT INTO pihome_action (action, date, time, topic) VALUES (%s, %s, %s, %s)"),
        (action, datetime.now().date(), datetime.now().time(), msg.topic)
    )
    conn.commit()
    cur.close()

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

    mqtt_client_connection.client.on_message = on_message

    while True:
        time.sleep(0.001)


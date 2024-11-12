import psycopg2
from psycopg2 import sql

# Función para obtener una conexión
def get_db_pl_core_connection():
    try:
        # Establecer la conexión
        connection = psycopg2.connect(
            host="localhost",         # Host donde está la base de datos
            database="master",     # Nombre de la base de datos
            user="master",           # Usuario de la base de datos
            password="Ku<=ngAZ*H|QA7-bj)WPz",    # Contraseña del usuario
            port="5432"               # Puerto de la base de datos (opcional)
        )
        return connection
    except Exception as e:
        print(f"Error al conectarse a la base de datos: {e}")
        return None

def get_db_pulpopay_connection():
    try:
        # Establecer la conexión
        connection = psycopg2.connect(
            host="localhost",         # Host donde está la base de datos
            database="pl_bridge_db",     # Nombre de la base de datos
            user="master",           # Usuario de la base de datos
            password="Ku<=ngAZ*H|QA7-bj)WPz",    # Contraseña del usuario
            port="5432"               # Puerto de la base de datos (opcional)
        )
        return connection
    except Exception as e:
        print(f"Error al conectarse a la base de datos: {e}")
        return None

# Función para cerrar la conexión
def close_db_connection(connection):
    if connection:
        connection.close()
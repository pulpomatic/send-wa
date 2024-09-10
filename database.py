import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql
# Función para obtener una conexión
def get_db_pl_core_connection():
    
    try:
        # Establecer la conexión
        connection = psycopg2.connect(
            host= os.getenv('DB_HOST'),        
            database=os.getenv('DB_NAME'),    
            user=os.getenv('DB_USER'),          
            password=os.getenv('DB_PASSWORD'),    
            port=os.getenv('DB_PORT')               
        )
        return connection
    except Exception as e:
        print(f"Error al conectarse a la base de datos: {e}")
        return None

def get_db_pulpopay_connection():
    try:
        # Establecer la conexión
        connection = psycopg2.connect(
            host=os.getenv('PP_DB_HOST'),         
            database=os.getenv('PP_DB_NAME'),    
            user=os.getenv('PP_DB_USER'),          
            password=os.getenv('PP_DB_PASSWORD'),    
            port=os.getenv('PP_DB_PORT')               
        )
        return connection
    except Exception as e:
        print(f"Error al conectarse a la base de datos: {e}")
        return None


def close_db_connection(connection):
    if connection:
        connection.close()
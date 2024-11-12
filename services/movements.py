import logging
from constants import QUERY_MOVEMENTS
from database import get_db_pl_core_connection, close_db_connection


def get_movements_without_checkin(account_ids) -> list:
    """Obtiene movimientos sin check-in para las cuentas especificadas.

    Args:
        account_ids (str): Lista de IDs de cuenta para filtrar los movimientos.

    Returns:
        list: Lista de diccionarios con los movimientos sin check-in.
    """
    connection = None
    try:
        connection = get_db_pl_core_connection()
        
        with connection.cursor() as cursor:
            cursor.execute(QUERY_MOVEMENTS.format(account_ids=account_ids))
            results = cursor.fetchall()
        
            # Definir las llaves de los diccionarios basadas en los nombres de las columnas
            column_names = [desc[0] for desc in cursor.description]
            movements = [dict(zip(column_names, row)) for row in results]  # Convertir filas a diccionarios
        
        return movements  # Devolver la lista de diccionarios
    
    except Exception as e:
        logging.error(f"Failed to retrieve movements: {e}")
        return []
    
    finally:
        if connection:
            close_db_connection(connection)

     
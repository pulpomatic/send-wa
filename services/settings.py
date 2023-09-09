import logging
from database import close_db_connection, get_db_pl_core_connection

def get_settings_by_key(key: str):
    connection = None
    try:
        connection = get_db_pl_core_connection()
        
        with connection.cursor() as cursor:
           
            cursor.execute("""
                SELECT as2."name", as2.value, as2.account_id 
                FROM accounts_settings as2 
                WHERE as2."name" = %s
            """, (key,))
            results = cursor.fetchall()

           
            column_names = [desc[0] for desc in cursor.description]
            settings = [dict(zip(column_names, row)) for row in results] 
        
        return settings  
    
    except Exception as e:
        logging.error(f"Failed to retrieve settings for key '{key}': {e}")
        return []
    
    finally:
        if connection:
            close_db_connection(connection)

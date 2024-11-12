from database import get_db_pl_core_connection, close_db_connection

def get_user_by_id(user_id):
    """Obtiene un usuario a partir de su ID.

    Args:
        user_id (int): El ID del usuario a buscar.

    Returns:
        dict: Diccionario con la información del usuario o None si no se encuentra.
    """
    connection = get_db_pl_core_connection()
    
    try:
        with connection.cursor() as cursor:
            # Definir la consulta SQL usando un parámetro para evitar inyecciones SQL
            sql = "SELECT id, full_name, phone_number FROM users WHERE id = %s"
            cursor.execute(sql, (user_id,))
            row = cursor.fetchone()  # Solo se espera un registro
            
            if row is None:
                return None  # Retorna None si no se encuentra el usuario
            
            # Procesar el resultado y devolver el usuario como un diccionario
            user = {
                "id": row[0],
                "name": row[1],
                "phone": row[2]
            }
            return user  # Devuelve el diccionario del usuario

    except Exception as e:
        print(f"Error al obtener el usuario: {e}")
        return None  # Devuelve None en caso de error

    finally:
        close_db_connection(connection)  # Cierra la conexión a la base de datos

    
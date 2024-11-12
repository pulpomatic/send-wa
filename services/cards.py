from database import get_db_pl_core_connection


def get_cards_ids_checkin_required_by_accounts(account_ids):
    connection = get_db_pl_core_connection()
    try:
        with connection.cursor() as cursor:
            query = f"""
                SELECT id
                FROM payment_methods
                WHERE account_id IN ({account_ids})
                AND checkin_required = true;
            """.format(account_ids=account_ids)
            cursor.execute(query)

            # Obtiene todos los resultados
            results = cursor.fetchall()
            # Extrae los IDs de los resultados en una lista
            ids = [str(row[0]) for row in results] if results else []
    except Exception:
        return None
    finally:
        if connection:
            connection.close()

    return ', '.join(ids) if ids else None

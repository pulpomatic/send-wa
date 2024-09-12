# constants.py
MESSAGES_REMAIDER_CHECKING = """
Hola {user_name},
Se registró un movimiento de ${movement_total} en tu tarjeta terminada en 1234.
Hora: {movement_date}
Hora límite: 15:00
Gracias,
PulpoPay :octopus:
"""

QUERY_MOVEMENTS = """
SELECT 
    u.phone_number,
    u.full_name,
    e.total AS movement_total, 
    pm.slug, 
    e."date" AT TIME ZONE 'America/Mexico_City' AS movement_date 
FROM 
    expenses e
INNER JOIN 
    fuels f ON f.expense_id = e.id
INNER JOIN 
    payment_methods pm ON pm.id = f.payment_method_id
INNER JOIN 
    users u ON u.id = f.driver_id
WHERE 
    pm.checkin_required = true 
    AND f.account_id IN ({account_ids}) 
    AND e.has_check_in = false
    AND e."date" AT TIME ZONE 'America/Mexico_City' >= (NOW() AT TIME ZONE 'America/Mexico_City') - INTERVAL '30 hours';
"""

CONTENT_SID_REMINDER_CHECKING = "HX11caf525382cc6d7aecb74c10e5dc6d7"

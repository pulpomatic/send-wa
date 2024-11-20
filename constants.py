# constants.py

QUERY_MOVEMENTS = """
SELECT 
    u.phone_number,
    u.full_name,
    ROUND(e.total, 2) AS movement_total, 
    RIGHT(pm.slug, 4) AS slug, 
    TO_CHAR(e."date" AT TIME ZONE 'America/Mexico_City', 'HH24:MI') AS movement_date
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
    AND e."date" AT TIME ZONE 'America/Mexico_City' >= (NOW() AT TIME ZONE 'America/Mexico_City') - INTERVAL '500 hours';
"""

CONTENT_SID_REMINDER_CHECKING = "HX0783b7112253b482efff9445a1f9ace1"

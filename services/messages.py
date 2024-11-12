from services.cards import get_cards_ids_checkin_required_by_accounts
from services.movements import get_movements_without_checkin
from services.wa import send_message
from constants import CONTENT_SID_REMINDER_CHECKING
from services.users import get_user_by_id
from services.settings import get_settings_by_key
import json
from decimal import Decimal


def send_reminder_checkins() -> None:
    """Envía recordatorios de check-in a los usuarios con movimientos sin check-in."""

    print("Iniciando el proceso de envío de recordatorios de check-in...")
    
    # Obtener la lista de configuraciones para el envío de recordatorios de check-in
    list_settings = get_settings_by_key('send_reminder_checkins')
    
    if not list_settings:
        print("No hay configuraciones disponibles para enviar recordatorios. Finalizando el proceso.")
        return

    print("Configuraciones obtenidas con éxito. Extraer accountIds...")

    # Extraer los accountIds de las configuraciones
    account_ids = [item['account_id'] for item in list_settings]
    if not account_ids:
        print("No se encontraron accountIds en las configuraciones. Finalizando el proceso.")
        return

    account_ids_string = ', '.join(f"'{account_id}'" for account_id in account_ids)
    print('account_ids:', account_ids_string)

    # Obtener los movimientos que no tienen check-in asociado
    print("Obteniendo movimientos sin check-in...")
    movements_without_checkin = get_movements_without_checkin(account_ids_string)

    if not movements_without_checkin:
        print("No se encontraron movimientos sin check-in disponibles.")
        return

    print(f"Se encontraron {len(movements_without_checkin)} movimientos sin check-in.")

    # Enlace para el formulario de check-in
    enlace_formulario = "https://appeu.getpulpo.com/tools"

    # Iterar sobre cada movimiento que no tiene check-in
    for movement in movements_without_checkin:
        process_movement(movement, enlace_formulario)


def process_movement(movement: dict, enlace_formulario: str) -> None:
    """Procesa el movimiento y envía un recordatorio de check-in al usuario correspondiente."""
    
    try:
        # Obtener datos relevantes del movimiento
        movement_total = Decimal(movement.get('movement_total', 0))
        movement_date = movement.get('movement_date', 'Fecha no disponible')
        user_name = movement.get('full_name', 'Usuario desconocido')
        user_phone = movement.get('phone_number', None)

        if not user_phone:
            print(f"Datos incompletos para el usuario: {user_name}. Se registrará y continuará con el siguiente movimiento.")
            return

        user_phone_msn = f'whatsapp:+521{user_phone}'
        print(f"Preparando el mensaje para el usuario {user_name} y teléfono {user_phone_msn}...")

        # Enviar el mensaje al usuario
        content_variables = {
            "1": user_name,
            "2": str(movement_total),
            "3": str(movement_date),
            "4": enlace_formulario
        }
        content_variables_string=json.dumps(content_variables)
        print(content_variables_string)
        send_message(content_sid=CONTENT_SID_REMINDER_CHECKING, to=user_phone_msn, content_variables=content_variables_string)
        print(f"Mensaje enviado a {user_phone_msn} con éxito.")

    except Exception as e:
        print(f"Error al enviar mensaje a {user_phone_msn}: {e}. Se registrará y continuará con el siguiente movimiento.")


from services.messages import send_reminder_checkins

def lambda_handler(event, context):
    print('Enviando mensajes de recordatorios de checkins...')
    send_reminder_checkins()
    print('Han finalizado')
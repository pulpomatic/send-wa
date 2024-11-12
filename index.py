from services.messages import send_reminder_checkins

if "__main__" == __name__:
    print('Enviando mensajes de recordatorios de checkins...')
    send_reminder_checkins()
    print('Han finalizado')

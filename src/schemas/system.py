

hour_regex = r'^[0-9][0-9]:[0-5][0-9]$'

def validation_hour(v):
    """Valida el formato de la hora en HH:MM"""
    hora, minuto = map(int, v.split(':'))
    if hora < 0 or hora > 99:
        raise ValueError('La hora debe estar entre 0 y 99')
    if minuto < 0 or minuto > 59:
        raise ValueError('El minuto debe estar entre 0 y 59')
    return v
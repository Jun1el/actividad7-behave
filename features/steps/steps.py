from behave import given, when, then
import re
import random
import logging

NUMEROS_ES = {
    "cero": 0, "uno": 1, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
    "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
    "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
    "diecisiete": 17, "dieciocho": 18, "diecinueve": 19, "veinte": 20,'treinta': 30,
    "media": 0.5
}
NUMEROS_EN = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20, "half": 0.5
}
# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    if not palabra:
        return 0
    palabra = palabra.lower()
    if palabra in NUMEROS_ES:
        return NUMEROS_ES[palabra]
    if palabra in NUMEROS_EN:
        return NUMEROS_EN[palabra]
    try:
        return float(palabra)
    except ValueError:
        return 0

@given('que he comido {cukes:g} pepinos')
def step_given_eaten_cukes(context, cukes):
    try:
        context.belly.comer(float(cukes))
        context.exception = None
    except Exception as e:
        context.exception = e

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace('y', ' ')
    time_description = time_description.replace(',', ' ')
    time_description = time_description.strip()

    if time_description == 'media hora'or time_description == 'half an hour':
        total_time_in_hours = 0.5
        context.belly.esperar(total_time_in_hours)
        return
    # Caso: aleatorio entre X e Y horas
    match_random = re.search(r'entre +(\d+(?:\.\d+)?)+ y +(\d+(?:\.\d+)?)+horas', time_description) 
    if match_random:
        min_h = float(match_random.group(1))
        max_h = float(match_random.group(2))
        random.seed(42)  # Semilla fija para reproducibilidad
        total_time_in_hours = round(random.uniform(min_h, max_h), 2)
        logging.info(f"Tiempo aleatorio generado: {total_time_in_hours} horas")
        context.belly.esperar(total_time_in_hours)
        return

    
    
    # Actualizamos la expresion regular para incluir segundos
    pattern = re.compile(
        r'(?:(\w+)\s*(?:hora|horas|hour|hours))?\s*(?:(\w+)\s*(?:minuto|minutos|minute|minutes))?\s*(?:(\w+)\s*(?:segundo|segundos|second|seconds))?'
    )
    match = pattern.match(time_description)

    if match:
        hours_word = match.group(1) or "0"
        minutes_word = match.group(2) or "0"
        seconds_word = match.group(3) or "0"

        hours = convertir_palabra_a_numero(hours_word)
        minutes = convertir_palabra_a_numero(minutes_word)
        seconds = convertir_palabra_a_numero(seconds_word)

        total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
        context.belly.esperar(total_time_in_hours)
    else:
        raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")
    

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then("debería lanzarse un error por negativa")
def step_then_error_expected(context):
    assert context.exception is not None # "Se esperaba una excepción, pero no se lanzó ninguna."
    assert isinstance(context.exception, ValueError)
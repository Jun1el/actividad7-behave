import pytest
from features.steps.steps import convertir_palabra_a_numero

# Pruebas de la función convertir_palabra_a_numero
def test_convertir_palabra_a_numero():
    assert convertir_palabra_a_numero('uno') == 1
    assert convertir_palabra_a_numero('dos') == 2
    assert convertir_palabra_a_numero('tres') == 3
    assert convertir_palabra_a_numero('media') == 0.5
    assert convertir_palabra_a_numero('diez') == 10
    assert convertir_palabra_a_numero('quince') == 15
    assert convertir_palabra_a_numero('veinte') == 20
    assert convertir_palabra_a_numero('treinta') == 30

    # Prueba con palabras no definidas (debería devolver 0)
    assert convertir_palabra_a_numero('no_existe') == 0
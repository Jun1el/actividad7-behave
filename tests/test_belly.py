import pytest
from src.belly import Belly

def test_comer_pepinos_fraccionarios():
    belly = Belly()
    belly.comer(2.75)  # Pepinos fraccionarios
    assert belly.pepinos_comidos == 2.75

def test_comer_pepinos_negativos():
    belly = Belly()
    with pytest.raises(ValueError):
        belly.comer(-5)  # Intentamos comer una cantidad negativa de pepinos
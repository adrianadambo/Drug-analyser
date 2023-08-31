import project
import pytest
from project import get_index, get_target, add_for, get_function

def test_get_index():
    assert get_index("new_match.csv", "Hydroxyprogesterone") == "D00AEQ"
    assert get_index("new_match.csv", "Ethanol") == "D00AMQ"
    assert get_index("new_match.csv", "Docosanol") == "D00AOJ"


def test_get_target():
    assert get_target("finaltarget.csv", "D09HNV") == "T47101"
    assert get_target("finaltarget.csv", "D0O6UY") == "T47101"
    assert get_target("finaltarget.csv", "D01PZD") == "T47101"

def test_add_for():
    assert add_for("Approved new medication") == "A"
    assert add_for("Approved colon cancer") == "A"




import pytest
from hat import Hat
from wizard import Wizard, Student, Professor
from vault import Vault


def test_hat_picks_a_real_house():
    for _ in range(20):                   # random, so try it many times
        result = Hat.sort("Harry")
        house = result.replace("Harry is in ", "")
        assert house in Hat.houses


def test_inheritance_shares_name_check():
    with pytest.raises(ValueError):
        Student("", "Gryffindor")
    with pytest.raises(ValueError):
        Professor("", "Potions")


def test_children_have_parent_attribute():
    s = Student("Harry", "Gryffindor")
    p = Professor("Severus", "Potions")
    assert s.name == "Harry"
    assert p.name == "Severus"
    assert str(p) == "Severus, professor of Potions"


def test_vault_add():
    total = Vault(100, 50, 25) + Vault(25, 50, 100)
    assert total.galleons == 125
    assert total.sickles == 100
    assert total.knuts == 125
    assert str(total) == "125 Galleons, 100 Sickles, 125 Knuts"

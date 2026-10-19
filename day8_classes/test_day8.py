
import pytest
from student_tuple_dict import get_student_tuple, get_student_dict
from student_class import Student


def test_tuple():
    name, house = get_student_tuple()
    assert name == "Harry"
    assert house == "Gryffindor"


def test_tuple_cannot_change():
    student = get_student_tuple()
    with pytest.raises(TypeError):
        student[0] = "Draco"


def test_dict():
    assert get_student_dict()["house"] == "Gryffindor"


def test_student_object():
    s = Student("Hermione", "Gryffindor")
    assert s.name == "Hermione"
    assert s.house == "Gryffindor"
    assert s.greeting() == "Hermione from Gryffindor"


def test_objects_are_separate():
    a = Student("Harry", "Gryffindor")
    b = Student("Draco", "Slytherin")
    a.house = "Hufflepuff"
    assert b.house == "Slytherin"     # changing a did not change b

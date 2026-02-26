from quiz.validators import validate_name, validate_choice


def test_name_valid():
    assert validate_name("Josh")[0] is True


def test_name_invalid():
    assert validate_name("")[0] is False


def test_choice_valid():
    assert validate_choice(1, 4)[0] is True


def test_choice_invalid():
    assert validate_choice(5, 4)[0] is False
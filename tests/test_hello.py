from hello import greet


def test_greet_with_explicit_name():
    assert greet("Daniel") == "Hello, Daniel!"


def test_greet_with_default_name_world():
    assert greet() == "Hello, World!"

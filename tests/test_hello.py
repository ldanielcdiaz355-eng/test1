import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hello import greet


def test_greet_with_explicit_name():
    assert greet("Daniel") == "Hello, Daniel!"


def test_greet_with_default_name_world():
    assert greet() == "Hello, World!"

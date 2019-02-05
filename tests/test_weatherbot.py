# -*- coding: utf-8 -*-

"""Testing weatherbot."""
from weather_bot.hello import main


def test_main():
    """Test main function."""
    assert main() == 'hello world!'

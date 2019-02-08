# -*- coding: utf-8 -*-

"""Testing weatherapi."""
import pytest

from weather_bot.weather import Location, WeatherError


@pytest.fixture(scope='session')
def weather_fixture_valid():
    """Create a Location class from coordinates."""
    latitude, longitude = (71.0273823, 9.1312633)
    yield Location(latitude, longitude)


@pytest.fixture(scope='session')
def weather_fixture_invalid():
    """Create a Location class from coordinates."""
    latitude, longitude = ('111asdf111', -111123.6310473)
    yield Location(latitude, longitude)


def test_forecast_success(weather_fixture_valid):
    """Test forecast."""
    try:
        weather_fixture_valid.forecast()
    except WeatherError:
        pytest.fail('Unexpected Error!')


def test_forecast_fail(weather_fixture_invalid):
    """Test forecast."""
    with pytest.raises(WeatherError):
        weather_fixture_invalid.forecast()


def test_class_creation_from_description_valid():
    """Create test class from valid description."""
    description = 'Brussels 1000 Belgium'
    try:
        Location.from_description(description)
    except Exception:
        pytest.fail('Unexpected Error!')


def test_class_creation_from_description_invalid():
    """Create test class from invalid description."""
    description = 'QWERTYUIOP ASDFGHJKL'
    with pytest.raises(WeatherError):
        Location.from_description(description)

# -*- coding: utf-8 -*-

"""Testing weatherapi."""
import pytest

from weather_bot.weather import Weather, WeatherError


@pytest.fixture(scope='session')
def weather_fixture_valid():
    """Create a Weather class from coordinates."""
    latitude, longitude = (71.0273823, 9.1312633)
    yield Weather(latitude, longitude)


@pytest.fixture(scope='session')
def weather_fixture_invalid():
    """Create a Weather class from coordinates."""
    latitude, longitude = ('111asdf111', -111123.6310473)
    yield Weather(latitude, longitude)


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


def test_class_creation_from_location_valid():
    """Create test class from valid location."""
    location = 'Brussels 1000 Belgium'
    try:
        Weather.from_location(location)
    except Exception:
        pytest.fail('Unexpected Error!')


def test_class_creation_from_location_invalid():
    """Create test class from invalid location."""
    location = 'QWERTYUIOP ASDFGHJKL'
    with pytest.raises(WeatherError):
        Weather.from_location(location)

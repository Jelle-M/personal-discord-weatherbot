# -*- coding: utf-8 -*-

"""Weather with Dark Sky API.

Dark Sky API requires an API key, latitude and longitude.

Latitude and longitude can be entered or using the geopy we can translate a
location string to their latitude and longitude coordinates
"""
import logging as log
from typing import NamedTuple

from darksky import forecast
from geopy.exc import GeocoderServiceError
from geopy.geocoders import Nominatim
from requests.exceptions import HTTPError

from config import token

TOKEN = token.DARK_SKY_TOKEN


class WeatherError(Exception):
    """Raises when something went wrong during creation or forecast."""


class Weather(NamedTuple):
    """Hold location and can return weather forecast."""

    latitude: float
    longitude: float

    @classmethod
    def from_location(cls, location: str):
        """Find latitude and longitude based on location string.

        Raises:
            WeatherError

        """
        geolocator = Nominatim(user_agent='personal-weather-bot')
        try:
            geo_location = geolocator.geocode(location)
        except GeocoderServiceError:  # pragma: no cover
            log.warning('Could not connect!')
            raise WeatherError
        try:
            return cls(geo_location.latitude, geo_location.longitude)
        except AttributeError:
            log.warning('Location not found!')
            raise WeatherError

    def forecast(self):
        """Return forecast.

        Contacts Dark Sky API

        Raises:
            WeatherError

        """
        try:
            weather_location = forecast(
                TOKEN,
                self.latitude,
                self.longitude,
                units='si',
            )
            log.debug(
                'Dark Sky responded in ',
                weather_location.response_headers['X-response-Time'],
                )
        except HTTPError:
            log.warning('Dark Sky API returned invalid reponse!')
            raise WeatherError
        return weather_location

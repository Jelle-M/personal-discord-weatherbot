# -*- coding: utf-8 -*-

"""Parse Forecast object."""
from darksky.forecast import Forecast


def is_tomorrow_freeze(forecast: Forecast):
    """Check if tomorrows low temperature is lower than 1."""
    daily_forecast = forecast.daily.data[1]
    return float(daily_forecast.temperatureLow) < 1

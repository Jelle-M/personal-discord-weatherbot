# -*- coding: utf-8 -*-

"""Format a Forecast object to string."""
from darksky.forecast import Forecast


def format_daily_forecast(forecast: Forecast):
    """Format Forecast object to display in message."""
    temperature = '{0} \u00B0C'
    formatted = ''
    # TODO: format with Discord.Emoji()
    # Weather currently
    formatted += 'Weather currently\n'
    formatted += forecast.currently.summary + ' '
    formatted += temperature.format(forecast.currently.temperature)
    formatted += '\n\n'
    # Weather tomorrow
    summary = 'Tomorrow: {0}'
    daily_forecast = forecast.daily.data[1]
    formatted += summary.format(daily_forecast.summary) + ' '
    formatted += temperature.format(daily_forecast.temperatureLow) + ' '
    formatted += temperature.format(daily_forecast.temperatureHigh) + '\n'
    return formatted


def format_darksky_forecast(forecast: Forecast):
    """Format Forecast object to display in message."""
    temperature = '{0} \u00B0C'
    formatted = ''
    # TODO: format with Discord.Emoji()
    # Weather currently
    formatted += 'Weather currently\n'
    formatted += forecast.currently.summary + ' '
    formatted += temperature.format(forecast.currently.temperature)
    formatted += '\n\n'
    # Weather next hour
    formatted += 'Weather for the next hour\n'
    formatted += forecast.hourly.data[1].summary + ' '
    formatted += temperature.format(forecast.hourly.data[1].temperature)
    formatted += '\n\n'
    # Summary Weather for next 7 days
    formatted += 'Weather for next 7 days\n'
    formatted += forecast.daily.summary
    formatted += '\n\n'
    # Weather today, tomorrow and day after
    summaries = ('Today: {0}', 'Tomorrow: {0}', 'Day-after-tomorrow: {0}')
    for daily_forecast, summary in zip(forecast.daily.data[:3], summaries):
        formatted += summary.format(daily_forecast.summary) + ' '
        formatted += temperature.format(daily_forecast.temperatureLow) + ' '
        formatted += temperature.format(daily_forecast.temperatureHigh) + '\n'
    return formatted

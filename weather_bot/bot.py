# -*- coding: utf-8 -*-

"""Discord bot."""
import logging as log

from darksky.forecast import Forecast
from discord.ext.commands import Bot

from config import token
from weather import Location

bot = Bot(
    command_prefix='w!',
    command_not_found='No command named {0} found.',
    description='Current Conditions & Forecast',
    pm_help=True,
)


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


@bot.command(pass_context=True)
async def forecast(ctx, *args):
    """Reply sender with forecast."""
    channel = ctx.message.channel
    description = ' '.join(str(loc) for loc in args)
    forecast_for_location = Location.from_description(description).forecast()
    forecast_formatted = format_darksky_forecast(forecast_for_location)
    forecast_message = '{0}\nForecast for {1}:\n{2}'.format(
        ctx.message.author.mention,
        description,
        forecast_formatted,
    )
    await bot.send_message(channel, forecast_message)


@bot.event
async def on_ready():
    """Log some info when ready."""
    log.debug('Logged in as')
    log.debug(bot.user.name)
    log.debug(bot.user.id)
    log.debug('------')


if __name__ == '__main__':
    bot.run(token.DISCORD_BOT_TOKEN)

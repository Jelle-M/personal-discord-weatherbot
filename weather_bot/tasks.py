# -*- coding: utf-8 -*-

"""Background tasks."""
from asyncio import sleep

from discord import Message
from discord.ext.commands import Bot, Context

from forecast_logic import is_tomorrow_freeze
from formats import format_daily_forecast
from weather import Location


async def hello_task(
    bot: Bot,
    channel: Message.channel,
) -> None:
    """Send three hello messages with 5 seconds interval."""
    await bot.wait_until_ready()
    counter = 0
    while not bot.is_closed and counter < 3:
        counter += 1
        await bot.send_message(channel, 'Hello! ({0}/3)'.format(counter))
        await sleep(3)


async def freeze_alert_task(
    bot: Bot,
    ctx: Context,
    *args: str,
) -> None:
    """Send message if tomorrow is going to freeze."""
    await bot.wait_until_ready()
    description = ' '.join(str(loc) for loc in args)
    location = Location.from_description(description)
    while not bot.is_closed:
        forecast_for_location = location.forecast()
        if is_tomorrow_freeze(forecast_for_location):
            forecast_formatted = 'Temps tomorrow will be below zero!\n'
            forecast_formatted += format_daily_forecast(forecast_for_location)
            forecast_message = '{0}\nForecast for {1}:\n{2}'.format(
                ctx.message.author.mention,
                description,
                forecast_formatted,
            )
            await bot.send_message(ctx.message.channel, forecast_message)
        await sleep(10)

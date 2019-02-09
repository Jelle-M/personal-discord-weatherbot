# -*- coding: utf-8 -*-

"""Discord bot."""
import logging as log
from asyncio import sleep
from typing import Callable

from darksky.forecast import Forecast
from discord import Message
from discord.ext.commands import Bot, Context

from config import token
from formats import (
    format_daily_forecast,
    format_darksky_forecast,
    format_freeze_forecast,
)
from weather import Location

bot = Bot(
    command_prefix='w!',
    command_not_found='No command named {0} found.',
    description='Current Conditions & Forecast',
    pm_help=True,
)


async def my_background_task(channel: Message.channel):
    """Send message."""
    await bot.wait_until_ready()
    counter = 0
    while not bot.is_closed:
        counter += 1
        await bot.send_message(channel, counter)
        await sleep(10)


async def forecast_controller(
    ctx: Context,
    formatter: Callable[[Forecast], None],
    *args: str,
) -> None:
    """Reply sender with forecast."""
    channel = ctx.message.channel
    description = ' '.join(str(loc) for loc in args)
    forecast_for_location = Location.from_description(description).forecast()
    forecast_formatted = formatter(forecast_for_location)
    forecast_message = '{0}\nForecast for {1}:\n{2}'.format(
        ctx.message.author.mention,
        description,
        forecast_formatted,
    )
    await bot.send_message(channel, forecast_message)


@bot.command(pass_context=True)
async def forecast(ctx, *args):
    """Reply sender with forecast."""
    await forecast_controller(ctx, format_darksky_forecast, *args)


@bot.command(pass_context=True)
async def freeze(ctx, *args):
    """Reply sender with forecast."""
    await forecast_controller(ctx, format_freeze_forecast, *args)


@bot.command(pass_context=True)
async def daily(ctx, *args):
    """Reply sender with forecast for the day."""
    await forecast_controller(ctx, format_daily_forecast, *args)


@bot.command(pass_context=True)
async def hello(ctx, *args):
    """Reply sender with hello."""
    channel = ctx.message.channel
    forecast_message = 'Hello {0}!'.format(ctx.message.author.mention)
    bot.loop.create_task(my_background_task(channel))
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

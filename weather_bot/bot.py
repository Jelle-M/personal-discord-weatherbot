# -*- coding: utf-8 -*-

"""Discord bot."""
import logging as log
from typing import Callable

from darksky.forecast import Forecast
from discord.ext.commands import Bot, Context

from config import token
from formats import format_daily_forecast, format_darksky_forecast
from tasks import freeze_alert_task, hello_task
from weather import Location

bot = Bot(
    command_prefix='w!',
    command_not_found='No command named {0} found.',
    description='Current Conditions & Forecast',
    pm_help=True,
)


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
async def daily(ctx, *args):
    """Reply sender with forecast for the day."""
    await forecast_controller(ctx, format_daily_forecast, *args)


@bot.command(pass_context=True)
async def freeze(ctx, *args):
    """Subscribe to a freeze alert task."""
    channel = ctx.message.channel
    forecast_message = 'Subscribing to freeze alert! {0}'.format(
        ctx.message.author.mention,
    )
    bot.loop.create_task(freeze_alert_task(bot, ctx, *args))
    await bot.send_message(channel, forecast_message)


@bot.command(pass_context=True)
async def hello(ctx, *args):
    """Create hello task."""
    channel = ctx.message.channel
    bot.loop.create_task(hello_task(bot, channel))


@bot.event
async def on_ready():
    """Log some info when ready."""
    log.debug('Logged in as')
    log.debug(bot.user.name)
    log.debug(bot.user.id)
    log.debug('------')


if __name__ == '__main__':
    bot.run(token.DISCORD_BOT_TOKEN)

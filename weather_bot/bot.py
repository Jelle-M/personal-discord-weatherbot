# -*- coding: utf-8 -*-

"""Discord bot."""
import logging as log

import discord

from weather_bot.config import token  # type:ignore

client = discord.Client()
client.run(token.DISCORD_BOT_TOKEN)


@client.event
async def on_message(message):
    """We do not want the bot to reply to itself."""
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    """Log some info when ready."""
    log.debug('Logged in as')
    log.debug(client.user.name)
    log.debug(client.user.id)
    log.debug('------')
# -*- coding: utf-8 -*-

"""Discord bot."""
import argparse
import logging as log
from argparse import Namespace

import discord

from weather_bot.config import token  # type:ignore

TOKEN = token.DISCORD_BOT_TOKEN
client = discord.Client()
client.run(TOKEN)


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


def parse_arguments() -> Namespace:
    """Parse arguments."""
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument(
        '-v', '--verbose', action='store_true', help='Show debug messages',
    )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_arguments()
    if args.verbose:
        log.basicConfig(filename='weather_bot.log', level=log.DEBUG)

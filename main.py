from mirubot import Mirubot
import interactions
from buttons import next_button, previous_button, enter_button, airing_button


mirubot = Mirubot()

## COMMAND WRAPPERS ##
@mirubot.command(
    name="ping",
    description="Responds with Pong!"
)
async def ping(ctx: interactions.CommandContext) -> None:
    """
    Respond with Pong!
    """
    await mirubot.ping(ctx)


@mirubot.command(
    name="echo",
    description="Responds with the message.",
    options = [
        interactions.Option(
            name="message",
            description="The message to echo.",
            type=interactions.OptionType.STRING,
            required=True
        ),
    ]
)
async def echo(ctx: interactions.CommandContext, message: str) -> None:
    """
    Respond with the message.
    """
    await mirubot.echo(ctx, message)


@mirubot.command(
    name="anime",
    description="Search for an anime.",
    options = [
        interactions.Option(
            name="anime",
            description="The anime to search for.",
            type=interactions.OptionType.STRING,
            required=True
        ),
    ]
)
async def anime(ctx: interactions.CommandContext, anime: str) -> None:
    """
    Respond with information on the anime.
    """
    await mirubot.anime(ctx, anime, [previous_button, enter_button, next_button])


## COMPONENT WRAPPERS ##
@mirubot.component("next_result")
async def next_result(ctx: interactions.CommandContext) -> None:
    """
    Display the next result.
    """
    await mirubot.next_result(ctx, [previous_button, enter_button, next_button])


@mirubot.component("previous_result")
async def prev_result(ctx: interactions.CommandContext) -> None:
    """
    Display the previous result.
    """
    buttons = {
        "prev": previous_button,
        "enter": enter_button,
        "next": next_button,
        "airing": airing_button
    }
    await mirubot.prev_result(ctx, buttons)


@mirubot.component("select_result")
async def select_result(ctx: interactions.CommandContext) -> None:
    """
    Select the current result.
    """
    await mirubot.select_result(ctx, [previous_button, airing_button])


@mirubot.component("airing_info")
async def airing_info(ctx: interactions.CommandContext) -> None:
    """
    Display the airing information.
    """
    await mirubot.airing_info(ctx, [previous_button])

mirubot.start()


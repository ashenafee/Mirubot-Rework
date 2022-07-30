from typing import Dict, List
import interactions
import os
from dotenv import load_dotenv
from anime.anime.anilist import AnilistAnime, AnilistAnimeFactory
from search.search.search import AnimeSearch
from bot.bot.screen import Screen


# Load .env file
load_dotenv()


class Mirubot(interactions.Client):
    """
    An object containing properties and methods pertaining
    to Mirubot: an anime-centric Discord bot.
    """

    def __init__(self) -> None:
        """
        Initialize a Mirubot object.
        """
        super().__init__(token=os.getenv("DISCORD_SECRET_BOT_TOKEN"))
        self.animes = None
        self.result_embeds = None

        self._curr_embeds = None
        self._curr_embed_index = None
        self._curr_screen = None
    
    ## BOT COMMANDS ##
    async def ping(self, ctx: interactions.CommandContext) -> None:
        """
        Respond with Pong!
        """
        return await ctx.send("Pong!")
    
    async def echo(self, ctx: interactions.CommandContext, message: str) -> None:
        """
        Respond with the message.
        """
        return await ctx.send(message)
    
    async def anime(self, ctx: interactions.CommandContext, query: str, buttons: List[interactions.Button]) -> None:
        """
        Search for anime.
        """
        # Search for the query
        results = self._search_anime(query)
        
        # Create a list of AnilistAnime objects for the results
        factory = AnilistAnimeFactory()
        self.animes = [factory.create_anilist_anime(result) for result in results]
        
        # Create a list of embeds for the results
        embeds = []
        for anime in self.animes:
            anime.make_embed(0)
            embeds.append(anime.get_embed())
        self.result_embeds = embeds
        self._curr_embeds = embeds
        self._curr_embed_index = 0
        self._curr_screen = Screen.RESULTS
        await ctx.send(embeds=[embeds[self._curr_embed_index]], components=buttons)
    
    def _search_anime(self, query: str) -> dict:
        """
        Search for an anime given by query.
        """
        # Search for the query
        results = AnimeSearch(query).search()
        # Return the results
        return results

    ## COMPONENT COMMANDS ##
    async def next_result(self, ctx: interactions.CommandContext, buttons: List[interactions.Button]) -> None:
        """
        Display the next result.
        """
        # Get the next embed
        self._curr_embed_index += 1
        await ctx.edit(embeds=[self.result_embeds[self._curr_embed_index]], components=buttons)
    
    async def prev_result(self, ctx: interactions.CommandContext, buttons: Dict[str, interactions.Button]) -> None:
        """
        Display the previous result.
        """
        if self._curr_screen == Screen.RESULTS:

            # Make the list of buttons
            valid_buttons = [
                buttons['prev'],
                buttons['enter'],
                buttons['next']
            ]

            self._curr_embed_index -= 1
            await ctx.edit(embeds=[self.result_embeds[self._curr_embed_index]], components=valid_buttons)
        
        elif self._curr_screen == Screen.DETAILS:

            # Make the list of buttons
            valid_buttons = [
                buttons['prev'],
                buttons['enter'],
                buttons['next']
            ]

            await ctx.edit(embeds=[self.result_embeds[self._curr_embed_index]], components=valid_buttons)
            self._curr_screen = Screen.RESULTS
        
        elif self._curr_screen == Screen.AIRING:

            # Make the list of buttons
            valid_buttons = [
                buttons['prev'],
                buttons['airing']
            ]

            await ctx.edit(embeds=[self._curr_embeds], components=valid_buttons)
            self._curr_screen = Screen.DETAILS
     
    async def select_result(self, ctx: interactions.CommandContext, buttons: List[interactions.Button]) -> None:
        """
        Select the current result.
        """
        # Get the current anime
        anime = self.animes[self._curr_embed_index]
        # Get the detailed anime embed
        anime.make_embed(1)
        # Send the anime embed
        self._curr_screen = Screen.DETAILS
        await ctx.edit(embeds=[anime.get_embed()], components=buttons)
        self._curr_embeds = anime.get_embed()
    
    async def airing_info(self, ctx: interactions.CommandContext, buttons: List[interactions.Button]) -> None:
        """
        Get the airing information for the current anime.
        """
        # Get the current anime
        anime = self.animes[self._curr_embed_index]
        # Get the airing information embed
        anime.make_embed(2)
        # Send the anime embed
        self._curr_screen = Screen.AIRING
        await ctx.edit(embeds=[anime.get_embed()], components=buttons)

from email.mime import image
from typing import Dict
from anime.anime.anime import Anime
import requests
import json
from search.search.queries import ANIME_SEARCH
from interactions.api.models import Embed, EmbedImageStruct


class AnilistAnime(Anime):
    """
    An object representing an AniList entry of an anime.
    This object builds on its parent object with AniList-specific
    properties included.
    """
    
    def __init__(self, name: Dict[str, str], airing: bool, format: str,
                 episodes: int, synopsis: str, id: int, site_url: str,
                 cover_image: str) -> None:
        """
        Initialize an AnilistAnime object.
        """
        super().__init__(name, airing, format, episodes, synopsis)
        self.id = id
        self.site_url = site_url
        self.cover_image = cover_image
        self.embed = None
    
    ## GETTERS ##
    def get_id(self) -> int:
        """
        Return the ID of the anime.
        """
        return self.id
    
    def get_site_url(self) -> str:
        """
        Return the URL of the anime on AniList.
        """
        return self.site_url
    
    def get_cover_image(self) -> str:
        """
        Return the URL of the cover image of the anime.
        """
        return self.cover_image
    
    def get_embed(self) -> Embed:
        """
        Return the embed object of this anime object.
        """
        return self.embed

    ## SETTERS ##
    def set_id(self, id: int) -> None:
        """
        Set the ID of the anime.
        """
        self.id = id
    
    def set_site_url(self, site_url: str) -> None:
        """
        Set the URL of the anime on AniList.
        """
        self.site_url = site_url
    
    def set_cover_image(self, cover_image: str) -> None:
        """
        Set the URL of the cover image of the anime.
        """
        self.cover_image = cover_image

    ## METHODS ##
    def make_embed(self, type: int) -> None:
        """
        Create a Discord Embed with information on this anime object.

        Type:
            0: Basic embed
            1: Full embed
            2: Airing information
        """
        if type == 0:
            self.embed = Embed(title=f"{self.name['romaji']}",
                        description=f"Also known as: {self.name['english']}", 
                        url=self.site_url,
                        image=EmbedImageStruct(url=self.cover_image))
        elif type == 1:
            self.embed = Embed(title=f"{self.name['romaji']} ({self.name['english']})",
                        url=self.site_url,
                        description=self.synopsis,
                        thumbnail=EmbedImageStruct(url=self.cover_image))
        elif type == 2:
            airing_info = f"**Airing**: {self.airing}\n**Format**: {self.format}\n**Episodes**: {self.episodes}"
            self.embed = Embed(title=f"{self.name['romaji']} ({self.name['english']})",
                        url=self.site_url,
                        description=airing_info,
                        thumbnail=EmbedImageStruct(url=self.cover_image))


class AnilistAnimeFactory:
    """
    An object representing a factory for AnilistAnime objects.
    """
    
    def __init__(self) -> None:
        """
        Initialize an AnilistAnimeFactory object.
        """
        pass
    
    ## METHODS ##
    def create_anilist_anime(self, anime: Dict[str, str]) -> AnilistAnime:
        """
        Create an AnilistAnime object from a dictionary.
        """
        return AnilistAnime(anime['title'], anime['status'], anime['format'],
                            anime['episodes'], anime['description'], anime['id'],
                            anime['siteUrl'], anime['coverImage']['extraLarge'])


if __name__ == '__main__':
    anime = input('Enter an anime: ')
    query = ANIME_SEARCH.replace('$ANIME', anime)
    r = requests.post('https://graphql.anilist.co', json={'query': query})
    response = r.json()

    # Pretty print the response
    print(json.dumps(response, indent=4))
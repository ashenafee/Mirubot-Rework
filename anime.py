from typing import Dict, List


class Anime:
    """
    An object representing an Anime. Basic information on the anime is
    encapsulated within this object and these pieces of information can
    be accessed by the methods provided in this class as well.
    """

    def __init__(self, name: Dict[str, str], airing: bool, format: str,
                episodes: int, synopsis: str) -> None:
        """
        Initialize an Anime object.
        """
        self.name = name
        self.airing = airing
        self.format = format
        self.episodes = episodes
        self.synopsis = synopsis

        self.parse_synopsis()
    
    ## GETTERS ##
    def get_name(self, type: str) -> str:
        """
        Return the name of the anime.
        """
        if type.lower() not in ['romaji', 'english', 'native']:
            raise ValueError('Invalid name type.')
        
        return self.name[type.lower()]
    
    def get_airing(self) -> bool:
        """
        Return whether the anime is currently airing.
        """
        return self.airing
    
    def get_format(self) -> str:
        """
        Return the format of the anime.
        """
        return self.format
    
    def get_episodes(self) -> int:
        """
        Return the number of episodes in the anime.
        """
        return self.episodes
    
    def get_synopsis(self) -> str:
        """
        Return the synopsis of the anime.
        """
        return self.synopsis
    
    ## SETTERS ##
    def set_name(self, type: str, name: str) -> None:
        """
        Set the name of the anime.
        """
        if type.lower() not in ['romaji', 'english', 'native']:
            raise ValueError('Invalid name type.')
        
        self.name[type.lower()] = name
    
    def set_airing(self, airing: bool) -> None:
        """
        Set whether the anime is currently airing.
        """
        self.airing = airing
    
    def set_format(self, format: str) -> None:
        """
        Set the format of the anime.
        """
        self.format = format

    def set_episodes(self, episodes: int) -> None:
        """
        Set the number of episodes in the anime.
        """
        self.episodes = episodes
    
    def set_synopsis(self, synopsis: str) -> None:
        """
        Set the synopsis of the anime.
        """
        self.synopsis = synopsis

    ## METHODS ##
    def parse_synopsis(self) -> None:
        """
        Parse the HTML synopsis of the anime.
        """
        self.synopsis = self.synopsis.replace("<br>", "\n")
        self.synopsis = self.synopsis.replace("<i>", "*")
        self.synopsis = self.synopsis.replace("</i>", "*")


    
    def __str__(self):
        """
        Return a string representation of the anime.
        """
        return f'{self.name["romaji"]} ({self.name["english"]})\n\tEpisodes: {self.episodes}'

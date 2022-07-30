from anime.anime.anilist import AnilistAnime
from search.search.queries import ANIME_SEARCH
import requests


ANILIST_API = "https://graphql.anilist.co"


class AnimeSearch:
    """
    An object representing a search for an anime.
    """

    def __init__(self, anime: str) -> None:
        """
        Initialize an AnimeSearch object.
        """
        self.anime = anime
        self.anilist_anime = None
        self._results = None

    ## GETTERS ##
    def get_anime(self) -> str:
        """
        Return the name of the anime.
        """
        return self.anime

    def get_anilist_anime(self) -> AnilistAnime:
        """
        Return the AnilistAnime object representing the anime.
        """
        return self.anilist_anime

    def get_results(self) -> list:
        """
        Return the search results.
        """
        return self._results

    ## SETTERS ##
    def set_anime(self, anime: str) -> None:
        """
        Set the name of the anime.
        """
        self.anime = anime

    def set_anilist_anime(self, anilist_anime: AnilistAnime) -> None:
        """
        Set the AnilistAnime object representing the anime.
        """
        self.anilist_anime = anilist_anime

    ## METHODS ##
    def search(self) -> list:
        """
        Search for the anime on AniList.
        """
        # Search for the anime on AniList.
        r = requests.post(ANILIST_API, json={'query': ANIME_SEARCH.replace('$ANIME', self.anime)})
        # Get the data from the response.
        self._results = r.json()["data"]["Page"]["media"]
        return self._results
    
    def display_results(self) -> None:
        """
        Display the search results from AniList.
        """
        for i in range(len(self._results)):
            if self._results[i]['title']['english'] is None:
                print(f"[{i + 1}]\t{self._results[i]['title']['romaji']}\n")
            else:
                print(f"[{i + 1}]\t{self._results[i]['title']['romaji']}\
                    \n\t{self._results[i]['title']['english']}\n")

    def select_result(self, choice: int) -> None:
        """
        Select a result from the search results.
        """
        # Create the AnilistAnime object.
        selected = self._results[choice - 1]
        anime = AnilistAnime(selected['title'], selected['status'], selected['format'], 
        selected['episodes'], selected['description'], selected['id'], selected['siteUrl'], 
        selected['coverImage']['extraLarge'])
        
        # Set the AnilistAnime object to the selected result.
        self.set_anilist_anime(anime)
    
    def display_selected_result(self) -> None:
        """
        Display the selected result.
        """
        print(self.anilist_anime)


if __name__ == '__main__':
    naruto_search = AnimeSearch('Naruto')
    naruto_search.search()
    naruto_search.select_result(1)

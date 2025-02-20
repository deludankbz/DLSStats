# TODO: findPlayersByStats(), and findPlayersByClub()
from fuzzywuzzy import fuzz

class PlayerFinder:
    def __init__(self, search_query: str, playerDict: dict) -> None:
        self.search_query = search_query
        self.playerDict = playerDict
        pass

    def __querySorter(self, qPlayerList: list) -> list[dict]:
        "Used to sort whatever dictionary `findPlayerByName()` returns."
        # fuzzInput = lambda x: x['sQueryInfo']['fuzzResult']['fuzzPartRatio'] + x['sQueryInfo']['fuzzResult']['fuzzUQRatio']

        # maybe it isn't qPlayerList
        qSortedPlayerList = sorted(qPlayerList, key=lambda x: x['sQueryInfo']['fuzzResult']['fuzzPartRatio'] + x['sQueryInfo']['fuzzResult']['fuzzUQRatio'], reverse=True)

        print(qSortedPlayerList[0]['sQueryInfo']['name'].title())
        return qSortedPlayerList

    def findPlayersByName(self) -> list[dict] :
        "Returns players found by name"
        fuzzResults = list()
        pPlayerCounter = 1
        for players in self.playerDict:
            fuzzPartRatio = fuzz.partial_ratio(self.search_query, players)
            fuzzUQRatio = fuzz.UWRatio(self.search_query, players)

            if fuzzPartRatio >= 75 and fuzzUQRatio >= 75: 
                # big ol' lis'
                # FIX big ol' lis'
                possiblePlayer = {'sQueryInfo': 
                  {'name': players, 'fuzzResult': 
                  {'fuzzPartRatio': fuzzPartRatio, 'fuzzUQRatio': fuzzUQRatio}},
                  'playerInfo': self.playerDict[players]}

                pPlayerCounter += 1
                fuzzResults.append(possiblePlayer)
        return self.__querySorter(qPlayerList=fuzzResults)

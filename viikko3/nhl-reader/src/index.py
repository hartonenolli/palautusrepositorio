import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = requests.get(url).json()

class PlayerStats:
    def __init__(self, response):
        self.response = response
        #self.players = []

    def top_scorers_by_nationality(self, nationality):
        players = []
        response_values = []
        for values in self.response:
            if values.get('nationality') == nationality:
            #if 'FIN' in values.get(nationality):
                response_values.append(values)

        for player_dict in response_values:
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists'],
                player_dict['nationality']
            )
            players.append(player)


        list = []
        isoin = 0
        isoin_pelaaja = None
        while players != []:
            for player in players:
                arvo = player.molemmat
                if arvo >= isoin:
                    isoin = arvo
                    isoin_pelaaja = player
            list.append(isoin_pelaaja)
            players.remove(isoin_pelaaja)
            isoin = 0
        return list

def filter_players(players):
    list = []
    isoin = 0
    isoin_pelaaja = None
    while players != []:
        for player in players:
            arvo = player.molemmat
            if arvo >= isoin:
                isoin = arvo
                isoin_pelaaja = player
        list.append(isoin_pelaaja)
        players.remove(isoin_pelaaja)
        isoin = 0
    return list

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = PlayerReader(url)
    stats = PlayerStats(response.url)
    filtered_list = stats.top_scorers_by_nationality("FIN")

    for player in filtered_list:
        print(player)

if __name__ == "__main__":
    main()

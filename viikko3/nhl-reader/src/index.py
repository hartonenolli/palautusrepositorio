import requests
from player import Player

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
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []
    response_values = []
    for values in response:
        if values.get('nationality') == 'FIN':
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

    #print("Oliot:")
    filtered_list = filter_players(players)

    for player in filtered_list:
        print(player)

if __name__ == "__main__":
    main()

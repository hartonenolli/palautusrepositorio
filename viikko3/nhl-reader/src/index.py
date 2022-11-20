import requests
from player import Player

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

    for player in players:
        print(player)

if __name__ == "__main__":
    main()

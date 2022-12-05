class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.match_score_1 = 0
        self.match_score_2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.match_score_1 = self.match_score_1 + 1
        else:
            self.match_score_2 = self.match_score_2 + 1

    def get_score(self):
        score_player_1 = self.game_situation(self.match_score_1)
        score_player_2 = self.game_situation(self.match_score_2)

        if self.match_score_1 == self.match_score_2:
            return self.tie_situation(score_player_1)

        return self.game_check(score_player_1, score_player_2)

    def game_situation(self, points):
        situation = ["Love", "Fifteen", "Thirty", "Forty", "Win"]
        if points < 5:
            return situation[points]
        return "Win"
    
    def tie_situation(self, players):
        if players == "Win":
            return "Deuce"
        return f"{players}-All"
    
    def game_check(self, player_1, player_2):
        if abs(self.match_score_1-self.match_score_2) < 2 and (player_1 == "Win" or player_2 == "Win"):
            return self.point_difference()
        elif player_1 == "Win" and self.match_score_1-self.match_score_2 > 1:
            return "Win for player1"
        elif player_2 == "Win" and self.match_score_2-self.match_score_1 > 1:
            return "Win for player2"
        return f"{player_1}-{player_2}"

    def point_difference(self):
        if self.match_score_1 - self.match_score_2 > 1:
            return "Win for player1"
        elif self.match_score_2 - self.match_score_1 > 1:
            return "Win for player2"
        elif self.match_score_1 > self.match_score_2:
            return "Advantage player1"
        return "Advantage player2"
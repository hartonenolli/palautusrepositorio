from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or

class Lana:
    def main():
            url = "https://studies.cs.helsinki.fi//nhlstats/2021-22/players.txt"
            reader = PlayerReader(url)
            stats = Statistics(reader)

            query = QueryBuilder()
            #matcher = query.build()
            #matcher = query.playsIn("NYR").build()
            matcher = query.playsIn("NYR").hasAtLeast(10, "goals").hasFewerThan(20, "goals").build()

            for player in stats.matches(matcher):
                print(player)


class QueryBuilder:
    def __init__(self, pino=Lana()):
        self.pino_olio = pino

    def build(self):
        if self.pino_olio == None:
            filtered_with_all = All()
            return filtered_with_all
        return self.pino_olio

    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team))
    
    def hasAtLeast(self, point, arg):
        return QueryBuilder(HasAtLeast(point, arg))
    
    def hasFewerThan(self, point, arg):
        return QueryBuilder(HasFewerThan(point, arg))

if __name__ == "__main__":
    osuva = Lana
    osuva.main()

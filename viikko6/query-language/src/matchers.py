class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All:
    def __init__(self):
        pass

    def matches(self, argument):
        return True

class Not:
    def __init__(self, olio):
        self.olio = olio

    def matches(self, argument):
        #print(self.olio._attr)
        if argument.goals < self.olio._value:
            return True

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class Or:
    def __init__(self, *oliot):
        self.oliot = oliot

    def matches(self, argument1):
        for olio in self.oliot:
            try:
                if olio._attr == "goals":
                    if argument1.goals >= olio._value:
                        return True
                elif olio._attr == "assists":
                    if argument1.assists >= olio._value:
                        return True
            except Exception:
                break

        for olio in self.oliot:
            if olio._team == argument1.team:
                return True
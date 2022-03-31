# player class

class Player:

    # instantiate max players and 
    max_players = 4
    num_players = 0

    def __init__(self, name):
        self.name = name
        # self.hand = []
        # self.sum = sum
        # self.discard = discard
        Player.add_player()

    # adds player to class, no more than max
    @classmethod
    def add_player(cls):
        if cls.num_players < cls.max_players:
            cls.num_players += 1
            return True
        return False

    @classmethod
    def get_num_players(cls):
        return cls.num_players


p1 = Player('Ari')
p2 = Player('Jim')
p3 = Player('Tom')
p4 = Player('Yams')


print(Player.get_num_players())
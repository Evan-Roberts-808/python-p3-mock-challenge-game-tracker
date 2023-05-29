class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

        game.players(player)
        game.results(self)

        player.results(self)
        player.games_played(game)

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, player):
        from classes.player import Player
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception
        
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        from classes.game import Game
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception
        
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000:
            self._score = score
        else:
            raise Exception
        
    @property
    def players(self):
        return self._players
    
    @players.setter
    def players(self, players):
        from player import Player
        if isinstance(players, Player):
            self._players = players
        else:
            raise Exception
    


class Game:

    all = []

    def __init__(self, title):
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and not hasattr(self, "title") and title:
            self._title = title
        # else:
        #     raise Exception

    # Create a property 'results' that returns a list of results for the game
    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list(set([result.player for result in self.results()]))

    def average_score(self, player):
        scores = [result.score for result in self.results() if result.player == player]
        return sum(scores) / len(scores)


class Player:

    all = []

    def __init__(self, username):
        self.username = username
        type(self).all.append(self)  # Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        # else:
        #     raise Exception

    # Create a property 'results' that returns a list of results for the player
    def results(self):
        return [result for result in Result.all if result.player == self]

    # Create a property 'games_played' that returns a list of games the player has played
    def games_played(self):
        return list(set([result.game for result in self.results()]))

    # Create a method 'played_game' that returns True if the player has played the game
    def played_game(self, game):
        return game in self.games_played()

    # Create a method 'num_times_played' that returns the number of times the player has played the game
    def num_times_played(self, game):
        games_played = [result.game for result in self.results()]
        return games_played.count(game)

    @classmethod
    def highest_scored(cls, game):
        average = [game.average_score(player) for player in cls.all]
        if not average:
            return None
        highest_record_tuple = max(enumerate(average), key=lambda x: x[1])
        return highest_record_tuple[0]


class Result:

    # Create a class variable 'all' that is an empty list
    all = []

    def __init__(self, player, game, score):
        # Initialize the Result object with player, game, and score
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)  # Add the Result object to the 'all' list

    # Create a property 'game' that returns the game object
    @property
    def score(self):
        return self._score

    # Create a property 'score' that sets the score of the result
    @score.setter
    def score(self, score):
        if isinstance(score, int) and not hasattr(self, "score") and 1 <= score <= 5000:
            self._score = score
        # else:
        #     raise Exception

    # Create a property 'player' that returns the player object
    @property
    def player(self):
        return self._player

    # Create a property 'player' that sets the player object
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
        # else:
        #     raise Exception

    # Create a property 'game' that returns the game object
    @property
    def game(self):
        return self._game

    # Create a property 'game' that sets the game object
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game
        # else:
        #     raise Exception

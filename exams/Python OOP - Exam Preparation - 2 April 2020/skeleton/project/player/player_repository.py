from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        player_name = player.username
        names = [p.username for p in self.players]
        if player_name in names:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player_name: str):
        if player_name == "":
            raise ValueError("Player cannot be an empty string!")
        player_to_remove = self.find(player_name)
        self.players.remove(player_to_remove)
        self.count -= 1

    def find(self, username):
        player = [p for p in self.players if p.username == username][0]
        return player

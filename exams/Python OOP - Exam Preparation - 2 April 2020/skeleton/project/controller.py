from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.player.player_repository import PlayerRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, types, username):
        if types == "Beginner":
            player = Beginner(username)
            self.player_repository.add(player)
        elif types == "Advanced":
            player = Advanced(username)
            self.player_repository.add(player)
        return f"Successfully added player of type {types} with username: {username}"

    def add_card(self, types, name):
        if types == "Magic":
            card = MagicCard(name)
            self.card_repository.add(card)
        elif types == "Trap":
            card = TrapCard(name)
            self.card_repository.add(card)
        return f"Successfully added card of type {types}Card with name: {name}"

    def add_player_card(self, username, card_name):
        player = self.player_repository.find(username)
        card = self.card_repository.find(card_name)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name, enemy_name):
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)
        BattleField.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"

    def report(self):
        result = ""
        for player in self.player_repository.players:
            cards = player.card_repository.cards
            result += f"Username: {player.username} - Health: {player.health} - Cards {len(cards)}\n"
            for card in cards:
                result += f"### Card: {card.name} - Damage: {card.damage_points}\n"

        return result
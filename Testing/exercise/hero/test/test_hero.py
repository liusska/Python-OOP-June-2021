from project.hero import Hero

from unittest import TestCase, main


class HeroTests(TestCase):
    def setUp(self):
        self.hero = Hero(username="Hero", level=2, health=100, damage=10)

    def test_init(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_with_same_name_hero_raises(self):
        enemy = Hero("Hero", 2, 100, 10)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_negative_health_raises(self):
        enemy = Hero("Enemy", 10, 10, 10)
        self.hero.health = -10
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_with_negative_health(self):
        enemy = Hero("Enemy", 10, -10, 10)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight Enemy. He needs to rest", str(ex.exception))

    def test_battle_with_negative_health_both_sides(self):
        hero = Hero("Hero", 10, 10, 10)
        enemy = Hero("Enemy", 10, 10, 10)
        result = hero.battle(enemy)
        self.assertEqual("Draw", result)

    def test_battle_hero_win_after_enemy_negative_health(self):
        hero = Hero("Hero", 2, 100, 10)
        enemy = Hero("Enemy", 2, 20, 10)
        result = hero.battle(enemy)
        self.assertEqual("You win", result)

    def test_battle_enemy_win_after_hero_negative_health(self):
        hero = Hero("Enemy", 2, 20, 10)
        enemy = Hero("Hero", 2, 100, 10)
        result = hero.battle(enemy)
        self.assertEqual("You lose", result)

    def test_init_after_hero_win(self):
        enemy = Hero("Enemy", 2, 20, 20)
        self.hero.battle(enemy)
        self.assertEqual(3, self.hero.level)
        self.assertEqual(65, self.hero.health)
        self.assertEqual(15, self.hero.damage)

    def test_enemy_init_after_hero_lose(self):
        hero = Hero("Enemy", 2, 20, 10)
        enemy = Hero("Hero", 2, 100, 10)
        hero.battle(enemy)
        self.assertEqual(3, enemy.level)
        self.assertEqual(85, enemy.health)
        self.assertEqual(15, enemy.damage)

    def test_hero_info(self):
        actual_result = self.hero.__str__()
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    main()
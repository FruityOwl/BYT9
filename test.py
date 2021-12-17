import unittest

from BYT9.Advertiser import Advertiser
from BYT9.Enemy import Enemy
from BYT9.Equipment import Equipment
from BYT9.Room import Room
from BYT9.Сharacter import Character


global test_character, test_equipment, test_room, test_enemy, test_adv
test_character = Character('Kiokoro', 'Warrior')
test_equipment = Equipment(1, 'Simple Sword', '+1', 'Weapon')
test_room = Room(1, 'Fight', 'Small Healing Potion')
test_enemy = Enemy(1, 'Small Slime', 'Common', 'slime.png', 'strength -2, constitution +3', 'slimy bite',
                   'play the dead')
test_adv = Advertiser(1, 'Facebook', 'Revive')

class TestCharacter(unittest.TestCase):

    def test_set_name(self):
        test_character.set_name('FruityOwl')
        self.assertEqual(test_character.get_name(), 'FruityOwl')

    def test_set_health_points(self):
        test_character.set_health_points(0)
        self.assertEqual(test_character.get_health_points(), 0)

    def test_set_char_class(self):
        test_character.set_char_class('Wizard')
        self.assertEqual(test_character.get_char_class(), 'Wizard')

    def test_set_level(self):
        test_character.set_level(10)
        self.assertEqual(test_character.get_level(), 10)


class TestEquipment(unittest.TestCase):

    def test_set_eq_id(self):
        test_equipment.set_eq_id(0)
        self.assertEqual(test_equipment.get_eq_id(), 0)

    def test_set_eq_name(self):
        test_equipment.set_eq_name('Simple Armour')
        self.assertEqual(test_equipment.get_eq_name(), 'Simple Armour')

    def test_set_eq_effects(self):
        test_equipment.set_eq_effects('+2')
        self.assertEqual(test_equipment.get_eq_effects(), '+2')

    def test_set_eq_type(self):
        test_equipment.set_eq_type('Armour')
        self.assertEqual(test_equipment.get_eq_type(), 'Armour')


class TestRoom(unittest.TestCase):

    def test_set_room_id(self):
        test_room.set_room_id(0)
        self.assertEqual(test_room.get_room_id(), 0)

    def test_set_room_type(self):
        test_room.set_room_type('Hidden Market')
        self.assertEqual(test_room.get_room_type(), 'Hidden Market')

    def test_set_room_reward(self):
        test_room.set_room_reward('Big Old Nothing')
        self.assertEqual(test_room.get_room_reward(), 'Big Old Nothing')


class TestEnemy(unittest.TestCase):

    def test_set_enemy_id(self):
        test_enemy.set_enemy_id(0)
        self.assertEqual(test_enemy.get_enemy_id(), 0)

    def test_set_enemy_name(self):
        test_enemy.set_enemy_name('Great Kobold')
        self.assertEqual(test_enemy.get_enemy_name(), 'Great Kobold')

    def test_set_enemy_type(self):
        test_enemy.set_enemy_type('Elite')
        self.assertEqual(test_enemy.get_enemy_type(), 'Elite')

    def test_set_enemy_icon(self):
        test_enemy.set_enemy_icon('eliteKobold.png')
        self.assertEqual(test_enemy.get_enemy_icon(), 'eliteKobold.png')

    def test_set_enemy_stats(self):
        test_enemy.set_enemy_stats('strength +2, constitution +2, intelligence -3')
        self.assertEqual(test_enemy.get_enemy_stats(), 'strength +2, constitution +2, intelligence -3')

    def test_set_enemy_attacks(self):
        test_enemy.set_enemy_attacks('Big Bonk')
        self.assertEqual(test_enemy.get_enemy_attacks(), 'Big Bonk')

    def test_set_enemy_abilities(self):
        test_enemy.set_enemy_abilities('Trapping Net')
        self.assertEqual(test_enemy.get_enemy_abilities(), 'Trapping Net')


class TestAdvertiser(unittest.TestCase):

    def test_set_adv_id(self):
        test_adv.set_adv_id(0)
        self.assertEqual(test_adv.get_adv_id(), 0)

    def test_set_adv_company(self):
        test_adv.set_adv_company('Twitter')
        self.assertEqual(test_adv.get_adv_company(), 'Twitter')

    def test_set_adv_ad_type(self):
        test_adv.set_adv_ad_type('Bottom')
        self.assertEqual(test_adv.get_adv_ad_type(), 'Bottom')

if __name__ == '__main__':
    unittest.TestCharacter()
    print('Passed')

import unittest

from AI import dice_roll, ability_check, attack_dice
from Armour import Armour
from Attack import Attack
from Advertiser import Advertiser
from Stats import Stats
from Weapon import Weapon
from Сharacter import Character
from Enemy import Enemy
from Equipment import Equipment
from Room import Room

global test_character, test_equipment, test_room, test_enemy, test_adv
test_stats = Stats(10, 10, 10, 14, 16, 14)
test_character = Character('Kiokoro', test_stats, 'Warrior')
test_weapon = Weapon(8, 'Physic')
test_armour = Armour(16)
test_equipment = Equipment(1, 'Simple Sword', '+1', test_weapon)
test_room = Room(1, 'Fight', 'Small Healing Potion')
test_attack = Attack('Bite', 6)
test_enemy = Enemy(1, 'Small Slime', 'Common', 'slime.png', test_stats, test_attack,
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

    def test_set_stats(self):
        test_stats_1 = Stats(12, 12, 12, 12, 18, 14)
        test_character.set_char_stats(test_stats_1)
        self.assertEqual(test_character.get_char_stats(), test_stats_1)


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
        test_armour = Armour(16)
        test_equipment.set_eq_type(test_armour)
        self.assertEqual(test_equipment.get_eq_type(), test_armour)


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


class TestAttack(unittest.TestCase):
    def test_set_attack_name(self):
        test_attack.set_attack_name('Kick')
        self.assertEqual(test_attack.get_attack_name(), 'Kick')

    def test_set_attack_damage(self):
        test_attack.set_attack_damage(8)
        self.assertEqual(test_attack.get_attack_damage(), 8)


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

    def test_set_enemy_abilities(self):
        test_enemy.set_enemy_abilities('Trapping Net')
        self.assertEqual(test_enemy.get_enemy_abilities(), 'Trapping Net')

    def test_enemy_attack(self):
        # Passes from time to time due to random factor of method
        test_enemy.enemy_attack(test_character)
        self.assertNotEqual(test_character.get_health_points(), test_character.get_char_ac())


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


class TestStats(unittest.TestCase):

    def test_set_strength(self):
        test_stats.set_strength(14)
        self.assertEqual(test_stats.get_strength(), 14)

    def test_set_dexterity(self):
        test_stats.set_dexterity(16)
        self.assertEqual(test_stats.get_dexterity(), 16)

    def test_set_constitution(self):
        test_stats.set_constitution(14)
        self.assertEqual(test_stats.get_constitution(), 14)

    def test_set_intelligence(self):
        test_stats.set_intelligence(10)
        self.assertEqual(test_stats.get_intelligence(), 10)

    def test_set_wisdom(self):
        test_stats.set_wisdom(10)
        self.assertEqual(test_stats.get_wisdom(), 10)

    def test_set_charisma(self):
        test_stats.set_charisma(10)
        self.assertEqual(test_stats.get_charisma(), 10)

    def test_modifiers(self):
        self.assertEqual(test_stats.get_str_modifier(), 0)
        self.assertEqual(test_stats.get_dex_modifier(), 0)
        self.assertEqual(test_stats.get_con_modifier(), 0)
        self.assertEqual(test_stats.get_int_modifier(), 2)
        self.assertEqual(test_stats.get_wis_modifier(), 3)
        self.assertEqual(test_stats.get_cha_modifier(), 2)


class TestWeapon(unittest.TestCase):

    def test_set_weapon_dice(self):
        test_weapon.set_weapon_dice(10)
        self.assertEqual(test_weapon.get_weapon_dice(), 10)

    def test_set_weapon_type(self):
        test_weapon.set_weapon_type('Magic')
        self.assertEqual(test_weapon.get_weapon_type(), 'Magic')


class TestArmour(unittest.TestCase):

    def test_set_armour_class(self):
        test_armour.set_armour_class(17)
        self.assertEqual(test_armour.get_armour_class(), 17)


class TestAI(unittest.TestCase):

    def test_dice_roll(self):
        self.assertIsNotNone(dice_roll())

    def test_ability_check(self):
        self.assertIsNotNone(ability_check(test_stats.get_dex_modifier()))

    def test_attack_dice(self):
        self.assertIsNotNone(attack_dice(8))


if __name__ == '__main__':
    unittest.TestCharacter()
    print('Passed')

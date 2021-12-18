import random


def dice_roll():
    return random.randrange(1, 20)


def ability_check(modifier):
    return random.randrange(1, 20) + modifier


def attack_dice(dice):
    return random.randrange(1, dice)


def generate_levels():
    pass


def generate_events():
    pass

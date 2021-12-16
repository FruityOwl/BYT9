import AI
import Сharacter


if __name__ == "__main__":
    print("Hello, stranger. Please, tell me who are you?")
    print("Enter your name.")
    name = input()
    print("Ok, I see,", name)
    print("Choose class")
    print("1. Warrior \n2. Wizard \n3. Paladin")
    ch_class = input()
    if ch_class == "1":
        ch_class = "Warrior"
    elif ch_class == "2":
        ch_class = "Wizard"
    elif ch_class == "3":
        ch_class = "Paladin"
    print("Choose stats", AI.dice_roll())

    char = Сharacter.Character(name, ch_class)
    char.info()

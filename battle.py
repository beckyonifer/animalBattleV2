import attacks as a
import characters as c


def check_both_alive(char1: c.Cat, char2: c.Cat) -> tuple:
    dead_message = ""
    dead_characters = []

    if char1.is_alive() and char2.is_alive():
        both_alive = True
    else:
        both_alive = False
        # get names of characters who died
        for char in (char1, char2):
            if not char.is_alive():
                dead_characters.append(char.name)

        if len(dead_characters) > 1:
            dead_message = " and ".join(dead_characters)
        elif len(dead_characters) == 1:
            dead_message = str(dead_characters[0])
        else:
            dead_message = ""

        dead_message = dead_message + " died"

    return both_alive, dead_message


def battle(char1, char2) -> None:
    characters_alive = char1.is_alive() and char2.is_alive()
    fight_round = 1
    hits = 1

    print("Initial character health")
    print(char1.name, char1.health)
    print(char2.name, char2.health)

    while characters_alive:
        if not hits % 2 == 0:
            attacker = char1
            victim = char2
            print("\nROUND ", fight_round)
        else:
            attacker = char2
            victim = char1

        round_attack = a.Attack(attacker, victim)
        round_hit = round_attack.hit()
        hits += 1
        print("ATTACK: ", attacker.name, "attacks", victim.name, f"-{round_hit}")
        print("health update: ", char1.name, char1.health, char2.name, char2.health)

        # check alive after each fight_round
        check_alive = check_both_alive(char1, char2)
        if check_alive[0]:
            pass
        else:
            characters_alive = False
            print("\nBATTLE OVER")
            print(check_alive[1])

        if hits % 2 == 0:
            fight_round += 1

import characters as c
import battle as b

# define characters
character1 = c.Cat(input("Character name"), int(input("strength")), 100)
character2 = c.Cat(input("Character name"), int(input("strength")), 100)

# begin battle
b.battle(character1, character2)

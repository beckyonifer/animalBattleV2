# define attack info

class Attack:
    def __init__(self, attacker, victim):
        self.attacker = attacker
        self.victim = victim

    def attack(self):
        return self.attacker.strength

    def hit(self):
        attack_strength = self.attack()
        self.victim.decrease_health(attack_strength)
        return attack_strength

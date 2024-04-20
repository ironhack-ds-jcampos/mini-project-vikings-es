import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super(). __init__(health, strength)
        self.name = name

    def attack(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super(). __init__(health, strength)
        

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health >0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        self.vikingArmy: list[Viking] = []
        self.saxonArmy: list[Saxon] = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        if len(self.saxonArmy) <= 0 or len(self.saxonArmy) <= 0:
            return None

        victim = self.saxonArmy[random.randrange(0, len(self.saxonArmy))]
        attacker = self.vikingArmy[random.randrange(0, len(self.vikingArmy))]
        res = victim.receiveDamage(attacker.strength)

        self.saxonArmy = [saxon for saxon in self.saxonArmy if saxon.health > 0]
        return res
    
    def saxonAttack(self):
        if len(self.saxonArmy) <= 0 or len(self.saxonArmy) <= 0:
            return None

        attacker = self.saxonArmy[random.randrange(0, len(self.saxonArmy))]
        victim = self.vikingArmy[random.randrange(0, len(self.vikingArmy))]
        res = victim.receiveDamage(attacker.strength)

        self.vikingArmy = [viking for viking in self.vikingArmy if viking.health > 0]
        return res

    def showStatus(self):
        if len(self.saxonArmy) <= 0:
            print("Vikings have won the war of the century!")
        elif len(self.vikingAttack) <= 0:
            print("Los Sajones han luchado por sus vidas y sobreviven otro día...")
        else:
            print("Los Vikingos y los Sajones todavía están en plena batalla.")

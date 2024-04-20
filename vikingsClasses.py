import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health < 0:
            self.health = 0
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here

    def battleCry(self):
        # your code here

    def receiveDamage(self, damage):
        # your code here

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here

    def receiveDamage(self, damage):
        # your code here

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
        # your code here
    pass

#yop
class War2:

    def __init__(self):
        # your code here

    def addViking(self, Viking):
        # your code here
    
    def addSaxon(self, Saxon):
        # your code here
    
    def vikingAttack(self):
        # your code here

    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here

    pass



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

    def attack():
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} ha recibido {damage} puntos de daño"
        else:
            return f"{self.name} ha muerto en acto de combate"
    
    def battleCry():
        return "¡Odin os posee a todos!"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super(). __init__(health, strength)
        

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health >0:
            return f"Un 'Saxon' ha recibido {damage} punto de daño"
        else:
            return f"Un 'Saxon' ha muerto en combate"

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
            print("¡Los Vikingos han ganado la guerra del siglo!")
        elif len(self.vikingAttack) <= 0:
            print("Los Sajones han luchado por sus vidas y sobreviven otro día...")
        else:
            print("Los Vikingos y los Sajones todavía están en plena batalla.")


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



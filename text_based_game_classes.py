import random

class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    
    def __str__(self):
        return f'A(n) {self.name} at level {self.level}'
    
    def defense(self):
        return self.level * random.randint(1, 12)


class Bat(Enemy):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.name = name
        self.level = level
    
    def defense(self):
        return super().defense() / 5
    

class Dragon(Enemy):
    def __init__(self, name, level, armor, fire_breathing):
        super().__init__(name, level)
        self.name = name
        self.level = level
        self.armor = armor
        self.fire_breathing = fire_breathing
    
    def defense(self):
        if self.fire_breathing:
            return super().defense() + self.armor * 8
        else:
            return super().defense() * self.armor


class Mouse(Enemy):
    def __init__(self, name, level):
        super().__init__(name, level)
        self.name = name
        self.level = level
    
    def defense(self):
        return super().defense() / 10


class Tiger(Enemy):
    def __init__(self, name, level, bite):
        super().__init__(name, level)
        self.name = name
        self.level = level
        self.bite = bite
    
    def defense(self):
        if self.bite:
            return super().defense() * 4
        else:
            return super().defense() * 2


class Wizard(Enemy):
    def __init__(self, name, level, spell, armor):
        super().__init__(name, level)
        self.name = name
        self.level = level
        self.spell = spell
        self.armor = armor
    
    def defense(self):
        if self.spell:
            return super().defense() * 5 + self.armor
        else:
            return super().defense() * 2 + self.armor


class Hero(Enemy):
    def __init__(self, name, level, armor, shield, weapon):
        super().__init__(name, level)
        self.name = name
        self.level = level
        self.armor = armor
        self.shield = shield
        self.weapon = weapon
    
    def attack(self, other):
        self.hero_attack = super().defense() + self.armor + self.shield * self.weapon
        other.other_attack = other.defense()

        if self.hero_attack >= other.other_attack:
            return True
        else:
            return False
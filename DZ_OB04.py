from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."


class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        print(self.weapon.attack())

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

def demonstrate_battle(fighter):
    fighter.attack()
    print("Монстр побежден!\n")

# Создание бойца с мечом
fighter = Fighter(Sword())

# Демонстрация боя с мечом
demonstrate_battle(fighter)

# Меняем оружие на лук и снова демонстрируем боевые действия
fighter.changeWeapon(Bow())
demonstrate_battle(fighter)
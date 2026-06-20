"""
Модуль organism.py

Содержит класс Organism, описывающий организм экосистемы.
"""


class Organism:
    """
    Класс организма.
    """

    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

    def eat(self, amount: int):
        """
        Увеличивает энергию организма.
        """
        self.energy += amount

    def spend_energy(self, amount: int):
        """
        Уменьшает энергию организма.
        """
        self.energy -= amount

    def is_alive(self) -> bool:
        """
        Проверка, жив ли организм.
        """
        return self.energy > 0

    def __str__(self):
        return f"{self.name}: энергия = {self.energy}"

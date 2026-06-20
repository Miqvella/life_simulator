"""
Модуль population.py

Содержит класс Population для работы с группой организмов.
"""

from organism import Organism


class Population:
    """
    Класс популяции организмов.
    """

    def __init__(self):
        self.organisms = []

    def add(self, organism: Organism):
        """
        Добавляет организм в популяцию.
        """
        self.organisms.append(organism)

    def alive_count(self) -> int:
        """
        Возвращает количество живых организмов.
        """
        return sum(
            1 for organism in self.organisms
            if organism.is_alive()
        )

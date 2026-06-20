"""
Модуль ecosystem.py

Содержит класс Ecosystem.
"""

from population import Population


class Ecosystem:
    """
    Класс экосистемы.
    """

    def __init__(self):
        self.population = Population()

    def add_organism(self, organism):
        """
        Добавление организма.
        """
        self.population.add(organism)

    def simulate_day(self):
        """
        Симуляция одного дня.
        """
        print("\n--- Новый день ---")

        for organism in self.population.organisms:

            if organism.is_alive():
                organism.eat(10)
                organism.spend_energy(5)

                print(
                    f"{organism.name} жив. "
                    f"Энергия: {organism.energy}"
                )

            else:
                print(f"{organism.name} мёртв.")

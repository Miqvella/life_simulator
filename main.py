"""
Главный файл проекта.
"""

from ecosystem import Ecosystem
from organism import Organism

REPOSITORY_URL = (
    "https://github.com/Miqvella/life_simulator.git"
)


def main():
    """
    Точка входа в программу.
    """

    ecosystem = Ecosystem()

    rabbit = Organism("Заяц", 20)
    fox = Organism("Лиса", 30)
    grass = Organism("Трава", 10)

    ecosystem.add_organism(rabbit)
    ecosystem.add_organism(fox)
    ecosystem.add_organism(grass)

    for day in range(3):
        print(f"\nДень {day + 1}")
        ecosystem.simulate_day()

    print(
        "\nКоличество живых организмов:",
        ecosystem.population.alive_count()
    )

    print("\nРепозиторий проекта:")
    print(REPOSITORY_URL)


if __name__ == "__main__":
    main()

"""Band class for prac_09 CP1404"""
from prac_09.musician import Musician


class Band:
    """Band class"""

    def __init__(self, name: str):
        self.name = name
        self.musicians = []

    def __str__(self):
        band_and_members = f"{self.name} "
        for musician in self.musicians:
            band_and_members += f"({Musician.__str__(musician)}), "
        return band_and_members[:-2]

    def add(self, other):
        self.musicians.append(other)

    def play(self):
        for musician in self.musicians:
            print(Musician.play(musician))

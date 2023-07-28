class Guitar:
    """Represent a guitar object"""

    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self):
        age = 2023 - self.year
        return age

    def is_vintage(self):
        if Guitar.get_age(self) >= 50:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.year < other.year

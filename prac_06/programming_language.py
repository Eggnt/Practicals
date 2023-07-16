class ProgrammingLanguage:
    """Represent a programming language object"""

    def __init__(self, name="", typing_style="", reflection="", year=0):
        """"Initialise a programming language instance"""
        self.name = name
        self.typing_style = typing_style
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing_style == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.typing_style} Typing, Reflection={self.reflection}, First appeared in {self.year}"

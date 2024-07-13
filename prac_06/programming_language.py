class ProgrammingLanguage:
    """the object of Programming Language"""
    def __init__(self, name="", typing="", reflection=True, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """determine whether the typing is dynamic"""
        return self.typing == "Dynamic"

    def __str__(self):
        """display the programming details"""
        return f"{self.name}, {self.typing}, {self.reflection}, First appeared in {self.year}"

programming = ProgrammingLanguage()


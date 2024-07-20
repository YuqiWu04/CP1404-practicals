"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""

class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, pointer):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.pointer = pointer

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}, Pointer Arithmetic= {self.pointer}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def is_pointer(self):
        return self.pointer == "Yes"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    # ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    # python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    # visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    #
    # languages = [ruby, python, visual_basic]
    # print(python)
    languages = []
    # Open the file for reading
    in_file = open('languages.csv', 'r')
    # File format is like: Language,Typing,Reflection,Year
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    # All other lines are language data
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # print(parts)  # debugging
        # Reflection is stored as a string (Yes/No) and we want a Boolean
        reflection = parts[2] == "Yes"
        # Construct a ProgrammingLanguage object using the elements
        # year should be an int
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), parts[4])
        # Add the language we've just constructed to the list
        languages.append(language)
    # Close the file as soon as we've finished reading it
    in_file.close()

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)
    for language in languages:
        if language.is_pointer():
            print(language.name)



if __name__ == "__main__":
    run_tests()
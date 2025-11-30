"""
Programming Language Class
Estimated: 8 minutes
Actual: 8 minutes 3 seconds

Missed a __str__ line
Updated time: 10 minutes 15 seconds
"""

class ProgrammingLanguage:
    """Represents a Programming Language"""
    def __init__(self, name="", typing="Static", is_reflective=False, year=0):
        """Initialise a Programming Language Instance

        name: string, Name of the Programming Language
        typing: string, type of typing of the programming language (either static or dynamic)
        is_reflective: bool, whether the programming language has reflection
        year: int, the year the programming language was created"""
        self.name = name
        self.typing = typing.title()
        self.is_reflective = is_reflective
        self.year = year

    def __str__(self):
        """Create a string to be able to print"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.is_reflective}, First appeared in {self.year}"

    def is_dynamic(self):
        """Checks if the programming language is dynamic.
        Returns True if dynamic"""
        if self.typing == "Dynamic":
            return True
        else:
            return False
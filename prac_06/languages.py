"""
Create list of languages
Estimate: 10 minutes
Actual: 6 minutes 24 seconds

Combined
Estimate: 16 minutes
Actual: 16 minutes 39 seconds
"""
from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

languages = [python,ruby,visual_basic]

print(f"The dynamically typed languages are:\n"
      f"{"\n".join([language.name for language in languages if language.is_dynamic()])}")

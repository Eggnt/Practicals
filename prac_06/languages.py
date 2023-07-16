"""est. 45 minutess, 11:45a.m.
    actual 25 minutes, 12;10p.m."""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
programming_languages = [python, ruby, visual_basic]
print(programming_languages)

print("The dynamically typed languages are:")
for language in programming_languages:
    if language.is_dynamic():
        print(language.name)

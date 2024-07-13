from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)


# create a list included these three programming details
languages = [
ProgrammingLanguage("Python", "Dynamic", True, 1991),
ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
ProgrammingLanguage("Visual Basic", "Static", False, 1991)
]

# put the name of programming languages which is dynamic into a list
dynamically_typed_languages = [programming.name for programming in languages if programming.is_dynamic()]
print(f"The dynamically typed languages are:")
for i in dynamically_typed_languages:
    print(i)
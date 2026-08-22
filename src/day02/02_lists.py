skills = ["Java", "Selenium", "PytHon", "AWS", "REST API"]

print(skills)
print(skills[0])  # Accessing the first element
print(skills[1])  # Accessing the second element
print(skills[-1])  # Accessing the last element
print(skills[1:4])  # Accessing a slice of the list
print(skills[0])
print(skills[-1])
print(len(skills))

print("Adding a new skill to the list")
skills.append("Docker")  # Adding a new skill to the list
print(skills)
print("Removing a skill from the list")
skills.remove("AWS")  # Removing a skill from the list
print(skills)
if "Python".casefold() == skills[2].casefold():
    print("Python was found")

for skill in skills:
    print(skill)

for index in range(len(skills)):
    if skills[index].casefold() == "python".casefold():
        print(f"Skill at index {index}: {skills[index]}")

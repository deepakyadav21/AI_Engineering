employee = {
    "name": "Deepak",
    "role": "Software Engineer",
    "experience": 5,
    "skills": ["Java", "Selenium", "AWS"],
    "is_active": True
}

print(employee)
print(employee["name"])  # Accessing the value of the "name" key
print(employee.get("role"))  # Accessing the value of the "role" key using
print(employee["name"])
print(employee["role"])
print(employee["experience"])
employee["experience"] = 6  # Updating the value of the "experience" key
print(employee["experience"])
employee["location"] = "Bangalore"  # Adding a new key-value pair
print(employee)
employee["role"] = "AI Engineer"
print(employee)
employee.pop("is_active")  # Removing a key-value pair
print(employee)
employee["skills"].append("Python")  # Adding a new skill to the list of skills
print(employee)
if "Python".casefold() in [skill.casefold() for skill in employee["skills"]]:
    print("Python was found in the skills list")
if "Java".casefold() in [skill.casefold() for skill in employee["skills"]]:
    print("Java was found in the skills list")
if "skills" in employee:
    print("Skills key is present in the employee dictionary")
    print("Skills:", employee["skills"])
for key, value in employee.items():
    print(key, value)    

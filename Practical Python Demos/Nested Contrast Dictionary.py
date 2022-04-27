contacts = {
    "number":4,
    "students":
    [
        {"name":"Hunter Dupre", "email":"test123@yahoo.com"},
        {"name":"Jack Dupre", "email":"test@yahoo.com"},
        {"name":"John Dupre", "email":"test123@outlook.com"},
        {"name":"Test Dupre", "email":"test123@gmail.com"},
    ]

}

for student in contacts["students"]:
    print(student["name"])
class Student:
    def __init__(self, name, grade_level):
        self.name = name
        self.grade_level = grade_level
        self.grades = []

    def add_grade(self, subject, grade):
        if 1 <= grade <= 5:
            self.grades.append((subject, grade))
            return f"{subject}: hinne {grade} lisatud"
        return "Hinne peab olema 1-5"
    
    def average(self):
        if not self.grades:
            return None
        total = 0
        for _, grade in self.grades:
            total += grade
        return total / len(self.grades)

    def status(self):
        avg = self.average()
        if avg is None:
            return "Hinded puuduvad"
        if avg >= 4:
            level = "väga tubli"
        elif avg >= 3:
            level = "rahuldav"
        else:
            level = "vajab järeleaitamist"
        return f"{self.name}({self.grade_level}. klass) – {level}, hinnete keskmine {round(avg,2)}"

s1 = Student("Remo", 10)
s2 = Student("Andry", 12)

print(s1.add_grade("Matemaatika", 5))
print(s1.add_grade("Eesti keel", 4))
print(s1.add_grade("Füüsika", 3))
print(s1.status())

print("")

print(s2.add_grade("Füüsika", 4))
print(s2.add_grade("Inglise keel", 5))
print(s2.add_grade("Keemia", 2))
print(s2.status())

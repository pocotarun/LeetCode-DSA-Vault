"""class Sikka:
    def __init__(self, value):
        self.value = value
        self.agla_sikka = None

# 1. Teen sikke banaye
sikka1 = Sikka(10)
sikka2 = Sikka(20)
sikka3 = Sikka(30)

# 2. Inko chain me joda (1 -> 2 -> 3)
sikka1.agla_sikka = sikka2
sikka2.agla_sikka = sikka3

# 3. Print karke check karte hain
print("Sikka 1 ki value:", sikka1.value) # Output: 10
print("Sikka 2 ki value (Sikka 1 ke aage wala):", sikka1.agla_sikka.value) # Output: 20

# 4. Update karna hai? Direct change karo!
sikka1.value = 500
print("Update ke baad Sikka 1:", sikka1.value) # Output: 500"""

class bottal:
    def __init__(self, Ltr):
        self.Ltr = Ltr
        # Type hint de diya, ab VS Code khush hai
        self.nextLtr: bottal | None = None

# Code ko chalane ke liye call
bislary = bottal(1)
bislary2 = bottal(2)
bislary3 = bottal(3)

# Ab Pylance roega nahi, chupchap connect karne dega
bislary.nextLtr = bislary2
bislary2.nextLtr = bislary3

# Tera purana while loop chala kar check karte hain
current = bislary
while current is not None:
    print(current.Ltr, end=" >> ")
    current = current.nextLtr
print("None")
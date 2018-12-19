class BankAccount:
 
    def __init__(self, name):
        self.owner = name
        self.balance = 0.0
 
    def getBalance(self):
        return self.balance
 
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
 
    def deposit(self, amount):
        self.balance += amount
        return self.balance

class BankAccount:
    def __init__(self, owner): 
        self.owner = owner
        self.balance = 0.0
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance



class User:
    @classmethod 
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

    @classmethod
    def from_string(cls, data_str):
        first,last,age = data_str.split(",")
        return cls(first, last, int(age))


    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

	def __repr__(self):
		return f"{self.first} is {self.age}"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        return f"{self.first} likes {thing}!"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday, {self.first}!"


user1 = User("Joe", "Johnson", 45)
user2 = User("Laura", "Leider", 65)
user3 = User("Beau", "Brigand", 38)


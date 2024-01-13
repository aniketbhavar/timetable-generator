# models.py
class Department:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

class Course:
    def __init__(self, name, prerequisites):
        self.name = name
        self.prerequisites = prerequisites

class Professor:
    def __init__(self, name, availability):
        self.name = name
        self.availability = availability

class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

class TimeSlot:
    def __init__(self, day, interval):
        self.day = day
        self.interval = interval

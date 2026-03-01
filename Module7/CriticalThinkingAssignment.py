# Critical Thinking Assignment Dictionary
# Author: Christian Campbell
# Course: CSC500 Module 7
# Date: 2/28/26

# Dictionaries for course data
room_numbers = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411
}

instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

meeting_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}


course = input("Enter a course number: ").upper()

if course in room_numbers:
    print(f"Room Number:   {room_numbers[course]}")
    print(f"Instructor:    {instructors[course]}")
    print(f"Meeting Time:  {meeting_times[course]}")
else:
    print("Course not found. Please enter a valid course number.")
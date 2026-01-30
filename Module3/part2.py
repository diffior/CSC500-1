# Part 2: 24-Hour Clock Alarm Calculator
# Author: Christian Campbell
# Course: CSC500 Module 3
# Date: 2/30/26

def calculate_alarm_time():
    """
    Calculates the time an alarm will go off on a 24-hour clock.
    Prompts user for:
    - Current time (0-23 hours)
    - Hours to wait for alarm
    Outputs the alarm time on a 24-hour clock.
    """
    
    # Get current time from user
    current_time = int(input("Enter the current time (0-23 hours): "))
    
    while current_time < 0 or current_time > 23:
        print("Invalid time. Please enter a value between 0 and 23.")
        current_time = int(input("Enter the current time (0-23 hours): "))
    
    hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))
    
    # Validate hours to wait is non-negative
    while hours_to_wait < 0:
        print("Invalid input. Hours to wait must be a non-negative number.")
        hours_to_wait = int(input("Enter the number of hours to wait for the alarm: "))
    
    # Calculate alarm time using modulo operator for 24-hour wraparound
    alarm_time = (current_time + hours_to_wait) % 24
    
    # Display result
    print(f"\nThe alarm will go off at {alarm_time}:00 on the 24-hour clock.")


# Run the program
if __name__ == "__main__":
    calculate_alarm_time()
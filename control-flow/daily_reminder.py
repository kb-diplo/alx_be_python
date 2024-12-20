task = input("Enter your task: ")  
priority = input("Priority (high/medium/low): ").lower()  
time_bound = input("Is it time-bound? (yes/no): ").lower()  

match priority:  
    case "high":  
        reminder = f"'{task}' is a high priority task"  
        if time_bound == "yes":  
            reminder += " that requires immediate attention today!"  
        else:  
            reminder += "."  
    case "medium":  
        reminder = f"'{task}' is a medium priority task"  
        if time_bound == "yes":  
            reminder += " that requires attention today!"  
        else:  
            reminder += ". Consider completing it soon."  
    case "low":  
        reminder = f"'{task}' is a low priority task"  
        if time_bound == "yes":  
            reminder += " but it's still important to address it soon."  
        else:  
            reminder += ". Consider completing it when you have free time."  

print(f"Reminder: {reminder}")
a = str(input("Enter the day:"))

match a:
    case "monday":
        print("It is the first working day")
    case "tuesday":
        print("Second day of the week")
    case "wednesday":
        print("Midweek")
    case "thursday":
        print("Almost there")
    case "friday":
        print("Last working day")
    case "saturday":
        print("Weekend")
    case "sunday":
        print("Relax") 
    case _:
        print("Invalid day.")
def guess_number():
    # Get range
    min_num = int(input("Min number: "))
    max_num = int(input("Max number: "))
    
    print(f"Think of a number between {min_num} and {max_num}")
    input("Press Enter when ready...")
    
    # Binary search
    low, high, questions = min_num, max_num, 0
    
    while low < high:
        mid = (low + high) // 2
        questions += 1
        
        answer = input(f"Q{questions}: Is your number > {mid}? (y/n): ").lower()
        
        if answer == 'y':
            low = mid + 1
        else:
            high = mid
    
    print(f"Your number is {low}! Found in {questions} questions.")

# Run the game
guess_number()
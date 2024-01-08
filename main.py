def mini_golf_tracker():
    print("Welcome to GC mini golf! What is your name?")
    name = input()
    print(f"Hi, {name}! Would you like to play 3 or 6 holes?")
    num_holes = int(input())

    if num_holes not in (3, 6):
        print("Please enter either 3 or 6 for the number of holes.")
        return

    course_par = num_holes * 3
    total_score = 0

    for hole in range(1, num_holes + 1):
        print(f"How many putts for hole {hole}? (par: 3)")
        putts = int(input())

        if putts < 0:
            print("Please enter a non-negative number of putts.")
            return

        total_score += putts

    score_diff = total_score - course_par

    if score_diff > 0:
        print(f"Nice try, {name}! Your total par was: +{score_diff}.")
    elif score_diff < 0:
        print(f"Great job, {name}! Your total par was: {score_diff}.")
    else:
        print(f"Good game, {name}! Your total par was: 0.")


# Run the function to simulate the golf game
mini_golf_tracker()

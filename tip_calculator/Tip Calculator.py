print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill?\n"))
tip_percent = float(input("What percentage of tip would you like to give? 10, 12, 15?\n"))
total_people = int(input("How many people to split the bill?\n"))
final_bill = total_bill * (tip_percent / 100) 
bill = total_bill + final_bill 
final = bill / total_people
print(f"Each person should pay ${final:.2f}")
print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What tip would you like to give? 10,12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))
sum = total_bill + total_bill*(tip_percentage/100)
final_amount = "{:.2f}".format(sum/num_of_people)
print(f"Each person should pay: ${final_amount}")
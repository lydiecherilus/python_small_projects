''' The program calculates the total bill each person should pay when dining in group including tip '''

calculation_end = False
while not calculation_end:
    print("Welcome to the bill calculator")
    bill = input("What is the total bill? $")
    tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
    total_tip = (float(bill) * float(tip)) / 100
    people = input("How many people are splitting the bill? ") 
    person_amount = (float(bill) + total_tip) / float(people)
    final_person_amount = round(person_amount, 2)
    final_person_amount = "{:.3f}".format(person_amount)
    print(f"Each person should pay: ${final_person_amount}")

    restart = input('Type "yes" if you want to calculate another bill -- otherwise type "no". \n')
    if restart == "no":
        calculation_end = True
        print("Goodbye")
        
# use this link to calculate your bill: https://replit.com/@lydiecherilus/billsplitter?v=1

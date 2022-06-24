''' The program calculates the total bill each person should pay when dining in group including tip '''

calculation_end = False
is_input_valid = False
print("Welcome to the bill calculator")

while not calculation_end and not is_input_valid: 
    try:
        bill = float(input("What was the total bill? $"))
        tip = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
        total_tip = (float(bill) * float(tip)) / 100
        people = float(input("How many people to split the bill? "))
        is_input_valid = True
        
        person_amount = (bill + total_tip) / people
        final_person_amount = round(person_amount, 2)
        final_person_amount = "{:.2f}".format(person_amount)
        print(f"Each person should pay: ${final_person_amount}")

        restart = input('Type "yes" if you want to calculate another bill -- otherwise type "no". \n')
        if restart == "no":
            calculation_end = True
            print("Goodbye")
        elif restart == "yes":
            calculation_end = False
            is_input_valid = False

    except ValueError:
        print("Please only input digits")

        
# use this link to calculate your bill: https://replit.com/@lydiecherilus/billsplitter?v=1

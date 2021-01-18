# Create a code that will ask for your marketing budget.
#  Facebook campaign = 100ILS per day.
#  Instagram campaign = 50ILS per day.
# Ask him:
# How long he wants the Facebook campaign will run.
# How long he wants the Instagram campaign will run.
# Then print to the screen the summary of the cost in ILS with tax (17%)
# If it is more than his marketing budget, tell him how much to add, if not tell him "successfull".

facebook = 100.0
instagram = 50.0

budget = input("What is your marketing budget: ")
print("Marketing budget is " + str(budget) + " ILS")

fDays = input("For how many days will the Facebook campaign run: ")
iDays = input("For how many days will the Instagram campaign run: ")


cost = (facebook * int(fDays) + instagram + int(iDays)) * 1.17
print("Cost: " + str(cost) + " ILS")
if(cost <= float(budget)):
    print("Successfull!")
else:
    toAdd = cost - float(budget)
    toAdd = round(toAdd, 2)
    print("You went over budget!")
    print("Amount missing: " + str(toAdd) + " ILS")
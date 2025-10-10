#DAILY CALORIE TRACKER 
#------------------------------------------------------
#COURSE : PROGRAMMING FOR PROBLEM SOLVING USING PYTHON
#NAME : AKANKSHA KUMARI
#ROLL NO.:2501010076
#SECTION : A
#SEMESTER : 1st
#------------------------------------------------------
#PROJECT OVERVIEW :-
#This is a simple calorie tracker code that helps user track their daily calorie intake.
#user can input meals,calorie values and can calulate their calorie intake
#compare them to daily limit
#-----------------------------------------------------------
#FEATURES :-#Add multipe meals with calorie counts
#calculate total and average calories
#warning system if limit is exceeded
#-----------------------------------------------------------
print("WELCOME TO THE DAILY CALORIE TRACKER")
print("..........................................")
num_meals=int(input("HOW MANY MEALS DID YOU HAVE TODAY?"))
meals=[]
calories=[]
for i in range(num_meals):
    meal_name=input(f"ENTER THE NAME OF MEAL{i+1}:")
    meal_cal=float(input(f"ENTER CALORIE FOR {meal_name}:"))
    meals.append(meal_name)
    calories.append(meal_cal)
print("\n-----------------------------------------------")
print("           DAILY CALORIE REPORT")
print("--------------------------------------------------")
print("MEAL\t\tCALORIES")
print("-------------------------------------------------")
for i in range(num_meals):
    print(f"{meals[i]}\t\t{calories[i]} calories")
total_calories=sum(calories)
average_calories=total_calories/num_meals
print("--------------------------------------------------")
print(f"TOTAL CALORIES CONSUMED TODAY:{total_calories}")
print(f"AVERAGE CALORIES PER MEAL:{average_calories}")
limit=float(input("\nENTER YOUR DAILY CALORIE LIMIT:"))
if total_calories > limit:
    print("YOU HAVE EXCEEDED YOUR DAILY CALORIE LIMIT!")
else:
    print("YOU ARE WITHIN YPUR DAILY CALORIE LIMIT, GREAT JOB!")





from datetime import date
exit = "YES"
current_year = date.today().year
while exit == "yes" or exit == "Yes" or exit == "YES":
 print("This is a simple age calculator")
 birth_year = int(input("What year were you born?"))
 age = current_year - birth_year
 print("Your age is", age)
 exit = input("Do you want to use age finder again? ")
if exit == "no" or exit == "No" or exit == "NO":
  print("Program ended successfully ")
else:
  print("Invalid input enter yes or no")
